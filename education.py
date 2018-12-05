import pandas as pd
import spacy
import numpy as np
#import nltk
#nltk.download()
from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk
from Word_extractor import get_org_from_sent
import string

nlp = spacy.load('en_core_web_sm')
data = pd.read_csv('L.csv')
bio = data.Biography

print(the_last_final_list)
print(final_list)

EDUCATION = []
for row in range(len(the_last_final_list[:100])):
    the_lol_list = []
    try:
        if the_last_final_list[row][0]:
            the_lol_list.append(the_last_final_list[row][0])
        else:
            the_lol_list.append('')
        if final_list[row][0]:
            the_lol_list.append(final_list[row][0])
        else:
            the_lol_list.append('')
        if the_last_final_list[row][1]:    
            the_lol_list.append(the_last_final_list[row][1])
        else:
            the_lol_list.append('')
        if final_list[row][1]:
            the_lol_list.append(final_list[row][1])
        else:
            the_lol_list.append('')
        if the_last_final_list[row][2]:
            the_lol_list.append(the_last_final_list[row][2])
        else:
            the_lol_list.append('')
    except IndexError:
        pass
    print(the_lol_list)
    EDUCATION.append(the_lol_list)
    
    
    