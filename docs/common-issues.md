# Common Issues

This page is for the moments where something does not work the first time.

## "Operation not permitted"

This usually means your Mac is protecting a folder or app until you allow access.

Try:

- check whether macOS showed a permission popup behind another window
- open `System Settings > Privacy & Security`
- allow access if Terminal or your coding app is listed there
- run the command again after approving it

## "git: command not found"

Git is a basic tool used to download and update many coding projects.

On most Macs, the fix is:

```bash
xcode-select --install
```

After the install finishes, close Terminal, open it again, and retry.

## "curl: command not found"

This is uncommon on a modern Mac. If it happens:

- update macOS if possible
- restart Terminal
- if it still fails, ask Claude to help you install `curl` safely for your Mac version

## "No such file or directory"

This usually means the folder path is wrong.

Start here:

- [folder-paths.md](folder-paths.md)

## A command pasted weirdly

Sometimes smart quotes or hidden formatting break a Terminal command.

Try:

- copy the command again from the README
- make sure the quote marks look normal, like `"this"`
- paste into a plain Terminal window, not into Notes first

## The folder opened, but not the file I expected

Open the project folder, then open these files first:

- [README.md](../README.md)
- [docs/faq.html](faq.html)
- [docs/chat-code-cowork.md](chat-code-cowork.md)

## Claude seems confused about what project I mean

This usually means Claude Code is not looking at the right folder yet.

Try:

- open the project folder first in Claude Code
- ask: `Before we start, please tell me what folder and files you can currently see.`
- if the folder is wrong, open the correct one and ask again

## I do not know where my files are on a Mac

That is normal if you usually work in a browser or on a phone.

Use this guide:

- [folder-paths.md](folder-paths.md)

## I am worried I will break something

A good rule:

- do not paste commands you do not understand into random places
- use trusted repos and official docs
- ask Claude to explain a command before you run it
- keep copies of important files before big changes

## Safety Reminder

Do not use AI tools to:

- share private passwords
- expose banking or medical data in unsafe places
- run security or hacking tools on systems you do not own or manage

If you are unsure, slow down and ask for a plain-English explanation first.
