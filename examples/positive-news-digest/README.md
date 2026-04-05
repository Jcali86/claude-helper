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

## Best Claude Code Prompts For This Project

Do not use the same prompt for every job.

If you want Claude Code to be genuinely useful here, pick the prompt that matches what you want to do.

### 1. Learn This App

Use this first if you want to understand the starter before changing anything.

```text
Please explain this project in plain language.
Walk me through what each file does, how the app works right now,
and where the current limits are.
Assume I am new to Terminal and beginner coding projects.
If there is any part that is easy to misunderstand, slow down and explain it clearly.
```

### 2. Improve This App Safely

Use this when you want Claude to review the current starter and make one sensible improvement at a time.

```text
Please review this project and suggest the next best small improvement.
Explain the tradeoffs in plain English before changing anything.
Then implement only one improvement at a time, test it, and summarize what changed.
If there is a safer or simpler way to do something, tell me before making the change.
```

### 3. Build The Fuller Version In Phases

Use this when you want Claude Code to turn the starter into a more complete local app instead of just explaining what is already here.

```text
Please turn this starter into a more complete local app.
Keep it local-first and explain each step in plain English.
Work in phases instead of trying to do everything at once.
Pause at the end of each phase, summarize what changed, and tell me the next safe step.

Build it in this order:

Phase 1:
- let me add my own town or city sources
- add a better positivity filter

Phase 2:
- save old digests by date
- add a settings page for non-technical users

Phase 3:
- send the digest by email
```

## Suggested Improvement Roadmap

If you are not sure where to start, use this order:

### Phase 1: Better Inputs And Better Results

- let me add my own town or city sources
- add a better positivity filter

### Phase 2: Make It More Useful Day To Day

- save old digests by date
- add a settings page for non-technical users

### Phase 3: Add Delivery

- send the digest by email

## Docker

This project includes a `Dockerfile` for later use. Once Docker is installed, the expected flow is:

```bash
docker build -t positive-news-digest .
docker run -p 8000:8000 positive-news-digest
```

## Note

This starter uses simple keyword filtering, not advanced AI classification. That keeps the project easier to understand for beginners and gives Claude Code a solid base to improve later.
