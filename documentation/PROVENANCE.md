# Tekryno — Source provenance

Tekryno was designed as individual Illustrator SVG letterforms. The final editable UFO was exported from the author's approved Tekryno TTF release candidate so its outlines include subsequent geometric, accent-alignment, and QA updates.

The historical SVG build script predates the later repairs, and should be retained for provenance rather than treated as a drop-in reproducible build for the release binaries.

Local verification of the UFO build against the approved TrueType candidate found matching glyph count (218), Unicode mappings (327), advance widths, and all but one compiled TrueType glyph outline (`uni25CC`, dotted circle). GPOS table compiled bytes also differed. These differences must be inspected before the upstream build is described as fully reproducible or submitted as a final Google Fonts release.

Both TrueType and CFF OpenType were produced for desktop use. Google Fonts requires the TTF and editable source.
