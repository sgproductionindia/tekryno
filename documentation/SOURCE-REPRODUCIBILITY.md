# TEKRYNO source reproducibility — verified

**Result: PASS.** The checked-in editable UFO and OpenType feature source rebuild the approved TrueType binary **byte-for-byte** with pinned `fonttools==4.63.0`.

- Release: `fonts/ttf/Tekryno-Regular.ttf`
- Build command: `bash sources/build.sh`
- Built output: `build/Tekryno-Regular.ttf`
- SHA-256 (both): `2d642f7844fbc8398caa729801782e2f6c2b9288c47cb3e3b1db8fcec2bffd37`
- Glyph count: 218; Unicode mappings: 327
- `OS/2.fsType`: 0 (installable embedding)
- Unchanged design: all glyph outlines, widths, kerning and mark positioning match the approved font.

This verifies TrueType source reproduction, not Google Fonts design acceptance, name clearance or completeness of manual warning reviews.
