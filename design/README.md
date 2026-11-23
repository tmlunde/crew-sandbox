# Design

This folder is the one shared place for design work. Screens are
sketched here before anything is built, so the team can agree on
them first.

Everything is plain Markdown. No design tools are needed to read or
change it.

## Where things go

```
design/
├── README.md     # This page
├── screens/      # One file per screen: low-fi wireframes
├── sketches/     # Rough ideas and explorations, not yet a screen
└── notes/        # Research, customer needs, decisions
```

- **screens/**: a screen the team means to build. It has a wireframe,
  says who it is for, and lists what is still open.
- **sketches/**: quick tries, other options, things thrown away. A
  sketch can be messy. When one is chosen, it moves to `screens/`.
- **notes/**: what we learned and why we chose what we did. Things
  like customer quotes, needs, and decision logs.

Make a subfolder only when you first need it. Empty folders are not
kept.

## How files are named

```
<area>-<what>.md
```

- Lowercase, words joined by hyphens.
- Start with the area of the product, then what the file shows.
- Examples: `account-sign-in.md`, `tasks-list.md`, `tasks-empty-state.md`.
- Sketches add a short tag for the option: `tasks-list-option-b.md`.
- Notes start with the date: `2026-11-22-owner-interview.md`.

## What a screen file holds

Copy the example in [screens/account-sign-in.md](screens/account-sign-in.md).
Each screen file has these parts, in this order:

1. **Header**: status (`draft`, `in review`, `agreed`, `built`) and
   the task id it came from.
2. **Who and why**: who uses this screen and what they need from it.
3. **Wireframe**: a text drawing in a code block. Boxes, labels,
   and `[Buttons]`. Low-fi on purpose: no colours or fonts.
4. **Parts**: a short list of what each piece does.
5. **States**: empty, loading, error, and so on.
6. **Open questions**: what still needs an answer before building.

## How work moves

1. Start a sketch in `sketches/` when an idea is still loose.
2. Once it is picked, move it to `screens/` and set status `draft`.
3. Open a pull request and set status `in review`.
4. When the owner agrees, set status `agreed`. It can be built now.
5. When it ships, set status `built`.
