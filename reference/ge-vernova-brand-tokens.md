# GE Vernova Brand Tokens — OFS Training Delivery

Reference this before building any branded document, deck, or dashboard for GE Vernova OFS Training. Source: GE Vernova OFS Training Design System.

## Color

| Token                               | Hex                             | Use                                                                                                     |
| ------------------------------------ | -------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `--gv-evergreen`                    | `#005e60`                       | Primary brand color (official Evergreen, logo color). Headers, footers, primary buttons, table headers. |
| `--gv-evergreen-deep` / `--gv-teal` | `#004a4c`                       | Legacy HLC OFS deep teal — two-tone header/nav look.                                                    |
| `--gv-teal-doc`                     | `#0d6e6e`                       | Controlled Word-doc heading color.                                                                      |
| `--gv-lime` (Urgency Green)         | `#c8ff08`                       | Signature accent — bottom rules, CTA text/borders, key numbers. Use sparingly, never as a large fill.   |
| `--gv-teal-hi`                      | `#59c3c9`                       | Supporting bright teal.                                                                                 |
| `--gv-tan`                          | `#bfa682`                       | Supporting warm neutral.                                                                                |
| `--gv-bg`                           | `#f0f2f0`                       | Page background.                                                                                        |
| Card background                     | `#ffffff`                       | Card/panel background.                                                                                  |
| `--gv-night`                        | `#212121`                       | Ink / headline text.                                                                                    |
| Body text                           | `#444444`                       | Body copy.                                                                                              |
| Muted text                          | `#888888`                       | Secondary/meta text.                                                                                    |
| Border                              | `#e5e7eb`                       | Hairlines (controlled-doc tables use `#cccccc`).                                                        |
| Critical/action                     | `#e63946`                       | RAG — critical.                                                                                         |
| Warning/reminder                    | `#f5a623`                       | RAG — warning.                                                                                          |
| Success/new                         | `#75ca64` (text-safe `#2d7a45`) | RAG — success.                                                                                          |
| Info/updated                        | `#59c3c9`                       | RAG — info.                                                                                             |

## Type

- **Display (headlines):** Sons Condensed (Klim Type Foundry) — Extrabold for H1, Semibold for H4. Always ALL CAPS (except program names). Fallback: Saira Condensed (Google Fonts) → Arial Narrow.
- **Body/text:** Inter — Regular/Semi Bold, ~20% extra leading. Body copy 14px, line-height 1.6–1.7.
- **Non-Latin scripts:** Noto Sans (Black headlines / Regular body).
- **Email/legal/CAD:** Arial replaces Inter.
- **Micro-labels/eyebrows:** UPPERCASE, 10–13px, +0.8–2px letter-spacing.
- Font files (verified, live in repo): `reference/fonts/SonsCondensed-Extrabold.ttf`, `reference/fonts/SonsCondensed-Semibold.ttf`.

## Logo

- Path (verified, live in repo): `reference/logo/`
  * `ge-vernova-evergreen.png` / `.svg` — light backgrounds
  * `ge-vernova-white.png` / `.svg` — dark backgrounds (e.g., on Evergreen headers)
  * `ge-vernova-black.png` / `.svg` — print/pure black-background use
- Rules: Monogram + wordmark always locked together, horizontal, intact. Clear space ≥ 40% of Monogram height. Min height 25px (digital). Never recolor, skew, outline, or use the Monogram alone.

## Corner radii

Badge 3px · button/control 6px · callout/toggle 8px · card/panel 10px · pill/chip 20px.

## Full design system

Original Design-exported bundle path (`_ds/ge-vernova-ofs-training-design-system-bdce87b1-cf6e-44c8-a53e-36a36984975a/`) is not populated in this repo — only this tokens file made it out of Design. The verified, working assets are the flattened `reference/fonts/` and `reference/logo/` paths above. If a full component/token bundle gets exported from Design later, drop it at `reference/_ds/` and update this section.
