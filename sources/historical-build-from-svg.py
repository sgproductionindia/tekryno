#!/usr/bin/env python3
"""Reproducible Optimus v9 test-build from the user's SVGs + v8 binaries.
Uses fontTools and Pillow; does not claim Google Fonts submission compliance.
"""
from __future__ import annotations
import copy, csv, json, re, unicodedata, hashlib
from pathlib import Path
from xml.etree import ElementTree as ET
from fontTools.ttLib import TTFont
from fontTools.agl import toUnicode
from fontTools.svgLib.path import parse_path
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.misc.transform import Transform
from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
from fontTools.pens.boundsPen import BoundsPen
from PIL import Image, ImageDraw, ImageFont, features

ROOT = Path(__file__).resolve().parent
LATIN = ROOT/'Latin_SVG_63'
OLD = ROOT/'Legacy_SVG_Sources'
BASE = ROOT/'Base_v8_Fonts'
UPM=1000; CAP=700; ORIGINAL_CAP_SOURCE=297.94
MARKS = {
    0x0300:('gravecomb','grave',True),
    0x0301:('acutecomb','acute',True),
    0x0302:('circumflexcomb','circumflex',True),
    0x0303:('tildecomb','tilde',True),
    0x0304:('macroncomb','macron',True),
    0x0306:('brevecomb','breve',True),
    0x0307:('dotaccentcomb','dotaccent',True),
    0x0308:('dieresiscomb','dieresis',True),
    0x030A:('ringcomb','ring',True),
    0x030B:('hungarumlautcomb','hungarumlaut',True),
    0x030C:('caroncomb','caron',True),
    0x0326:('commabelowcomb','comma',False),
    0x0327:('cedillacomb','cedilla',False),
    0x0328:('ogonekcomb','ogonek',False),
}
# Complete encoded character set, transcribed from Google's currently published
# GF_Latin_Core generated GLYPHSETS.md (other required glyphs are unencoded).
CORE_PARTS = [
 '''A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z ª º À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï Ð Ñ Ò Ó Ô Õ Ö Ø Ù Ú Û Ü Ý Þ ß à á â ã ä å æ ç è é ê ë ì í î ï ð ñ ò ó ô õ ö ø ù ú û ü ý þ ÿ Ā ā Ă ă Ą ą Ć ć Ċ ċ Č č Ď ď Đ đ Ē ē Ė ė Ę ę Ě ě Ğ ğ Ġ ġ Ģ ģ Ħ ħ Ī ī Į į İ ı Ķ ķ Ĺ ĺ Ļ ļ Ľ ľ Ł ł Ń ń Ņ ņ Ň ň Ő ő Œ œ Ŕ ŕ Ř ř Ś ś Ş ş Š š Ť ť Ū ū Ů ů Ű ű Ų ų Ŵ ŵ Ŷ ŷ Ÿ Ź ź Ż ż Ž ž Ș ș Ț ț ȷ Ẁ ẁ Ẃ ẃ Ẅ ẅ ẞ Ỳ ỳ''',
 '''̀ ́ ̂ ̃ ̄ ̆ ̇ ̈ ̊ ̋ ̌ ̦ ̧ ̨''',
 '''¨ ¯ ´ ¸ ˆ ˇ ˘ ˙ ˚ ˛ ˜ ˝''',
 '''0 1 2 3 4 5 6 7 8 9''',
 '''! " # ' ( ) * , - . / : ; ? [ \\ ] _ { } ¡ « · » ¿ – — ‘ ’ ‚ “ ” „ • … ‹ ›''',
 '''$ % & + < = > @ ^ | ~ ¢ £ ¥ § © ® ° ¶ × ÷ € ™ −'''
]
CORE = {ord(c) for part in CORE_PARTS for c in part.split()}
CORE.update({0x20,0xA0})
assert len(CORE)==318, f'Expected 318 encoded GF Latin Core characters, got {len(CORE)}'

EXPECTED = '''Atilde Aring Amacron Abreve Aogonek Ecircumflex Edieresis Emacron Edotaccent Eogonek Ecaron Igrave Iacute Icircumflex Idieresis Imacron Iogonek Idotaccent Ograve Oacute Ocircumflex Otilde Ohungarumlaut Ugrave Uacute Ucircumflex Umacron Uring Uhungarumlaut Uogonek Yacute Ycircumflex Ydieresis Ygrave Cacute Cdotaccent Ccaron Dcaron Gbreve Gdotaccent Gcedilla Kcedilla Lacute Lcedilla Lcaron Nacute Ncedilla Ncaron Racute Rcaron Sacute Scedilla Scaron Scommaaccent Tcaron Tcommaaccent Wcircumflex Wgrave Wacute Wdieresis Zacute Zdotaccent Zcaron'''.split()
assert len(EXPECTED)==63
actual={p.stem for p in LATIN.glob('*.svg')}
assert actual==set(EXPECTED), {'missing':sorted(set(EXPECTED)-actual),'unexpected':sorted(actual-set(EXPECTED))}

