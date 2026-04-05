# Positive Local News Digest

This folder is a real beginner-friendly starter project, not just an idea.

It gives you a simple local web app that:

- reads a small list of news or community feeds
- looks for positive or community-helpful stories
- generates a short digest
- shows the result in a browser
- can later be containerized with Docker

## Why This Project Matters

This is a good example of using AI and automation in a positive way:

- it helps people feel more connected to their area
- it can highlight good news instead of only stressful news
- it can be adapted for schools, libraries, local groups, and neighborhoods

## What Is Included

- `app.py`: the local server and digest generator
- `data/sources.json`: a starter list of feed URLs
- `data/sample_feed.xml`: local sample data so the app still works as a demo
- `templates/index.html`: the browser page template
- `Dockerfile`: a simple container setup

## Run It Locally

From inside this folder:

```bash
python3 app.py
```

Then open:

```text
http://localhost:8000
```

## What Happens When You Run It

- the app tries to fetch the feeds in `data/sources.json`
- if that fails, it falls back to `data/sample_feed.xml`
- it filters for positive language
- it creates a digest page with featured stories and source links

## Good Beginner Prompt For Claude Code

```text
Please explain this project in plain language.
Show me what each file does, then help me improve it one small step at a time.
If there is a safer or simpler way to do something, tell me before changing it.
```

## Next Improvements You Could Ask Claude For

- send the digest by email
- let me add my own town or city sources
- add a better positivity filter
- save old digests by date
- add a settings page for non-technical users

## Docker

This project includes a `Dockerfile` for later use. Once Docker is installed, the expected flow is:

```bash
docker build -t positive-news-digest .
docker run -p 8000:8000 positive-news-digest
```

## Note

This starter uses simple keyword filtering, not advanced AI classification. That keeps the project easier to understand for beginners and gives Claude Code a solid base to improve later.
