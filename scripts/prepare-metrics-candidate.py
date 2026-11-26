#!/usr/bin/env python3
"""Prepare an isolated Google Fonts vertical-metrics compliance candidate.

Does not modify the 1.003 public release binaries. Proposes 1.004 for review.
"""
from pathlib import Path
from fontTools.ttLib import TTFont
import json, hashlib

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "candidate"
OUTPUT.mkdir(exist_ok=True)
report = {}

for ext in ("ttf", "otf"):
    published = ROOT / "fonts" / ext / ("Tekryno-Regular." + ext)
    source = TTFont(published, recalcTimestamp=False)
    font = TTFont(published, recalcTimestamp=False)

    assert len(font.getGlyphOrder()) == 218
    assert len(font.getBestCmap()) == 327
    assert font["head"].unitsPerEm == 1000
    y_top, y_bottom = font["head"].yMax, font["head"].yMin
    assert y_top == 977 and y_bottom == -173

    # Typo and hhea metrics: 130% of UPM; capitals centred in line.
    font["OS/2"].sTypoAscender = 1000
    font["OS/2"].sTypoDescender = -300
    font["OS/2"].sTypoLineGap = 0
    font["hhea"].ascent = 1000
    font["hhea"].descent = -300
    font["hhea"].lineGap = 0

    # Windows bounds track the font's actual highest/lowest outlines.
    font["OS/2"].usWinAscent = y_top
    font["OS/2"].usWinDescent = -y_bottom
    font["OS/2"].fsSelection |= (1 << 7)  # USE_TYPO_METRICS
    font["head"].fontRevision = 1.004
    font["head"].modified += 1

    # This release is unhinted. The GF static guide recommends 0x000A.
    if ext == "ttf":
        assert "fpgm" not in font and "prep" not in font
        font["gasp"].gaspRange = {65535: 10}

    for name in font["name"].names:
        if name.nameID == 5:
            value = "Version 1.004"
        elif name.nameID == 3:
            value = name.toUnicode().replace("1.003", "1.004")
        else:
            continue
        name.string = value.encode("utf_16_be" if name.isUnicode() else "mac_roman")

    if ext == "otf":
        top = font["CFF "].cff.topDictIndex[0]
        if hasattr(top, "version"):
            top.version = "1.004"

    target = OUTPUT / ext / ("Tekryno-Regular." + ext)
    target.parent.mkdir(parents=True, exist_ok=True)
    font.save(target)
    produced = TTFont(target)

    protected = ("GPOS", "GDEF", "hmtx", "cmap", "glyf" if ext == "ttf" else "maxp")
    matches = {t: source.getTableData(t) == produced.getTableData(t) for t in protected}
    assert all(matches.values()), ("Design or shaping table changed unexpectedly", matches)
    assert produced["OS/2"].usWinAscent == produced["head"].yMax
    assert produced["OS/2"].usWinDescent == -produced["head"].yMin
    assert produced["OS/2"].sTypoAscender == produced["hhea"].ascent
    assert produced["OS/2"].sTypoDescender == produced["hhea"].descent
    assert produced["OS/2"].sTypoLineGap == produced["hhea"].lineGap == 0
    assert produced["OS/2"].fsType == 0
    assert len(produced.getGlyphOrder()) == 218
    assert len(produced.getBestCmap()) == 327
    assert produced["name"].getDebugName(5) == "Version 1.004"

    report[ext] = {
        "status": "PASS",
        "version": "1.004 CANDIDATE — NOT RELEASED",
        "source_sha256": hashlib.sha256(published.read_bytes()).hexdigest(),
        "candidate_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
        "protected_tables_equal": matches,
        "vertical_metrics": {
            "sTypoAscender": produced["OS/2"].sTypoAscender,
            "sTypoDescender": produced["OS/2"].sTypoDescender,
            "usWinAscent": produced["OS/2"].usWinAscent,
            "usWinDescent": produced["OS/2"].usWinDescent,
            "hheaAscent": produced["hhea"].ascent,
            "hheaDescent": produced["hhea"].descent,
        },
    }

(OUTPUT / "METRICS-CANDIDATE-QA.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