# SVG parser supports SVG path, polygon/polyline and rectangles as output by Illustrator.
def load_svg(p):
    root=ET.parse(p).getroot()
    dims=[float(v) for v in re.split(r'[\s,]+',root.attrib['viewBox'].strip())]
    assert len(dims)==4 and dims[2]>0 and dims[3]>0,(p,dims)
    return root,dims

def draw(root, pen):
    n=0
    for el in root.iter():
        kind=el.tag.rsplit('}',1)[-1]
        if kind=='path' and el.get('d'):
            parse_path(el.get('d'),pen);n+=1
        elif kind in ('polygon','polyline'):
            vals=[float(s) for s in re.findall(r'[-+]?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?',el.get('points',''))]
            pts=list(zip(vals[::2],vals[1::2]));assert len(pts)>=2
            pen.moveTo(pts[0]);[pen.lineTo(pt) for pt in pts[1:]]
            if kind=='polygon':pen.closePath()
            else:pen.endPath()
            n+=1
        elif kind=='rect':
            x=float(el.get('x','0'));y=float(el.get('y','0'))
            w=float(el.get('width'));h=float(el.get('height'))
            assert w>0 and h>0
            pts=((x,y),(x+w,y),(x+w,y+h),(x,y+h))
            pen.moveTo(pts[0]);[pen.lineTo(pt) for pt in pts[1:]];pen.closePath();n+=1
        elif kind in ('svg','g','defs','style'):
            assert 'transform' not in el.attrib,('Unexpected unhandled SVG transform',el.attrib)
        else:
            raise ValueError(f'Unexpected SVG element {kind} in {root.attrib}')
    assert n>0
    return n

# The 63 Illustrator glyphs all share the same native ~298-unit capital body;
# accent padding is above or below it. Align the capital body to 700 units,
# rather than shrinking the whole letter + accents into 700 units.
def setup_accented(name):
    root,(x,y,w,h)=load_svg(LATIN/(name+'.svg'))
    s=CAP/ORIGINAL_CAP_SOURCE
    below = name.endswith(('cedilla','ogonek','commaaccent'))
    body_bottom = y+ORIGINAL_CAP_SOURCE if below else y+h
    L=72;R=72
    # Original path source geometry is not modified; all paths share this transform.
    transform=Transform(s,0,0,-s,L-x*s,body_bottom*s)
    adv=round(L+w*s+R)
    return root,adv,transform

def setup_mark(name,src,above):
    root,(x,y,w,h)=load_svg(OLD/(src+'.svg'))
    # Reuse original mark design, scaled to practical mark size, with mark anchor at (0,0).
    target=135 if src not in ('ring','tilde','hungarumlaut','comma') else 155
    scale=min(target/h, 1.7)
    transform=Transform(scale,0,0,-scale,-(x+w/2)*scale,
                        (y+h)*scale if above else y*scale)
    return root,0,transform

def extract_pairs(font):
    result={}
    if 'GPOS' not in font:return result
    gp=font['GPOS'].table
    for feat in gp.FeatureList.FeatureRecord:
        if feat.FeatureTag!='kern':continue
        for ix in feat.Feature.LookupListIndex:
            lookup=gp.LookupList.Lookup[ix]
            for st in lookup.SubTable:
                if lookup.LookupType!=2 or st.Format!=1:
                    raise RuntimeError('Unexpected kerning lookup structure')
                for name,pairset in zip(st.Coverage.glyphs,st.PairSet):
                    for pr in pairset.PairValueRecord:
                        assert pr.Value1 is not None and pr.Value1.XAdvance is not None
                        assert pr.Value2 is None
                        result[(name,pr.SecondGlyph)] = pr.Value1.XAdvance
    return result

