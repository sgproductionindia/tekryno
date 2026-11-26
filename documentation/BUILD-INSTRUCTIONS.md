# Tekryno — Development build

The editable UFO master is intended to be kept in `sources/Tekryno-Regular.ufo/`; the OpenType feature definitions are in `sources/features.fea`.

Install Python and run:

```bash
python3 -m pip install -r requirements.txt
python3 sources/build_from_ufo.py
```

A development TTF will be created at `build/Tekryno-Regular.ttf`.

**Important:** Before distribution or Google Fonts submission, compare the built font to the approved release master (glyphs, widths, Unicode mapping, GPOS pair adjustments and mark positioning, and the corrected accents). The current script is a development helper and is not yet certified to reproduce the final release identically. Refer to `documentation/PROVENANCE.md`.
