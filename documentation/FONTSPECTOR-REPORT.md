## FontSpector report

fontspector version: 1.9.0






## Check results




<details><summary>[1] /home/runner/work/_temp/tekryno</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. (googlefonts/metadata/unreachable_subsetting)</summary>
    <div>


> This check ensures that all encoded glyphs in the font are covered by a subset declared in the METADATA.pb. Google Fonts splits the font into a set of subset fonts based on the contents of the `subsets` field and the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions will not be served in the subsetted fonts, and so will be unreachable to the end user.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4097 and https://github.com/fonttools/fontbakery/pull/4273]





- ⚠️ **WARN** /home/runner/work/_temp/tekryno/Tekryno-Regular.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: canadian-aboriginal, yi
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: canadian-aboriginal, yi
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, math, coptic
* U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
* U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, coptic, tai-le, math, canadian-aboriginal, duployan, hebrew, malayalam, syriac, tifinagh, todhri
* U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: tai-le, cherokee
... and 6 others

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  

</div>
</details>


</div>
</details>


<details><summary>[6] /home/runner/work/_temp/tekryno/Tekryno-Regular.ttf</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron (alt_caron)</summary>
    <div>


> Lcaron, dcaron, lcaron, tcaron should NOT be composed with quoteright or quotesingle or comma or caron(comb). It should be composed with a distinctive glyph which doesn't look like an apostrophe.
> 
> Source: https://ilovetypography.com/2009/01/24/on-diacritics/ http://diacritics.typo.cz/index.php?id=5 https://www.typotheque.com/articles/lcaron