def apply_shapes(font,ext, specs):
    # specs: name -> (source root, advance, transform)
    if ext=='ttf':
        glyf=font['glyf']
        for name,(root,adv,tf) in specs.items():
            out=TTGlyphPen(None)
            pen=Cu2QuPen(out,max_err=0.65,reverse_direction=False)
            draw(root,TransformPen(pen,tf))
            glyph=out.glyph();glyf.glyphs[name]=glyph;glyph.recalcBounds(glyf)
            font['hmtx'].metrics[name]=(adv,glyph.xMin)
    else:
        cff=font['CFF '].cff;top=cff.topDictIndex[0]
        for name,(root,adv,tf) in specs.items():
            out=T2CharStringPen(adv,None)
            draw(root,TransformPen(out,tf))
            cs=out.getCharString(private=top.Private,globalSubrs=cff.GlobalSubrs)
            cs.private=top.Private;cs.globalSubrs=cff.GlobalSubrs
            top.CharStrings.charStrings[name]=len(top.CharStrings.charStringsIndex)
            top.CharStrings.charStringsIndex.append(cs)
            top.charset.append(name)
            # Use outline bound for true left sidebearing, not a default guess.
            bounds=BoundsPen(None)
            draw(root,TransformPen(bounds,tf))
            font['hmtx'].metrics[name]=(adv,round(bounds.bounds[0]) if bounds.bounds else 0)

def cmap_add(font,mapping):
    for t in font['cmap'].tables:
        if t.isUnicode():
            for code,name in mapping.items():
                old=t.cmap.get(code)
                assert old is None or old==name, ('mapping conflict',hex(code),old,name)
                t.cmap[code]=name

def fea_for_font(font,old_pairs,letter_names):
    above=' '.join(n for c,(n,_,is_above) in MARKS.items() if is_above)
    below=' '.join(n for c,(n,_,is_above) in MARKS.items() if not is_above)
    lines=['languagesystem DFLT dflt;','languagesystem latn dflt;','feature kern {']
    for (a,b),v in sorted(old_pairs.items()):
        if v!=0:lines.append(f'    pos {a} {b} {v};')
    lines+=['} kern;']
    for n in above.split():lines.append(f'markClass {n} <anchor 0 0> @TOP;')
    for n in below.split():lines.append(f'markClass {n} <anchor 0 0> @BOTTOM;')
    lines.append('feature mark {')
    for n in letter_names:
        advance=font['hmtx'].metrics[n][0]
        anchorX=round(advance/2)
        # Marks are centered on base glyphs; below marks attach below baseline.
        lines.append(f'    pos base {n} <anchor {anchorX} 810> mark @TOP;')
        lines.append(f'    pos base {n} <anchor {anchorX} -20> mark @BOTTOM;')
    lines+=['} mark;']
    return '\n'.join(lines)+'\n'

metrics=[]
base_for_check=TTFont(BASE/'Optimus-Refined-v8.ttf')
oldcmap=base_for_check.getBestCmap().copy()
oldorder=base_for_check.getGlyphOrder().copy()
oldmetrics={n:v for n,v in base_for_check['hmtx'].metrics.items()}
oldpairs=extract_pairs(base_for_check)
assert len(oldpairs)>=700, len(oldpairs)
TTF_old_outlines={n:base_for_check['glyf'][n].compile(base_for_check['glyf']) for n in oldorder}

specs={}
add_codes={}
for name in sorted(EXPECTED):
    specs[name]=setup_accented(name)
    cp=('Ț' if name=='Tcommaaccent' else toUnicode(name));assert len(cp)==1,(name,cp)
    add_codes[ord(cp)]=name
    lower=cp.lower()
    if len(lower)==1:
        add_codes[ord(lower)]=name
for cp,(name,svgsrc,above) in MARKS.items():
    specs[name]=setup_mark(name,svgsrc,above)
    add_codes[cp]=name
# Map whitespace & dotless letters to existing uppercase shaped glyphs.
add_codes[0x00A0]=oldcmap[0x20]
add_codes[0x0131]=oldcmap[ord('I')]
add_codes[0x0237]=oldcmap[ord('J')]
# There is no need for a new 'i̇' composite: use lowercase i + combining dot above.
assert all(cp not in oldcmap for cp in add_codes)
assert len(add_codes)==142, len(add_codes)

