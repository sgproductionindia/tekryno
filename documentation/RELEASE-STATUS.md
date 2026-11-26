# Tekryno — publication and Google Fonts status

## Public project assets: COMPLETE

All of the following are live in https://github.com/sgproductionindia/tekryno:

- `OFL.txt` (SIL OFL 1.1, no Reserved Font Name), authors and contributors.
- `fonts/ttf/Tekryno-Regular.ttf` and `fonts/otf/Tekryno-Regular.otf`.
- `sources/Tekryno-Regular.ufo`, `sources/features.fea`, original Illustrator SVG artwork, and build helper.
- Specimen PDF plus editable SVGs and preview image in `documentation/specimen/`.
- Production documentation, GitHub Actions importer, and automated Fontspector QA workflow.

The initial automatic ZIP extraction failed because the importer incorrectly treated an already-published build helper as a file it also had to extract. The issue was corrected and the second GitHub Actions run succeeded. The compressed ZIP was removed after the files were published.

## Latest technical QA — 2026-11-26

- Fontspector googlefonts profile: **109 PASS, 0 FAIL, 10 WARN, 11 INFO, 83 SKIP**.
- All **319 of 319** required encoded GF Latin Core codepoints are present.
- Full report: `documentation/FONTSPECTOR-REPORT.md`.
- Manual warning review: `documentation/QA-REVIEW.md`.
- **Source reproducibility PASS**: Independent GitHub Actions verified that editable UFO + feature sources rebuild the release TTF byte-for-byte with pinned fontTools 4.63.0. Evidence: `documentation/SOURCE-REPRODUCIBILITY.md`.

## Outstanding review and onboarding

1. Review Fontspector warnings, diacritic shapes, and small-size/readability specimens without discarding the original display design.
2. Respond to Google Fonts team in [proposal #11520](https://github.com/google/fonts/issues/11520) if they request refinements.
3. Further trademark/name clearance if needed; Fontdata reported no exact Tekryno match.
4. Await independent review and possible onboarding; the user reports submitting the Google CLA on 2026-11-26 (not independently verified).

**Google Fonts submission status:** Issue [google/fonts#11520](https://github.com/google/fonts/issues/11520) is open. On 2026-11-26, Google's bot flagged the original customized form (`X Form not completed`); the author has now posted the exact official checklist in a new comment as requested. Re-triage is pending; the label had not yet changed when checked. **Google Fonts acceptance: NOT GRANTED.**
