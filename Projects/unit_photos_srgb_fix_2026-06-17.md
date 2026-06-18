---
type: project
created: 2026-06-17
tags: [str, photos, airbnb, color-profile, cityside]
units: [558584, 558585]
---

# Unit Photos — Adobe RGB → sRGB Re-Export (2026-06-17)

## Problem
Sam asked why the unit listing photos looked soft/off after upload. Investigated the
photo folder at `C:\Users\samth\Downloads\sam_unit_photos\organized` (2 units:
`558584_unit-A`, `558585_unit-B`, sorted into category subfolders).

## Diagnosis (reality-checked, not guessed)
- The 34 `organized` JPEGs were **already at Airbnb spec**: 2048×1365, 3:2 (1.500),
  0.2–0.6 MB. Re-resizing them would only re-compress and soften — DON'T.
- 7 of 34 are legitimately **portrait** (1365×2048). Decision: **leave as-is**
  (Airbnb displays portrait in-frame; cropping to 3:2 would throw away top/bottom).
- **Root cause found:** every original is **Adobe RGB (1998)**. The earlier 2048px
  export **stripped the ICC profile WITHOUT converting pixels to sRGB**. Browsers/Airbnb
  then read Adobe-RGB pixel data as sRGB → dull/muddy color.
- Proved it: old `organized` file == strip-only export (diff 0.47 ≈ identical) and was
  2.89 away from a proper sRGB conversion. Bug confirmed.

## Fix
Re-exported all 34 from the **full-res originals** (6050×4032), in
`C:\Users\samth\Downloads\2026-06-03 Sam(2).zip` (355 MB, flat `_DSC####(-HDR).jpg`):
- Proper **Adobe RGB → sRGB** ICC transform (ImageCms), sRGB profile embedded
- Lanczos downscale to 2048 long edge, preserve aspect
- Mild output sharpening (UnsharpMask r=1.0, 70%, t=2)
- JPEG quality 90, optimize → avg 535 KB (306–863 KB)
- Mirrors the `organized` tree + filenames

**Output (upload-ready):** `C:\Users\samth\Downloads\sam_unit_photos\organized_srgb\`

## Honest takeaway
This is a **refinement, not a rescue**. Color shift is small (max ~3/255) because these
are neutral beige interiors — Adobe RGB vs sRGB only diverges on **saturated greens**
(plants/bamboo) and warm wood. Verified visually with an 8× diff: only the foliage lit
up; walls/TV/floor unchanged. If photos look soft *on Airbnb*, that's Airbnb's display
recompression (unavoidable); the new set survives that pipeline as well as possible.

## Reusable lesson
For any future photo export: **always convert Adobe RGB → sRGB (transform, not strip)**
before downsizing. Stripping the profile ≠ converting. Camera/editor here exports Adobe
RGB by default.

## Cleanup
Removed temp `_orig_full`, `_zippeek`, `_compare.png`. Left pre-existing loose
`_DSC*.jpg` files in `sam_unit_photos\` untouched (not mine to delete).
