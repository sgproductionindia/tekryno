# Tekryno

**Tekryno** is an original geometric, angular, futuristic display typeface designed by **Shrawan Gaikwad**. Its letterforms take inspiration from electronic music and modular shapes. Uppercase and lowercase input intentionally display uppercase-style designs.

![Tekryno type specimen](documentation/specimen/Tekryno-Overview.jpg)

**Status:** Public OFL-1.1 release candidate and editable source repository. [Google Fonts submission #11520](https://github.com/google/fonts/issues/11520) is open and awaiting independent review. **Not yet accepted or published.**

## Font family

- Menu family: **Tekryno**
- Style: **Regular**
- OpenType PostScript name: **Tekryno-Regular**
- Glyphs: **218**; Unicode mappings: **327**
- Required GF Latin Core codepoints: **319 of 319 present**
- Specimen branding: **TEKRYNO**

## Download and sources

- [TrueType font](fonts/ttf/Tekryno-Regular.ttf)
- [CFF OpenType font](fonts/otf/Tekryno-Regular.otf)
- [Editable UFO source](sources/Tekryno-Regular.ufo)
- [Illustrator SVG artwork archive](sources/original-svg-archive/)
- [OpenType feature source](sources/features.fea)
- [Build helper](sources/build_from_ufo.py)
- [Five-page vector specimen](documentation/specimen/Tekryno-Type-Specimen.pdf)
- [Font license](OFL.txt)

The font is licensed under **SIL Open Font License 1.1, with no Reserved Font Name**. Copyright 2026 The Tekryno Project Authors (https://github.com/sgproductionindia/tekryno). The original designer is Shrawan Gaikwad. The entire family is open source, not just the Regular style.

## Build from editable sources

Install Python 3, then run these commands at the repository root:

```bash
python3 -m pip install -r requirements.txt
make build
make verify
```

`make build` compiles the editable UFO and `sources/features.fea` into `build/Tekryno-Regular.ttf`. `make verify` checks the result against the approved binary, including byte-for-byte identity. Dependency versions are pinned in `requirements.txt`; see [build instructions](documentation/BUILD-INSTRUCTIONS.md) and the [independent GitHub Actions verification](documentation/SOURCE-REPRODUCIBILITY.md).

## Google Fonts review

The official Fontspector Google Fonts profile was executed on the TTF in a correctly named `tekryno` directory on 2026-11-26:

**109 PASS, 0 FAIL, 10 WARN, 11 INFO, 83 SKIP.**

- [Full Fontspector report](documentation/FONTSPECTOR-REPORT.md)
- [Design-aware warning review](documentation/QA-REVIEW.md)
- [Official Latin Core coverage check](documentation/LATIN-CORE-COVERAGE.md)
- [Verified, reproducible source build](documentation/SOURCE-REPRODUCIBILITY.md)
- [Source provenance](documentation/PROVENANCE.md)
- [Current submission checklist](documentation/SUBMISSION-CHECKLIST.md)
- [Official Google Fonts proposal #11520](https://github.com/google/fonts/issues/11520)

**Source reproducibility: VERIFIED.** On 26 November 2026, GitHub Actions rebuilt the approved 20,496-byte TTF byte-for-byte from the editable UFO and OpenType feature source with pinned fontTools 4.63.0. Original outlines, metrics, kerning and mark positioning are unchanged.

Google Fonts publication is subject to independent design review, source and engineering validation, and the author's Contributor License Agreement. Technical checks passing does **not** imply acceptance.

Guide: https://googlefonts.github.io/gf-guide/onboarding.html