# Build the mark layout table alongside the existing kerning pairs.
source_fea=''
for ext in ('ttf','otf'):
    font=TTFont(BASE/('Optimus-Refined-v8.'+ext))
    oldextcmap=font.getBestCmap().copy()
    oldextmetrics={n:v for n,v in font['hmtx'].metrics.items()}
    oldextpairs=extract_pairs(font)
    new_order=font.getGlyphOrder()+list(specs.keys())
    font.setGlyphOrder(new_order)
    apply_shapes(font,ext,specs)
    cmap_add(font,add_codes)
    font['maxp'].numGlyphs=len(new_order)
    font['hhea'].numberOfHMetrics=len(new_order)
    # Accommodate user-drawn accents which extend above the 700-unit cap height.
    font['hhea'].ascent=1220
    font['hhea'].descent=-260
    font['OS/2'].sTypoAscender=1220
    font['OS/2'].sTypoDescender=-260
    font['OS/2'].sTypoLineGap=0
    font['OS/2'].usWinAscent=1220
    font['OS/2'].usWinDescent=260
    font['OS/2'].fsSelection |= 0x40  # REGULAR flag
    cmap=font.getBestCmap();font['OS/2'].usFirstCharIndex=min(cmap)
    font['OS/2'].usLastCharIndex=min(0xffff,max(cmap))
    letter_names=[n for n in new_order if n not in {m[0] for m in MARKS.values()} and any(unicodedata.category(chr(c)).startswith('L') for c,nm in cmap.items() if nm==n)]
    fea=fea_for_font(font,oldextpairs,letter_names)
    addOpenTypeFeaturesFromString(font,fea)
    source_fea=fea
    for record in font['name'].names:
        vals={1:'Optimus Refined v9',2:'Regular',3:'Optimus Refined v9 Regular;9.000',4:'Optimus Refined v9 Regular',5:'Version 9.000',6:'OptimusRefinedv9-Regular',16:'Optimus Refined v9',17:'Regular'}
        if record.nameID in vals:
            record.string=vals[record.nameID].encode('utf-16-be' if record.isUnicode() else 'latin1')
    font['head'].fontRevision=9.0
    outfile=ROOT/('Optimus-Refined-v9.'+ext)
    font.save(outfile)
    check=TTFont(outfile)
    cp=check.getBestCmap()
    assert len(check.getGlyphOrder())==len(oldorder)+len(specs)
    assert all(cp[c]==g for c,g in oldextcmap.items()),'Changed existing mappings'
    assert all(cp[c]==g for c,g in add_codes.items()),'Missing new Unicode mappings'
    assert all(check['hmtx'].metrics[n]==v for n,v in oldextmetrics.items()),'Changed existing metrics'
    assert extract_pairs(check)==oldextpairs, 'Existing kerning values changed'
    if ext=='ttf':
        assert all(check['glyf'][n].compile(check['glyf'])==bytesval for n,bytesval in TTF_old_outlines.items()), 'Existing outlines changed'
    missing=sorted(CORE-set(cp))
    assert not missing, 'Remaining Latin Core mappings: '+str(missing)
    assert 'mark' in [r.FeatureTag for r in check['GPOS'].table.FeatureList.FeatureRecord]
    print('PASS',ext,'glyphs',len(check.getGlyphOrder()),'mapped',len(cp),'Core coverage',len(CORE),'file bytes',outfile.stat().st_size)
    metrics.append({'file':outfile.name,'glyphs':len(check.getGlyphOrder()),'unicode_mappings':len(cp), 'gf_latin_core_mapped':len(CORE),'missing':len(missing),'kerning_pairs':len(oldextpairs),'mark_glyphs':14})

(ROOT/'font-features.fea').write_text(source_fea)
with (ROOT/'New-Unicode-Mappings.csv').open('w',newline='') as fh:
    out=csv.writer(fh);out.writerow(['character','Unicode','Unicode name','glyph_name','source_svg'])
    for cp,name in sorted(add_codes.items()):
        out.writerow([chr(cp),f'U+{cp:04X}',unicodedata.name(chr(cp),'N/A'),name,
                      name+'.svg' if name in EXPECTED else (MARKS[cp][1]+'.svg' if cp in MARKS else 'reuse from v8')])
(ROOT/'Coverage-Report.json').write_text(json.dumps({'version':'9.0 prototype', 'gf_latin_core_source':'https://github.com/googlefonts/glyphsets/blob/main/GLYPHSETS.md', 'gf_latin_core_encoded_characters':len(CORE),'new_unicode_mappings':len(add_codes),'new_svg_glyphs':63,'new_combining_mark_glyphs':14,'existing_base_glyphs':len(oldorder),'target_font_mappings':len(oldcmap)+len(add_codes),'files':metrics,'notes':['Unencoded GF Latin Core special glyphs and localized features are not validated.','No license or name clearance yet.','OpenType marks have generic positioning anchors; manual proofing needed.','Some preexisting accents in v8 have different proportion rules.']},indent=2))

