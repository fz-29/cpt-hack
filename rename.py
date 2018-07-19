rename_dict = {
    "Q467":"woman",
    "Q8441":"man",
    "Q345":"mary",
    "Q527":"sky",
    "Q10884":"tree",
    "Q8074":"cloud",
    "Q3010":"boy",
    "Q942467":"childJesus",
    "Q302":"JesusChrist",
    "Q1144593":"sitting",
}

import os
for di in rename_dict.keys():
    if os.path.exists(di):
        os.rename(di, rename_dict[di])