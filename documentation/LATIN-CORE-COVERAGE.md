# Tekryno — Google Fonts Latin Core coverage

**Result: PASS for encoded Unicode coverage**

Validated against the official Google Fonts `GF_Latin_Core.nam` reference (319 distinct required Unicode code points):
https://github.com/googlefonts/glyphsets/blob/main/data/results/nam/GF_Latin_Core.nam

- Required encoded code points: **319**
- Tekryno-Regular.ttf encoded code points: **327**
- Required encoded code points missing from Tekryno: **0**
- Mappings are intentionally uppercase-styled for many lowercase letters as a display-design choice

Test method: compare the font's `cmap` mappings with the Unicode set in the official `.nam` definition.

**Limitations:** This is a code point availability test, **not** a substitute for Fontspector's complete Google Fonts profile, linguistic shaping validation, glyph-level quality, diacritic mark placement or title-case readability review.
