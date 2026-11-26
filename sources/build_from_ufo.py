#!/usr/bin/env python3
"""Build Tekryno TrueType from the editable UFO master.

Python package requirements: fonttools, ufoLib2 is not required.
Note: run final visual and OpenType-layout QA before replacing a release font.
"""
from pathlib import Path
from types import SimpleNamespace
from fontTools.fontBuilder import FontBuilder
from fontTools.ufoLib import UFOReader
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.pointPen import PointToSegmentPen
from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
from fontTools.ttLib import newTable
from fontTools.otlLib.builder import buildStatTable

ROOT = Path(__file__).resolve().parent
ufo = UFOReader(str(ROOT / "Tekryno-Regular.ufo"))
source = ufo.getGlyphSet()
info = SimpleNamespace()
ufo.readInfo(info)
order = ufo.readLib()["public.glyphOrder"]
cmap, glyphs, metrics = {}, {}, {}

for name in order:
    obj = SimpleNamespace()
    pen = TTGlyphPen(source)
    source.readGlyph(name, obj, PointToSegmentPen(pen))
    glyphs[name] = pen.glyph()
    boundspen = BoundsPen(source)
    source.readGlyph(name, SimpleNamespace(), PointToSegmentPen(boundspen))
    metrics[name] = (getattr(obj, "width", 0),
                     int(round(boundspen.bounds[0])) if boundspen.bounds else 0)
    for cp in getattr(obj, "unicodes", []):
        cmap[cp] = name

fb = FontBuilder(info.unitsPerEm, isTTF=True)
fb.setupGlyphOrder(order)
fb.setupCharacterMap(cmap)
fb.setupGlyf(glyphs)
fb.setupHorizontalMetrics(metrics)
fb.setupHorizontalHeader(ascent=info.ascender, descent=info.descender, lineGap=0)
fb.setupNameTable({
    "familyName": "Tekryno",
    "styleName": "Regular",
    "uniqueFontIdentifier": "Tekryno Regular;1.003;Shrawan Gaikwad",
    "fullName": "Tekryno Regular",
    "psName": "Tekryno-Regular",
    "version": "Version 1.003",
    "copyright": "Copyright 2026 The Tekryno Project Authors (https://github.com/sgproductionindia/tekryno)",
    "designer": "Shrawan Gaikwad",
})
fb.setupOS2(
    version=4, sTypoAscender=info.ascender, sTypoDescender=info.descender,
    sTypoLineGap=0, usWinAscent=1220, usWinDescent=260,
    usWeightClass=400, usWidthClass=5, fsSelection=(1 << 6) | (1 << 7) | (1 << 8),
    ulCodePageRange1=1, sxHeight=info.xHeight, sCapHeight=info.capHeight,
)
fb.setupPost(italicAngle=0, underlinePosition=-75, underlineThickness=50)
fb.setupMaxp()
font = fb.font
addOpenTypeFeaturesFromString(font, (ROOT / "features.fea").read_text())
gasp = newTable("gasp")
gasp.gaspRange = {65535: 15}
font["gasp"] = gasp
meta = newTable("meta")
meta.data = {"dlng": "Latn", "slng": "Latn"}
font["meta"] = meta
buildStatTable(
    font, [dict(tag="ital", name="Italic",
                values=[dict(value=0, name="Roman", flags=2)])]
)
name = font["name"]
name.setName(
    "This Font Software is licensed under the SIL Open Font License, Version 1.1. "
    "This license is available with a FAQ at: https://openfontlicense.org",
    13, 3, 1, 0x409
)
name.setName("https://openfontlicense.org", 14, 3, 1, 0x409)
font["head"].fontRevision = 1.003
output = ROOT.parent / "build" / "Tekryno-Regular.ttf"
output.parent.mkdir(exist_ok=True)
font.save(output)
print(f"Built {output}")
