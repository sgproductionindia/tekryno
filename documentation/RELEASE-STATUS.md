# Tekryno — publication and Google Fonts status

## Public project assets: COMPLETE

All of the following are live in https://github.com/sgproductionindia/tekryno:

- `OFL.txt` (SIL OFL 1.1, no Reserved Font Name), authors and contributors.
- `fonts/Tekryno-Regular.ttf` and `fonts/Tekryno-Regular.otf`.
- `sources/Tekryno-Regular.ufo`, `sources/features.fea`, original Illustrator SVG artwork, and build helper.
- Specimen PDF plus editable SVGs and preview image in `documentation/specimen/`.
- Production documentation, GitHub Actions importer, and automated Fontspector QA workflow.

The initial automatic ZIP extraction failed because the importer incorrectly treated an already-published build helper as a file it also had to extract. The issue was corrected and the second GitHub Actions run succeeded. The compressed ZIP was removed after the files were published.

## Latest technical QA — 2026-11-26

- Fontspector googlefonts profile: **109 PASS, 0 FAIL, 10 WARN, 11 INFO, 83 SKIP**.
- All **319 of 319** required encoded GF Latin Core codepoints are present.
- Full report: `documentation/FONTSPECTOR-REPORT.md`.
- Manual warning review: `documentation/QA-REVIEW.md`.

## Remaining for Google Fonts submission

1. Reconcile one dotted-circle UFO rebuild outline and compiled GPOS differences.
2. Complete manual warning, diacritics and readability proofing.
3. Check font-name availability. The original designer reported submitting the Google CLA on 2026-11-26 (not independently verified).
4. Submit through Google's new-font intake and undergo independent review.

**Google Fonts submission status: NOT SUBMITTED. Google Fonts acceptance: NOT GRANTED.**
