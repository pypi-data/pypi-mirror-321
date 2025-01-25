import re 

ARABIC2BUCKWALTER = { #mapping from Arabic script to Buckwalter
	u'\u0628': u'b' , u'\u0630': u'*' , u'\u0637': u'T' , u'\u0645': u'm',
	u'\u062a': u't' , u'\u0631': u'r' , u'\u0638': u'Z' , u'\u0646': u'n',
	u'\u062b': u'^' , u'\u0632': u'z' , u'\u0639': u'E' , u'\u0647': u'h',
	u'\u062c': u'j' , u'\u0633': u's' , u'\u063a': u'g' , u'\u062d': u'H',
	u'\u0642': u'q' , u'\u0641': u'f' , u'\u062e': u'x' , u'\u0635': u'S',
	u'\u0634': u'$' , u'\u062f': u'd' , u'\u0636': u'D' , u'\u0643': u'k',
	u'\u0623': u'>' , u'\u0621': u'\'', u'\u0626': u'}' , u'\u0624': u'&',
	u'\u0625': u'<' , u'\u0622': u'|' , u'\u0627': u'A' , u'\u0649': u'Y',
	u'\u0629': u'p' , u'\u064a': u'y' , u'\u0644': u'l' , u'\u0648': u'w',
	u'\u064b': u'F' , u'\u064c': u'N' , u'\u064d': u'K' , u'\u064e': u'a',
	u'\u064f': u'u' , u'\u0650': u'i' , u'\u0651': u'~' , u'\u0652': u'o'
}

SPECIAL_WORDS_MAP = { #Regularly being updated
    "هذا": "هَاذَا",
    "هذه": "هَاذِهِ",
    "هذان": "هَاذَانِ",
    "هؤلاء": "هَاؤُلَاءِ",
    "ذلك": "ذَالِكَ",
    "أولئك": "أولَائِكَ",
    "طه": "طَاهَا",
    "لكن": "لَاكِنْ",
    "لكنه": "لَاكِنَّهُ",
    "لكنك": "لَاكِنَّكَ",
    "لكنكم": "لَاكِنَّكُمْ",
    "لكنهم": "لَاكِنَّهُمْ",
    "لكنهما": "لَاكِنَّهُمَا",
    "لكننا": "لَاكِنَّنَا",
    "الذي": "اللَّذِي",
    "التي": "اللَّتِي",
    "الذين": "اللَّذِينَ",
}

ARABIC_LETTERS = "ابتثجحخدذرزسشصضطظعغفقكلمنهويىءةؤئإأآ"
SHAMSI_LETTERS = "تثدذرزسشصضطظلن"
QAMARI_LETTERS = "اأإآبجحخعغفقكمهوي"
TASHKEEL = "ًٌٍَُِّْ"
PUNCTUATIONS = "".join(["،",",","؛"",",":",",","؟","?","\\-",",","_",",",".",";","\"","\'"])

alf_wasl_pattern = re.compile(f"\\b(?<![{TASHKEEL}])ا[{ARABIC_LETTERS+TASHKEEL}]+\\b",re.UNICODE)
# alf_mad_pattern = re.compile(f"{wb}([{ARABIC_LETTERS+TASHKEEL}]+)(ا[{TASHKEEL}]*)([{ARABIC_LETTERS+TASHKEEL}]+){wb}",re.UNICODE)
ta2_marbootah_sakenah_pattern = re.compile(f"\\b[{ARABIC_LETTERS+TASHKEEL}]+ةْ",re.UNICODE)
words_pattern = re.compile(f"\\b(?<![{PUNCTUATIONS}])[{ARABIC_LETTERS+TASHKEEL}]+\\b",re.UNICODE)
char_alf_lam_pattern = re.compile(f"\\b[كفوب][{TASHKEEL}]*ا[{TASHKEEL}]*ل[{TASHKEEL}]*[{ARABIC_LETTERS+TASHKEEL}]+\\b",re.UNICODE)
char_char_alf_lam_pattern = re.compile(f"\\b[وف][{TASHKEEL}]*[كفوب][{TASHKEEL}]*ا[{TASHKEEL}]*ل[{TASHKEEL}]*[{ARABIC_LETTERS+TASHKEEL}]+\\b",re.UNICODE)
alf_lam_pattern = re.compile(f"\\bا[{TASHKEEL}]*ل[{TASHKEEL}]*[{ARABIC_LETTERS+TASHKEEL}]+\\b",re.UNICODE)
alf_lam_bos = re.compile(f"(^|[{PUNCTUATIONS}][\\s]*)(ا[{TASHKEEL}]*ل[{TASHKEEL}]*[{ARABIC_LETTERS+TASHKEEL}]+(\\b))",re.UNICODE)
arabic_letters_pattern = re.compile(f"[{ARABIC_LETTERS}]",re.UNICODE)
all_arabic_pattern = re.compile(f"[{ARABIC_LETTERS+TASHKEEL+PUNCTUATIONS} ]+",re.UNICODE)
punctuations_pattern = re.compile(f"[{PUNCTUATIONS}]",re.UNICODE)
sentence_segments_pattern = re.compile(f"[^{PUNCTUATIONS}]+[{PUNCTUATIONS}]+",re.UNICODE)
no_punc_segments_pattern = re.compile(f"[^{PUNCTUATIONS}]+$",re.UNICODE)