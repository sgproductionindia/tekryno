# Tekryno — Google Fonts preparation checklist

## Author approval and licensing

- [x] Author has affirmed ownership/rights and authorized publication of the font, sources, and assets.
- [x] Public SIL Open Font License 1.1 (no Reserved Font Names), published as `OFL.txt`.
- [x] Font copyright and project-author names point at the public GitHub URL.
- [ ] Complete definitive name and trademark similarity review; basic web lookups are preliminary.
- [ ] Original designer completes Google Contributor License Agreement.

## Source and release

- [x] Publish canonical `fonts/Tekryno-Regular.ttf` and desktop OTF.
- [x] Publish editable UFO, original Illustrator SVG artwork and documented build helper.
- [ ] Reconcile dotted-circle outline and GPOS differences in UFO rebuild.
- [x] Publish five-page specimen and descriptive documentation.

## Google Fonts technical QA

- [x] Verify canonical filename and internal family name (`Tekryno`).
- [x] Check encoded GF Latin Core coverage (**319/319**).
- [x] Execute current Fontspector Google Fonts profile (**0 FAIL**, 10 WARN).
- [ ] Complete manual review of all 10 Fontspector WARNs.
- [ ] Complete small-size/readability, kerning and diacritic composition proofing.
- [x] Confirm OFL copyright strings and URL in binary font metadata.

## Official submission

- [ ] File Add Font issue with upstream repository and specimen when readiness tasks are complete.
- [ ] Respond to design and engineering feedback and assist with packaging/pull request if accepted.
- [ ] Obtain Google Fonts acceptance and publication (curated and not guaranteed).

Official requirements: https://googlefonts.github.io/gf-guide/onboarding.html

**Status:** Public source release candidate, not yet submitted to Google Fonts.
