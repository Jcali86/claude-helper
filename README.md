# Claude Helper

Claude Helper is a beginner-friendly guide for people who are new to AI, Mac apps, Terminal, and trying to figure out what Claude is actually good for.

The goal is simple: help someone go from "I mostly use my phone or browser" to "I can use Claude Chat, Cowork, and Code with confidence."

If you learn best by seeing things, this repo includes visual walkthroughs, real Claude screenshots, and plain-English prompts you can actually reuse.

## How To Use This Repo

This README is the repo-facing version.

If you are reading this on GitHub, start with the guides below.

If you want the learner-friendly website version, open [index.html](index.html) or the published Pages site when the repo is public again.

## Start Here If You Are New

1. Read the GitHub version of the visual guide: [docs/first-10-minutes.md](docs/first-10-minutes.md)
2. Learn the difference between Claude modes: [docs/chat-code-cowork.md](docs/chat-code-cowork.md)
3. If something goes wrong, open: [docs/common-issues.md](docs/common-issues.md)
4. If file paths feel confusing, open: [docs/folder-paths.md](docs/folder-paths.md)

## What "Using Claude Effectively" Means

In this repo, "effective" means:

- using normal language instead of unnecessary jargon
- understanding what each Claude mode is actually good for
- knowing what to click, paste, or ask next
- fixing common Mac and Terminal problems without panic
- using AI for useful, positive, real-life outcomes

## Which Claude Option Should I Use?

`Chat`

Use this when you want to ask, learn, plan, write, or talk through an idea.

`Cowork`

Use this when a task has more steps, more context, or feels like a lot and you want a guided partner.

`Code`

Use this when you want Claude to help inside a real folder on your Mac, explain Terminal commands, work with files, or build something step by step.

More detail: [docs/chat-code-cowork.md](docs/chat-code-cowork.md)

## One Important Thing Before You Use Claude Code

Claude Code is not reading your whole computer by magic.

It works best when you open the right project folder first.

Claude Code can read the files in the folder you opened.

It cannot guess the right project if the wrong folder is open.

In plain English:

1. Open Claude Code.
2. Open the folder for the project you want help with.
3. Then paste your prompt.

That gives Claude Code the file context it needs.

Most beginners do not need a skill or integration to ask questions or start a simple project.

If you are not sure whether Claude Code is looking at the right folder, say:

```text
I am new to this. Before we change anything, please tell me what folder and files you can currently see.
```

## Visual Walkthroughs

These were added for people who learn better by seeing examples:

- learner-friendly homepage: [index.html](index.html)
- visual first-run guide: [docs/first-10-minutes.html](docs/first-10-minutes.html)
- markdown version for GitHub reading: [docs/first-10-minutes.md](docs/first-10-minutes.md)
- browser-friendly modes guide: [docs/chat-code-cowork.html](docs/chat-code-cowork.html)
- browser-friendly common issues guide: [docs/common-issues.html](docs/common-issues.html)
- browser-friendly folder paths guide: [docs/folder-paths.html](docs/folder-paths.html)
- browser-friendly example app guide: [docs/positive-news-example.html](docs/positive-news-example.html)
- real Claude Chat screenshots page: [docs/chat-examples.html](docs/chat-examples.html)
- real Claude Cowork screenshots page: [docs/cowork-examples.html](docs/cowork-examples.html)
- real Claude Code screenshots page: [docs/code-examples.html](docs/code-examples.html)
- setup and customization screenshots page: [docs/setup-examples.html](docs/setup-examples.html)

## What Is In This Repo

- beginner homepage for sharing with others: [index.html](index.html)
- simple setup script: [setup.sh](setup.sh)
- visual FAQ page: [docs/faq.html](docs/faq.html)
- beginner mode guide: [docs/chat-code-cowork.md](docs/chat-code-cowork.md)
- visual first 10 minutes guide: [docs/first-10-minutes.md](docs/first-10-minutes.md)
- common setup fixes: [docs/common-issues.md](docs/common-issues.md)
- plain-English Mac path help: [docs/folder-paths.md](docs/folder-paths.md)
- positive AI ideas: [docs/positive-ideas.md](docs/positive-ideas.md)
- source links for keeping things current: [docs/sources.md](docs/sources.md)
- runnable starter for a positive local news app: [examples/positive-news-digest/README.md](examples/positive-news-digest/README.md)

## Positive Ways To Use AI

This repo focuses on helpful, grounded use cases such as:

- creativity prompts and family game ideas
- school support and study planning
- writing help in plain language
- organizing projects and daily life
- helping older adults understand scam risks and privacy basics
- finding trustworthy help, local services, food banks, or local news sources
- building simple automations that save time without becoming a second job

## Example App In This Repo

The repo now includes a real starter for a "positive local news digest" app:

- it reads trusted sources
- it looks for community-positive stories
- it creates a simple digest page
- it can run locally with Python
- it includes a Dockerfile for later container use

Open the learner-friendly guide here: [docs/positive-news-example.html](docs/positive-news-example.html)

Open the repo project here: [examples/positive-news-digest/README.md](examples/positive-news-digest/README.md)

## Launch-Day Installer

This one-line installer is for the public version of the project.

If the repo is private, skip this for now and use the guides directly.

Use it when the repo is public and ready to share widely.

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/Jcali86/claude-helper/main/setup.sh)
```

What it does:

- downloads or updates the repo into `~/Documents/Claude-Helper`
- opens the main beginner pages
- opens the project folder in Finder

## If You Get Stuck

Start with:

- [docs/common-issues.md](docs/common-issues.md)
- [docs/folder-paths.md](docs/folder-paths.md)
- [docs/faq.html](docs/faq.html)

## Notes

- This repo is designed to be friendly first and technical second.
- If a step feels confusing, rewrite it in even plainer words and trim the fluff.
- If tools change over time, check the latest links in [docs/sources.md](docs/sources.md).
