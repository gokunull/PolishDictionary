import random
import time
import codecs
import datetime
wordslist = ['color_words','comparisons_words','exceptions_words','family_words','general_words',
            'mood_words','numbers','numbers_x10','profession_words']
filename = wordslist[0]
logname = datetime.datetime.now().strftime("%m.%d-%H;%M;%S")
logfile = codecs.open(f"C:/Other/PythonProject/dictionary/log/{logname}_{filename}.txt", "w", "utf_8_sig")
words = codecs.open(f"C:/Other/PythonProject/dictionary/words/{filename}.txt", "r", "utf_8_sig")
unique_words = list(set(words))
random.shuffle(unique_words)
random.SystemRandom().shuffle(unique_words)
for i in unique_words:
    print(i)
    time.sleep(0.1)
logfile.writelines("%s\n" % i for i in unique_words)
logfile.close()

# list = color_words.txt, comparisons_words.txt,
# exceptions_words.txt, family_words.txt,
# general_words.txt, mood_words.txt,
# numbers.txt, numbers_x10.txt,
# profession_words.txt, ...
