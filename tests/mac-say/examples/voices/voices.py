#!/usr/bin/env python
import mac_say

voices = mac_say.voices()

english_voices = mac_say.voices("en")
print("english_voices (%s):" % len(english_voices))
for v in english_voices:
    print(v)
