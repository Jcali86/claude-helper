#!/usr/bin/env python3

from __future__ import annotations

import html
import json
import urllib.request
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from string import Template
from typing import Any
import xml.etree.ElementTree as ET

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
TEMPLATE_PATH = BASE_DIR / "templates" / "index.html"
HOST = "127.0.0.1"
PORT = 8000

POSITIVE_KEYWORDS = {
    "help",
    "helping",
    "support",
    "community",
    "celebrate",
    "celebration",
    "kindness",
    "local",
    "school",
    "library",
    "volunteer",
    "success",
    "positive",
    "hope",
    "award",
    "donate",
    "garden",
    "festival",
    "improve",
    "opens",
    "opening",
    "restores",
    "family",
}

COMMUNITY_KEYWORDS = {
    "city",
    "county",
    "local",
    "school",
    "park",
    "library",
    "community",
    "town",
    "neighborhood",
}


def load_sources() -> list[dict[str, str]]:
    with (DATA_DIR / "sources.json").open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return payload.get("sources", [])


def fetch_url(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Claude-Helper-Positive-News-Digest/1.0"
        },
    )
    with urllib.request.urlopen(request, timeout=8) as response:
        return response.read()


def parse_feed(xml_bytes: bytes, source_name: str) -> list[dict[str, str]]:
    root = ET.fromstring(xml_bytes)
    items: list[dict[str, str]] = []
    for item in root.findall(".//item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip() or "#"
        description = (item.findtext("description") or "").strip()
        items.append(
            {
                "source": source_name,
                "title": title,
                "link": link,
                "description": description,
            }
        )
    return items


def story_score(story: dict[str, str]) -> int:
    text = " ".join(
        [story.get("title", ""), story.get("description", ""), story.get("source", "")]
    ).lower()
    positive_hits = sum(1 for word in POSITIVE_KEYWORDS if word in text)
    community_hits = sum(1 for word in COMMUNITY_KEYWORDS if word in text)
    return positive_hits * 2 + community_hits


def load_stories() -> tuple[list[dict[str, Any]], list[str]]:
    stories: list[dict[str, Any]] = []
    notes: list[str] = []

    for source in load_sources():
        name = source.get("name", "Unknown source")
        url = source.get("url", "")
        if not url:
            continue
        try:
            stories.extend(parse_feed(fetch_url(url), name))
            notes.append(f"Loaded live feed: {name}")
        except Exception:
            notes.append(f"Could not load live feed, skipped for now: {name}")

    if stories:
        return stories, notes

    sample_bytes = (DATA_DIR / "sample_feed.xml").read_bytes()
    notes.append("Using local sample feed because live feeds were unavailable.")
    return parse_feed(sample_bytes, "Sample community feed"), notes


def build_digest() -> dict[str, Any]:
    stories, notes = load_stories()
    for story in stories:
        story["score"] = story_score(story)

    ranked = sorted(stories, key=lambda item: item["score"], reverse=True)
    featured = [story for story in ranked if story["score"] > 0][:6]
    if not featured:
        featured = ranked[:4]

    summary_lines = []
    for story in featured[:3]:
        summary_lines.append(
            f"{story['title']} ({story['source']}) looks like a positive or community-useful update."
        )

    return {
        "generated_at": datetime.now().strftime("%B %d, %Y at %I:%M %p"),
        "notes": notes,
        "stories": featured,
        "summary": " ".join(summary_lines)
        or "No strong matches yet, but the starter is working and ready for improvement.",
    }


def render_story_cards(stories: list[dict[str, Any]]) -> str:
    cards = []
    for story in stories:
        cards.append(
            """
            <article class="story-card">
              <p class="story-source">{source}</p>
              <h3>{title}</h3>
              <p>{description}</p>
              <p><a href="{link}" target="_blank" rel="noreferrer">Open original source</a></p>
            </article>
            """.format(
                source=html.escape(story["source"]),
                title=html.escape(story["title"] or "Untitled story"),
                description=html.escape(
                    (story["description"] or "No description available.")[:240]
                ),
                link=html.escape(story["link"]),
            )
        )
    return "\n".join(cards)


def render_notes(notes: list[str]) -> str:
    return "\n".join(f"<li>{html.escape(note)}</li>" for note in notes)


def render_page() -> bytes:
    digest = build_digest()
    template = Template(TEMPLATE_PATH.read_text(encoding="utf-8"))
    page = template.substitute(
        generated_at=html.escape(digest["generated_at"]),
        summary=html.escape(digest["summary"]),
        notes=render_notes(digest["notes"]),
        story_cards=render_story_cards(digest["stories"]),
    )
    return page.encode("utf-8")


class DigestHandler(BaseHTTPRequestHandler):
    def send_digest_response(self, body: bytes | None = None) -> None:
        if self.path not in {"/", "/index.html"}:
            self.send_error(404, "Page not found")
            return

        response_body = body if body is not None else render_page()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(response_body)))
        self.end_headers()

        if body is not None:
            self.wfile.write(response_body)

    def do_GET(self) -> None:
        self.send_digest_response(render_page())

    def do_HEAD(self) -> None:
        self.send_digest_response()

    def log_message(self, format: str, *args: Any) -> None:
        return


def main() -> None:
    server = HTTPServer((HOST, PORT), DigestHandler)
    print(f"Positive Local News Digest running at http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
