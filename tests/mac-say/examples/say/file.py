#!/usr/bin/env python
import os
import mac_say

path = os.path.join(os.path.dirname(__file__), "file.txt")
mac_say.say(["-v", path])
mac_say.say(["-v", path], background=True)
