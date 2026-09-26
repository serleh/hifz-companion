import re


ARABIC_DIACRITICS = re.compile(r"[\u0617-\u061A\u064B-\u065F\u0670]")


def normalize_arabic(text):
    return ARABIC_DIACRITICS.sub("", text)