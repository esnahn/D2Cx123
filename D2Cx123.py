from fontforge import *
from psMat import *
from pathlib import Path

directory = Path(__file__).parent
print(directory)
d2 = open(str(directory / "D2Coding-Ver1.3.2-20180524.ttf"))

d2.familyname = "D2Cx123"
d2.fontname = "D2Cx123"
d2.fullname = "D2C 123% width"

# The strings in the sfnt ‘name’ table.
# A tuple of all MS names.
# Each name is itself a tuple of strings (language,strid,string).
d2.sfnt_names = (
    (
        "English (US)",
        "Copyright",
        "Copyright (c) 2015-2016 NHN Corporation. All rights reserved. Font designed by FONTRIX Inc.",
    ),
    ("English (US)", "Family", "D2Cx123"),
    ("English (US)", "SubFamily", "Regular"),
    ("English (US)", "UniqueID", "D2Cx123 Regular"),
    ("English (US)", "Fullname", "D2Cx123"),
    ("English (US)", "Version", "Version 1.0.0"),
    ("English (US)", "PostScriptName", "D2Cx123"),
    (
        "English (US)",
        "Trademark",
        "D2Coding is a registered trademark of NHN Corporation.",
    ),
    (
        "English (US)",
        "License",
        "This Font Software is licensed under the SIL Open Font License, Version 1.1.",
    ),
    (
        "English (US)",
        "License URL",
        "http://dev.naver.com/wiki/nanumfont/index.php/OpenFontLicense",
    ),
    ("English (US)", "Preferred Family", "D2Cx123"),
    ("English (US)", "Preferred Styles", "Regular"),
    (
        "Korean",
        "Copyright",
        "Copyright (c) 2015-2016 NHN Corporation. All rights reserved. Font designed by FONTRIX Inc.",
    ),
    (65535, "CID findfont Name", "D2Cx123"),
)

# for glyph in ["uniB2E4", "uniB78C", "uniC950", "one", "two"]:
#     print(glyph, d2[glyph].width, d2[glyph].left_side_bearing, d2[glyph].right_side_bearing)

d2.selection.all()
scale_mat = scale(1.23, 1)
d2.transform(scale_mat)
d2.changeWeight(-20)

new_upm = 1230
for glyph in d2:
    if d2[glyph].width <= new_upm // 4:
        d2[glyph].width = 0
    elif d2[glyph].width <= 3 * new_upm // 4:
        d2[glyph].width = new_upm // 2
    elif d2[glyph].width <= 5 * new_upm // 4:
        d2[glyph].width = new_upm
    else:
        print(
            glyph,
            d2[glyph].width,
            d2[glyph].left_side_bearing,
            d2[glyph].right_side_bearing,
        )

d2.generate(str(directory / "D2Cx123.ttf"))
