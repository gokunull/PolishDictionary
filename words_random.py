import random
import time
import codecs
words = codecs.open("words/general_words.txt", "r", "utf_8_sig")
unique_words = list(set(words))
random.shuffle(unique_words)
random.SystemRandom().shuffle(unique_words)
for i in unique_words:
    print(i)
    time.sleep(20)
    