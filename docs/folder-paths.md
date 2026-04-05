# Folder Paths On Mac

If a path looks confusing, this file is for you.

## What Is A Folder Path?

A folder path is the "address" of a file or folder on your Mac.

Example:

```text
/Users/yourname/Documents/Claude-Helper
```

That means:

- start at your Mac user account
- go into `Documents`
- then open the `Claude-Helper` folder

## Fastest Beginner Method

The easiest way to avoid typing a path by hand is:

1. Open `Finder`.
2. Find the folder you want.
3. Drag that folder into the Terminal window.

Your Mac will paste the full path for you.

## Another Easy Method

1. In `Finder`, open the folder you want.
2. Right-click the folder name or file.
3. Look for `Copy` options that include the path name if your version of macOS shows them.
4. Paste that path into Terminal.

## What Does `~` Mean?

The `~` symbol means "your Home folder."

So:

```text
~/Documents
```

means the same kind of place as:

```text
/Users/yourname/Documents
```

## If The Path Is Wrong

Common signs:

- Terminal says `No such file or directory`
- a command works for someone else but not on your Mac
- you copied an example path and forgot to change the username or folder name

## Plain-English Example

If someone tells you to use:

```text
/Users/jamie/Documents/Project
```

and your Mac username is `Chris`, you would need:

```text
/Users/Chris/Documents/Project
```

## Best Habit

If you are unsure, do not guess.

Use Finder, then drag the folder into Terminal.