# Text proof with the real font binary.
W,H=2000,1700
image=Image.new('RGB',(W,H),'#fcfcfc')
d=ImageDraw.Draw(image)
fontfile=str(ROOT/'Optimus-Refined-v9.ttf')
normal='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
head=ImageFont.truetype(normal,38);small=ImageFont.truetype(normal,25)
font=ImageFont.truetype(fontfile,104)
fontbig=ImageFont.truetype(fontfile,116)
d.rectangle((0,0,W,15),fill='#202c3e')
d.text((75,55),'OPTIMUS REFINED  /  VERSION 09',font=head,fill='#2f3b51')
d.text((75,120),'USER SVG LETTERFORMS  ·  63 NEW LATIN CHARACTERS  ·  UPPERCASE-STYLE LOWERCASE',font=small,fill='#666f7d')
sections=[
  ('PRIMARY LATIN DIACRITICS','À Á Â Ã Ä Å Ā Ă Ą'),
  ('EXTENDED EUROPEAN LETTERS','Ć Č Ď Ģ Ķ Ł Ň Ř Š Ť Ž'),
  ('MORE DIACRITICS','È É Ê Ë Ė Ě Í Î Ï Į'),
  ('W, Y AND O ACCENTS','Ẁ Ẃ Ẅ Ŵ Ŷ Ÿ Ỳ Õ Ő'),
  ('LOWERCASE INPUT  =  UPPERCASE STYLE','á ẽ š ü ź ẅ ỳ æ ø'),
  ('ACCENTED WORDS','AVATAR  FRÉQUENCE  ČESKÝ'),
  ('LEGACY CHARACTER TEST','HAMBURGEFONTSIV  ₹599  © ® ™'),
  ('DECOMPOSED INPUT','A\u0301 O\u0308 N\u0303 S\u0327'),
]
y=220
for caption,line in sections:
 d.text((75,y),caption,font=small,fill='#5e6877');y+=40
 use=font if len(line)<23 else ImageFont.truetype(fontfile,81 if len(line)<37 else 64)
 # fit width
 while d.textbbox((0,0),line,font=use)[2]>W-150 and use.size>40:
  use=ImageFont.truetype(fontfile,use.size-2)
 d.text((75,y),line,font=use,fill='#101827',stroke_width=0);y+=120
 d.line((75,y,W-75,y),fill='#dce1e7',width=2);y+=18
image.save(ROOT/'Optimus-v9-Latin-Specimen.png')
(ROOT/'README.md').write_text('''# Optimus Refined v9 — Latin Core Test Build

## Contents
- `Optimus-Refined-v9.ttf` and `.otf`: installable fonts
- `Latin_SVG_63/`: original 63 corrected SVGs provided by the designer, unchanged
- `Legacy_SVG_Sources/`: base v8 SVGs used for reusable combining accent artwork
- `Base_v8_Fonts/`: the exact v8 font binaries used as input
- `build_optimus_v9.py`: reproducible build with Python fontTools and Pillow
- `font-features.fea`: generated OpenType pair kerning and mark positioning rules
- `New-Unicode-Mappings.csv` and `Coverage-Report.json`: technical audit
- `Optimus-v9-Latin-Specimen.png`: specimen rendered from the produced TTF

## Key changes
- Added the 63 corrected uppercase-style accented Latin SVG designs and matching lowercase keyboard mappings.
- Added 14 combining marks using SVG source marks, plus nonbreaking space and dotless i/j mapping.
- All 318 encoded character codepoints in the current official GF Latin Core specification are mapped.
- Original v8 glyph outlines, advances, existing Unicode mappings and numeric kerning values are preserved.
- Added basic OpenType mark-to-base GPOS anchors; manual placement and script-language behavior proofing remains necessary.

## Important limitations
**This is a development build, NOT ready for Google Fonts publication.**
- Glyph presence is not a complete quality check: localized Catalan glyphs, required unencoded alternates, marks, character sequences, outline overlaps, hinting, QA reports and language-shaping checks need further work.
- Positioning of the new accents has not been optically approved across all 63 characters.
- The name *Optimus* may conflict with existing typefaces. Final naming, ownership, SIL OFL licensing and source-project preparation are incomplete.
- Preexisting accented glyphs in the v8 base were not changed, so some cap-height inconsistencies may remain.

## Test on macOS
Install either TTF or OTF through Font Book (not both). Set tracking to 0 and kerning to Metrics. If previous copies are installed, deactivate them in Font Book first.
''')
print('ALL CHECKS OK')
