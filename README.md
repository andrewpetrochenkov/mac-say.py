<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/mac-say.svg?maxAge=3600)](https://pypi.org/project/mac-say/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/mac-say.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/mac-say.py/actions)

### Installation
```bash
$ [sudo] pip install mac-say
```

#### Examples
```python
>>> import mac_say
>>> mac_say.say("hello world")
>>> mac_say.say(["-f","file.txt","-v","Alex"])
```

voices list
```python
>>> mac_say.voices("en")
[('Alex', 'en_US', 'Most people recognize me by my voice.'), ...]
```

background - add `background=True`
```python
>>> mac_say.say("hello world",background=True)
```

Google Text-To-Speech
```python
>>> mac_say.gtts.mp3("en","hello world")
/Users/username/Library/Caches/say/<hash>.mp3

>>> mac_say.gtts.say("en","hello world")
```

```bash
$ python -m mac_say.gtts "en" "hello world"
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>