# Google Fonts requirements audit and metrics candidate

Date: 2026-11-26  
Google Fonts submission: [google/fonts#11520](https://github.com/google/fonts/issues/11520)  
Approved public release: **Tekryno 1.003** (unchanged)  
Isolated candidate: **Tekryno 1.004** in [review/metrics-v1.004](https://github.com/sgproductionindia/tekryno/tree/review/metrics-v1.004)

## Official requirements reviewed

Google Fonts Guide:
- [Overall font files requirements](https://googlefonts.github.io/gf-guide/requirements.html)
- [Static fonts specifics](https://googlefonts.github.io/gf-guide/statics.html)
- [Vertical metrics](https://googlefonts.github.io/gf-guide/metrics.html)
- [Upstream repository structure](https://googlefonts.github.io/gf-guide/upstream.html)

### Confirmed compatible

- [x] Correct family **Tekryno**, style **Regular**, source TTF filename `Tekryno-Regular.ttf`.
- [x] Public upstream structure, source UFO, separate TTF/OTF directories, copyright, OFL-1.1 and build instructions.
- [x] Family Regular linking and installable embedding (`fsType = 0`, USE_TYPO_METRICS enabled).
- [x] `hhea` and OS/2 typo ascender/descender correspond; line gaps are zero.
- [x] GF Latin Core codepoints: 319/319; the Google submission bot confirmed 324/324 required Latin Core glyphs.
- [x] Editable UFO reproducibility: byte-for-byte identical to published 1.003 TTF using pinned fontTools 4.63.0.
- [x] Google Fonts Fontspector profile: published TTF **109 PASS, 0 FAIL, 10 WARN**, with human warning review ongoing.

### Production findings that require a release decision

**1. Vertical metrics.** The current 1.003 font has a 1000-unit UPM and actual bounding yMax=977, yMin=-173. Its OS/2 Windows values are WinAscent=1220 and WinDescent=260, not the exact extrema recommended by GF. Its typo/hhea ascent=1220, descent=-260 gives line spacing of 1480 units (**148% of UPM**), above GF's suggested 120–130% interval.

An experimental **1.004** revision proposes:
- WinAscent **977**, WinDescent **173** (exact outline bounds).
- Typo and hhea ascent **1000**, descent **-300** (130% of UPM).
- Unhinted TrueType `gasp` range `0x000A` instead of `0x000F`, as suggested in Google's static-font guidance.
- Version metadata updated from 1.003 to 1.004.

All approved glyph outlines, widths, Unicode mappings, kerning and GPOS mark positioning are preserved. The new metrics **change default line height** and therefore require a designer release decision before replacing 1.003.

[Metrics candidate GitHub Actions run](https://github.com/sgproductionindia/tekryno/actions/runs/45796112320): **SUCCESS**, including candidate Fontspector Google Fonts profile. Candidate TTF/OTF and QA outputs are stored in that run's downloadable artifact.

**2. Numeral spacing.** The approved release uses equal 895-unit advances for digits 0–9 and has no `tnum` feature. The Guide describes proportional numerals as the default with an accompanying tabular number feature. Since Tekryno deliberately uses a modular techno/display design, a design decision or Google reviewer clarification is needed here. This is **not** a current Fontspector FAIL. We will not introduce arbitrary alternate numeral shapes or widths without an approved design.

**3. Other warnings and accent aesthetics.** The published Fontspector report lists 10 WARN instances (7 check categories). Previous visual proofs found no blatant rendering faults, but Ľ/ľ apostrophe-like caron, language aux glyph coverage, mark combinations and small-size browser/desktop proofing remain subject to review. The unregistered four-character vendor ID is optional, not grounds to redesign glyphs.

### Google Fonts issue triage

The original [issue #11520](https://github.com/google/fonts/issues/11520) was edited to the exact official template, and the author also posted the official checklist as a comment. **Google's `X Form not completed` label remains**. Google Fonts' Gemini triage workflow is owner-controlled; a correction in a comment is not guaranteed to clear the label. The linked GitHub connector does not have permission to edit labels, trigger maintainer triage, or post comments in google/fonts. A Google Fonts maintainer must re-evaluate the issue. Do not create a duplicate submission.

## Outstanding

- [ ] Review potential visual impact of v1.004 line-height candidate; optionally approve a new numbered release.
- [ ] Determine correct default numeral treatment for the display design; consult Google Fonts if needed.
- [ ] Complete design-aware QA of accent forms and language shaping.
- [ ] Ask Google Fonts to re-triage the corrected official issue and clear stale `X Form not completed` label when appropriate.
- [ ] Obtain human design assessment and final curated Google Fonts acceptance.

This report separates verified technical findings, GF recommendations, and decisions reserved for the designer or Google Fonts. No assertion of full contributing compliance is made.
