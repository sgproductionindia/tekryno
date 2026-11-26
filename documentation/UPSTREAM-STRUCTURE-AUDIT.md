# Tekryno upstream repository structure audit

Checked: 2026-11-26
Reference: https://googlefonts.github.io/gf-guide/upstream.html

Google Fonts explicitly states that the scripts and automated actions from the **Google Fonts Project Template are optional**, while the core source/layout requirements apply. Tekryno uses a custom deterministic build workflow instead of copying the whole template.

## Essential items verified in the public repository

- [x] `AUTHORS.txt` with designer and contact
- [x] `CONTRIBUTORS.txt`
- [x] `OFL.txt` including family copyright line, no Reserved Font Name
- [x] `README.md` with font description, specimen preview and reproducible build instructions
- [x] `documentation/` with specimen PDF and PNG/JPG preview artwork
- [x] `fonts/ttf/Tekryno-Regular.ttf`
- [x] `fonts/otf/Tekryno-Regular.otf`
- [x] `sources/Tekryno-Regular.ufo/` (editable glyph source)
- [x] `sources/features.fea` (OpenType layout source)
- [x] `sources/build.sh` (one-command source compiler)
- [x] `sources/config.yaml` (upstream build configuration for potential alternative gftools builder; custom build is authoritative)
- [x] `requirements.txt` (pinned fontTools version), `requirements.in` and `.gitignore`
- [x] `Makefile` with `make build` and `make verify`
- [x] Independently passing GitHub Actions source rebuild using `make verify`, matching the release TTF byte-for-byte.

## Notes

This audit concerns the *upstream repository organization only*. It does not assert that all font-production and type-design requirements are satisfied. Google Fonts acceptance and the `X Form not completed` label on submission issue #11520 must be determined by Google. Full contributing compliance remains unchecked until the remaining design/QA issues have been assessed.

Evidence:
- https://github.com/sgproductionindia/tekryno/actions/runs/45792833754
- https://github.com/sgproductionindia/tekryno/blob/main/documentation/SOURCE-REPRODUCIBILITY.md
- https://github.com/sgproductionindia/tekryno/blob/main/documentation/FONTSPECTOR-REPORT.md