Original proposal: [https://github.com/fonttools/fontbakery/issues/3308]





- ⚠️ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** Dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** Tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. (contour_count)</summary>
    <div>


> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be constructured in a handful of ways. This means a glyph's contour count will only differ slightly amongst different fonts, e.g a 'g' could either be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs to a display family.
> 
> This check currently does not cover variable fonts because there's plenty of alternative ways of constructing glyphs with multiple outlines for each feature in a VarFont. The expected contour count data for this check is currently optimized for the typical construction of glyphs in static fonts.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are
     inferred from the typical amounts of contours observed in a
     large collection of reference font families. The divergences
     listed below may simply indicate a significantly different
     design on some of your glyphs. On the other hand, some of these
     may flag actual bugs in the font such as glyphs mapped to an
     incorrect codepoint. Please consider reviewing the design and
     codepoint assignment of these to make sure they are correct.


    The following glyphs do not have the recommended number of contours:
* two (U+0032): found 3, expected one of: [1, 2, 5]
* five (U+0035): found 3, expected one of: [1, 2, 5]
* section (U+00A7): found 3, expected one of: [2, 4, 6] [code: contour-count]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>


> This check uses a heuristic to determine which GF glyphsets a font supports. Then it checks the font for correct shaping behaviour for all languages in those glyphsets.




Original proposal: [https://github.com/googlefonts/fontbakery/issues/4147]





- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages                    |
|-------------------------------------------------------------------|------------------------------|
| Auxiliary orthography codepoints:                                 | * cs_Latn (Czech)            |
|   The following auxiliary characters are missing from the font: Ĕ | * cy_Latn (Welsh)            |
|   The following auxiliary characters are missing from the font: Ĭ | * es_Latn (Spanish)          |
|   The following auxiliary characters are missing from the font: Ŏ | * hu_Latn (Hungarian)        |
|   The following auxiliary characters are missing from the font: Ō | * pt_Latn (Portuguese)       |
|   The following auxiliary characters are missing from the font: Ŭ | * sk_Latn (Slovak)           |
|   The following auxiliary characters are missing from the font: ĕ | * tr_Latn (Turkish)          |
|   The following auxiliary characters are missing from the font: ĭ |                              |
|   The following auxiliary characters are missing from the font: ŏ |                              |
|   The following auxiliary characters are missing from the font: ō |                              |
|   The following auxiliary characters are missing from the font: ŭ |                              |
| Auxiliary orthography codepoints:                                 | * lv_Latn (Latvian)          |
|   The following auxiliary characters are missing from the font: Ō |                              |
|   The following auxiliary characters are missing from the font: Ŗ |                              |
|   The following auxiliary characters are missing from the font: ō |                              |
|   The following auxiliary characters are missing from the font: ŗ |                              |
| Auxiliary orthography codepoints:                                 | * lt_Latn (Lithuanian)       |
|   The following auxiliary characters are missing from the font: Ẽ |                              |
|   The following auxiliary characters are missing from the font: Ĩ |                              |
|   The following auxiliary characters are missing from the font: Ũ |                              |
|   The following auxiliary characters are missing from the font: ẽ |                              |
|   The following auxiliary characters are missing from the font: ĩ |                              |
|   The following auxiliary characters are missing from the font: ũ |                              |
| Auxiliary orthography codepoints:                                 | * de_Latn (German)           |
|   The following auxiliary characters are missing from the font: Ĕ |                              |
|   The following auxiliary characters are missing from the font: Ĭ |                              |
|   The following auxiliary characters are missing from the font: Ŏ |                              |
|   The following auxiliary characters are missing from the font: Ō |                              |
|   The following auxiliary characters are missing from the font: Ŭ |                              |
|   The following auxiliary characters are missing from the font: ĕ |                              |
|   The following auxiliary characters are missing from the font: ĭ |                              |
|   The following auxiliary characters are missing from the font: ŏ |                              |
|   The following auxiliary characters are missing from the font: ō |                              |
|   The following auxiliary characters are missing from the font: ſ |                              |
|   The following auxiliary characters are missing from the font: ŭ |                              |
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)           |
|   The following auxiliary characters are missing from the font: Ǿ |                              |
|   The following auxiliary characters are missing from the font: ǿ |                              |
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ǧ |                              |
|   The following auxiliary characters are missing from the font: Ǥ |                              |
|   The following auxiliary characters are missing from the font: Ȟ |                              |
|   The following auxiliary characters are missing from the font: Ǩ |                              |
|   The following auxiliary characters are missing from the font: Ŋ |                              |
|   The following auxiliary characters are missing from the font: Ŝ |                              |
|   The following auxiliary characters are missing from the font: Ţ |                              |
|   The following auxiliary characters are missing from the font: Ŧ |                              |
|   The following auxiliary characters are missing from the font: Ʒ |                              |
|   The following auxiliary characters are missing from the font: Ǯ |                              |
|   The following auxiliary characters are missing from the font: ǧ |                              |
|   The following auxiliary characters are missing from the font: ǥ |                              |
|   The following auxiliary characters are missing from the font: ȟ |                              |
|   The following auxiliary characters are missing from the font: ǩ |                              |
|   The following auxiliary characters are missing from the font: ŋ |                              |
|   The following auxiliary characters are missing from the font: ŝ |                              |
|   The following auxiliary characters are missing from the font: ţ |                              |
|   The following auxiliary characters are missing from the font: ŧ |                              |
|   The following auxiliary characters are missing from the font: ʒ |                              |
|   The following auxiliary characters are missing from the font: ǯ |                              |
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ǎ |                              |
|   The following auxiliary characters are missing from the font: Ŋ |                              |
|   The following auxiliary characters are missing from the font: Ŧ |                              |
|   The following auxiliary characters are missing from the font: ǎ |                              |
|   The following auxiliary characters are missing from the font: ŋ |                              |
|   The following auxiliary characters are missing from the font: ŧ |                              |
| Auxiliary orthography codepoints:                                 | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: Ĕ |                              |
|   The following auxiliary characters are missing from the font: Ĭ |                              |
|   The following auxiliary characters are missing from the font: Ŏ |                              |
|   The following auxiliary characters are missing from the font: Ō |                              |
|   The following auxiliary characters are missing from the font: Ŭ |                              |
|   The following auxiliary characters are missing from the font: ĕ |                              |
|   The following auxiliary characters are missing from the font: ĭ |                              |
|   The following auxiliary characters are missing from the font: ŏ |                              |
|   The following auxiliary characters are missing from the font: ō |                              |
|   The following auxiliary characters are missing from the font: ŭ |                              |
|   The following auxiliary characters are missing from the font: ʻ |                              |
| Auxiliary orthography codepoints:                                 | * nl_Latn (Dutch)            |
|   The following auxiliary characters are missing from the font: Ĳ |                              |
|   The following auxiliary characters are missing from the font: ĳ |                              |
| Auxiliary orthography codepoints:                                 | * ro_Latn (Romanian)         |
|   The following auxiliary characters are missing from the font: Ţ |                              |
|   The following auxiliary characters are missing from the font: ţ |                              |
| Auxiliary orthography codepoints:                                 | * fr_Latn (French)           |
|   The following auxiliary characters are missing from the font: Ǔ |                              |
|   The following auxiliary characters are missing from the font: ſ |                              |
|   The following auxiliary characters are missing from the font: ǔ |                              |
| Auxiliary orthography codepoints:                                 | * ca_Latn (Catalan)          |
|   The following auxiliary characters are missing from the font: Ĕ |                              |
|   The following auxiliary characters are missing from the font: Ĭ |                              |
|   The following auxiliary characters are missing from the font: Ŀ |                              |
|   The following auxiliary characters are missing from the font: Ŏ |                              |
|   The following auxiliary characters are missing from the font: Ō |                              |
|   The following auxiliary characters are missing from the font: Ŭ |                              |
|   The following auxiliary characters are missing from the font: ĕ |                              |
|   The following auxiliary characters are missing from the font: ĭ |                              |
|   The following auxiliary characters are missing from the font: ŀ |                              |
|   The following auxiliary characters are missing from the font: ŏ |                              |
|   The following auxiliary characters are missing from the font: ō |                              |
|   The following auxiliary characters are missing from the font: ŭ |                              | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? (outline_alignment_miss)</summary>
    <div>


> This check heuristically looks for on-curve points which are close to, but do not sit on, significant boundary coordinates. For example, a point which has a Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the baseline, here we also check for points near the x-height (but only for lowercase Latin letters), cap-height, ascender and descender Y coordinates.
> 
> Not all such misaligned curve points are a mistake, and sometimes the design may call for points in locations near the boundaries. As this check is liable to generate significant numbers of false positives, it will pass if there are more than 100 reported misalignments.




Original proposal: [https://github.com/fonttools/fontbakery/pull/3088]





- ⚠️ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

* - asterisk (U+002A): X=174,Y=698 (should be at cap-height 700?)
* - asterisk (U+002A): X=372,Y=698 (should be at cap-height 700?)
* - registered (U+00AE): X=425,Y=699 (should be at cap-height 700?)
* - registered (U+00AE): X=425,Y=1 (should be at baseline 0?)
* - registered (U+00AE): X=425,Y=699 (should be at cap-height 700?) [code: found-misalignments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Are any segments inordinately short? (outline_short_segments)</summary>
    <div>


> This check looks for outline segments which seem particularly short (less than 0.6% of the overall path length).
> 
> This check is not run for variable fonts, as they may legitimately have short segments. As this check is liable to generate significant numbers of false positives, it will pass if there are more than 100 reported short segments.




Original proposal: [https://github.com/fonttools/fontbakery/pull/3088]





- ⚠️ **WARN** The following glyphs have short segments:

* Q (U+0071) contains a short segment Quad(QuadBez { p0: (740.0, 138.0), p1: (740.0, 138.0), p2: (750.5, 127.5) }) (length: 14.85, total outline: 2886.64)
* Q (U+0071) contains a short segment Quad(QuadBez { p0: (799.5, 79.5), p1: (810.0, 69.0), p2: (810.0, 69.0) }) (length: 14.85, total outline: 2886.64)
* five (U+0035) contains a short segment Line(Line { p0: (96.0, 135.0), p1: (99.0, 138.0) }) (length: 4.24, total outline: 2118.57)
* eight (U+0038) contains a short segment Quad(QuadBez { p0: (755.0, 400.0), p1: (755.0, 400.0), p2: (765.5, 389.5) }) (length: 14.85, total outline: 2696.97)
* eight (U+0038) contains a short segment Quad(QuadBez { p0: (813.5, 341.5), p1: (824.0, 331.0), p2: (824.0, 331.0) }) (length: 14.85, total outline: 2696.97)
* ampersand (U+0026) contains a short segment Quad(QuadBez { p0: (72.0, 281.0), p1: (72.0, 281.0), p2: (79.0, 288.0) }) (length: 9.90, total outline: 3102.69)
* ampersand (U+0026) contains a short segment Quad(QuadBez { p0: (134.0, 343.0), p1: (141.0, 350.0), p2: (141.0, 350.0) }) (length: 9.90, total outline: 3102.69)
* ampersand (U+0026) contains a short segment Quad(QuadBez { p0: (210.0, 562.0), p1: (210.0, 562.0), p2: (210.0, 547.5) }) (length: 14.50, total outline: 3102.69)
* ampersand (U+0026) contains a short segment Quad(QuadBez { p0: (210.0, 433.5), p1: (210.0, 419.0), p2: (210.0, 419.0) }) (length: 14.50, total outline: 3102.69)
... and 13 others [code: found-short-segments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>


> Microsoft keeps a list of font vendors and their respective contact info. This list is updated regularly and is indexed by a 4-char "Vendor ID" which is stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some applications may display the type designer / type foundry contact info on some dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in that list or if it has some of the default values used by the most common font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs. If you registered recently, you're safe to ignore warnings emitted by this check, since your ID will soon be included in one of our upcoming releases.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3943, https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** OS/2 VendorID value 'SGPR' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>


</div>
</details>






### Summary

| ⚠️ WARN | ℹ️ INFO | ✅ PASS | ⏩ SKIP | 
| ---|---|---|---|
| 10 | 11 | 109 | 83 | 
| 5% | 5% | 51% | 39% | 





---
QA command exit status: **0** (0 means no unsuppressed failures).
