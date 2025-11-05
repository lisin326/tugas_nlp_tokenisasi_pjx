import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = """Belajar NLP dengan Python 
Editor VS Code
library nltk (Natural Language Toolkit)."""

tokens = word_tokenize(text)

print("Teks asli:", text)
print("Hasil tokenisasi:", tokens)


# by: muhlisin
