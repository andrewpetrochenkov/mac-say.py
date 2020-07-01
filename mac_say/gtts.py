__all__ = ['mp3', 'say']


# -*- coding: utf-8 -*-
"""create `. mp3` file with Google Text-to-Speech and play it with `afplay`"""
import click
from gtts import gTTS
import hashlib
import os
import tempfile


def mp3(lang, string):
    """create .mp3 file (if cache not exists) and return path"""
    md5 = hashlib.md5(str("".join([lang, string])).encode('utf-8')).hexdigest()
    tmp = tempfile.mkstemp()[1]
    dst = os.path.expanduser("~/Library/Caches/say/%s.mp3" % md5)
    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))
    if not os.path.exists(dst):
        tts = gTTS(string, lang=lang)
        tts.save(tmp)
        os.rename(tmp, dst)
    return dst


def say(lang, string):
    """creare `.mp3` file and play it with `afplay`"""
    path = mp3(lang, string)
    os.system("afplay %s" % path)


MODULE_NAME = "mac_say.gtts"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s lang strings ...' % MODULE_NAME


@click.command()
@click.argument('lang', required=True)
@click.argument('strings', nargs=-1, required=True)
def _cli(lang, strings):
    string = " ".join(strings)
    path = mp3(lang, string)
    os.system("afplay %s" % path)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
