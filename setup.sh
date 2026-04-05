#!/usr/bin/env bash

set -euo pipefail

REPO_URL="${REPO_URL:-https://github.com/Jcali86/claude-helper.git}"
INSTALL_DIR="${INSTALL_DIR:-$HOME/Documents/Claude-Helper}"

print_block() {
  printf "\n%s\n" "$1"
}

need_command() {
  command -v "$1" >/dev/null 2>&1
}

print_block "Claude Helper setup is starting."
print_block "This script will place the project in: $INSTALL_DIR"

if ! need_command curl; then
  print_block "curl is not installed on this Mac. Please install it or update macOS, then try again."
  exit 1
fi

if ! need_command git; then
  print_block "Git is not installed yet."
  print_block "On most Macs, the easiest fix is to run:"
  printf "\n  xcode-select --install\n\n"
  print_block "Then run this setup command again."
  exit 1
fi

mkdir -p "$(dirname "$INSTALL_DIR")"

if [ -d "$INSTALL_DIR/.git" ]; then
  print_block "An existing Claude Helper folder was found, so it will be updated."
  git -C "$INSTALL_DIR" pull --ff-only || true
else
  print_block "Downloading Claude Helper into your Documents folder."
  git clone "$REPO_URL" "$INSTALL_DIR"
fi

print_block "Opening the most helpful files for you."

if [ -f "$INSTALL_DIR/docs/faq.html" ]; then
  open "$INSTALL_DIR/docs/faq.html"
fi

if [ -f "$INSTALL_DIR/README.md" ]; then
  open "$INSTALL_DIR/README.md"
fi

open "$INSTALL_DIR"

print_block "Setup complete."
print_block "Next steps:"
printf "%s\n" \
  "1. Read the FAQ page that just opened." \
  "2. Read the README for the simple path forward." \
  "3. If you get stuck, open docs/common-issues.md." \
  "4. If a folder path is confusing, open docs/folder-paths.md."
