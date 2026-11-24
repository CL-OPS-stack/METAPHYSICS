# METAPHYSICS

An Obsidian-style vault for metaphysics, in a deep-space look of glowing blue orbs and silver orbital arcs. It comes preloaded with study notes on all **247 entries** of *Metaphysics: The Key Concepts* (Beebee, Effingham & Goff, Routledge 2011), sorted into 16 groups with a hub note for each, plus a **Journal** for your own writing.

It is one self-contained web page: no server, no account, no build tools needed to use it.

## Features
- **Explorer** with folders for each group and a reading-status dot on every note (unread / reading / understood)
- **Read and edit modes** (`Ctrl/Cmd + E`): Markdown with properties, tables, lists and quotes
- **`[[Wikilinks]]`** with autocomplete as you type `[[`, and a preview when you hover over a link
- **Backlinks**, outgoing links, outline and a **local graph** for every note
- **Graph view** (`Ctrl/Cmd + G`): every note as an orb, coloured by group; drag, zoom, highlight and filter
- **Quick switcher** (`Ctrl/Cmd + O`), **command palette** (`Ctrl/Cmd + P`) and **full-text search** (`Ctrl/Cmd + Shift + F`)
- **Journal**: one click starts today's entry from a template
- **Rename** a note and every link to it updates
- **Export** the whole vault as a `.zip` of Markdown files, which also opens in real Obsidian; **import** `.md` files
- Works on phones: the sidebars become slide-out drawers

## Your data
Your notes are saved in your browser's local storage, on that device and in that browser only. Use **Settings → Export vault (.zip)** regularly to keep a copy.

## Put it on GitHub (GitHub Pages)
1. Create a new repository named **METAPHYSICS** on github.com.
2. Upload the contents of this folder (on a phone: **Add file → Upload files**), or from a computer:
   ```bash
   git remote add origin https://github.com/<your-username>/METAPHYSICS.git
   git push -u origin main
   ```
3. In the repository, go to **Settings → Pages**, set **Source: Deploy from a branch**, choose **main** and **/ (root)**, then save.
4. After a minute your app is live at `https://<your-username>.github.io/METAPHYSICS/`.

## Editing the app or the starter notes
- `src/app.js`, `src/app.css` and `src/template.html` hold the app's code.
- `vault/` holds the starter notes as plain Markdown.
- Run `python3 build.py` to rebuild `index.html` after changing either.

## About the notes
The notes are original study notes about the book. They paraphrase its entries, and point to page numbers instead of reproducing its text.
