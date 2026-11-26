# Tekryno — Google Fonts release-candidate QA review

Last checked: 2026-11-26

## Technical validation

- Google Fonts Fontspector profile: **109 PASS, 0 FAIL, 10 WARN, 11 INFO, 83 SKIP**.
- Encoded GF Latin Core coverage: **319/319 required codepoints present**; see `LATIN-CORE-COVERAGE.md`.
- Final font name: `Tekryno`, style `Regular`, PostScript `Tekryno-Regular`.
- Fonts: `fonts/ttf/Tekryno-Regular.ttf` and `fonts/otf/Tekryno-Regular.otf`.
- Source: editable UFO and original Illustrator SVG artwork are committed.

## Warnings requiring design-aware review

1. **METADATA subset reachability:** Certain encoded accent and combining-mark characters would be unreachable in the default Google Fonts subsets. This warning arises during downstream subset metadata evaluation. Onboarding metadata needs review.
2. **Lcaron and similar diacritics:** The checker cannot evaluate some decomposed outlines; manually inspect the characteristic caron shape.
3. **Contour counts:** `two`, `five`, `section` differ from typical reference fonts. Review but do not automatically replace the intentionally modular geometry.
4. **Language shaping:** Missing auxiliary orthography characters in some languages; these are outside the official encoded GF Latin Core minimum set. Confirm target language claims and test representative text.
5. **Near-alignment:** `asterisk` and `registered` have points within 1–2 units of major metrics; consider visual QA.
6. **Short segments:** Several design outlines have short segments, most visibly in `Q`, `five`, `eight`, and ampersand. Review for glitches before changing shapes.
7. **Vendor ID:** Unregistered `SGPR` in OS/2. Registration is optional; this is a warning, not an automatic font failure.

The 10 WARN instances above are grouped into seven distinct check categories. Full authoritative tool output:
`FONTSPECTOR-REPORT.md`.

## Additional source and release tasks

- **Resolved:** Corrected UFO dotted-circle alignment and unified mark feature generation; a pinned build now matches the approved TTF byte-for-byte. See `SOURCE-REPRODUCIBILITY.md`.
- Confirm licensing attribution, Google Fonts Contributor License Agreement and final name review.
- Obtain independent font design assessment; passing technical checks does not guarantee Google Fonts curation acceptance.
