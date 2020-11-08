import random
import time
import codecs
# list = color_words.txt, comparisons_words.txt,
# exceptions_words.txt, family_words.txt,
# general_words.txt, mood_words.txt,
# numbers.txt, numbers_x10.txt,
# profession_words.txt, 
words = codecs.open("words/x10_numbers.txt", "r", "utf_8_sig")
unique_words = list(set(words))
random.shuffle(unique_words)
random.SystemRandom().shuffle(unique_words)
for i in unique_words:
    print(i)
    time.sleep(15)
    
