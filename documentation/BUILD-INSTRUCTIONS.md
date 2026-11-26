# Tekryno — Development build

The editable UFO master is intended to be kept in `sources/Tekryno-Regular.ufo/`; the OpenType feature definitions are in `sources/features.fea`.

Install Python and run:

```bash
python3 -m pip install -r requirements.txt
python3 sources/build_from_ufo.py
```

A development TTF will be created at `build/Tekryno-Regular.ttf`.

**Verified:** With the pinned `fonttools==4.63.0` dependency, this source build reproduces `fonts/ttf/Tekryno-Regular.ttf` **byte-for-byte**. The GitHub workflow `.github/workflows/verify-source-build.yml` runs this test independently. See `documentation/SOURCE-REPRODUCIBILITY.md` and `documentation/PROVENANCE.md`.

Do not change the historical source metadata or input glyph coordinates when building the published 1.003 release; changes should be made in a versioned upgrade, with QA rerun before distribution.
