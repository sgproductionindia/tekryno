# Tekryno — Source provenance

Tekryno was designed as individual Illustrator SVG letterforms. The final editable UFO was exported from the author's approved Tekryno TTF release candidate so its outlines include subsequent geometric, accent-alignment, and QA updates.

The historical SVG build script predates the later repairs, and should be retained for provenance rather than treated as a drop-in reproducible build for the release binaries.

**Resolved 2026-11-26:** The source's `uni25CC` dotted-circle outlines were originally shifted left by 163 units relative to the approved TTF, and two separate mark-attachment lookups differed from the original single lookup. Those source-only discrepancies were repaired. The source builder now also preserves the release font's table metadata and open, installable embedding permission (`OS/2.fsType=0`).

An independent GitHub Actions run proved that the corrected UFO, `features.fea` and pinned fontTools 4.63.0 reproduce `fonts/ttf/Tekryno-Regular.ttf` **byte-for-byte**. SHA-256: `2d642f7844fbc8398caa729801782e2f6c2b9288c47cb3e3b1db8fcec2bffd37`. See [source build report](SOURCE-REPRODUCIBILITY.md). No released glyph outlines were changed.

Both TrueType and CFF OpenType were produced for desktop use. Google Fonts requires the TTF and editable source.
