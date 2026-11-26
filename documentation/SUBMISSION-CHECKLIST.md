# Tekryno — Google Fonts preparation checklist

## Author approval and licensing

- [x] Author has affirmed ownership/rights and authorized publication of the font, sources, and assets.
- [x] Public SIL Open Font License 1.1 (no Reserved Font Names), published as `OFL.txt`.
- [x] Font copyright and project-author names point at the public GitHub URL.
- [x] Fontdata Typeface Name Check returned no exact font named **Tekryno** (user screenshot, 2026-11-26).
- [ ] Complete broader trademark and similar-name clearance if desired; Fontdata results do not establish legal trademark rights.
- [x] Original designer reported submitting the Google Contributor License Agreement on 2026-11-26 (Google-side processing not independently verified).

## Source and release

- [x] Publish canonical `fonts/ttf/Tekryno-Regular.ttf` and desktop OTF.
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

- [x] File Add Font issue with upstream repository and specimen: [google/fonts#11520](https://github.com/google/fonts/issues/11520) (created 2026-11-26, open).
- [ ] Respond to design and engineering feedback and assist with packaging/pull request if accepted.
- [ ] Obtain Google Fonts acceptance and publication (curated and not guaranteed).

Official requirements: https://googlefonts.github.io/gf-guide/onboarding.html

**Status:** Public OFL source release candidate; [Google Fonts proposal #11520](https://github.com/google/fonts/issues/11520) submitted and open. Not yet accepted or published.
