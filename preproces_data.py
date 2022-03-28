import os
from typing import List, Dict
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


#recomment this if some of those packages are not installed
'''
import nltk
nltk.download('omw-1.4')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('snowball_data')
nltk.download('universal_tagset')
nltk.download('averaged_perceptron_tagger')
'''


def preproces_data(path: str):

    def preambels_endings_remover(text_to_process: str) -> str:
        sub_string1 = " ***"
        sub_string2 = "*** END"
        index1 = text_to_process.index(sub_string1)
        index2 = text_to_process.index(sub_string2)
        preprocesed_file = text_to_process[index1 + len(sub_string1) + 1: index2]
        return preprocesed_file

    def pos_tag_transform(word: str) -> str:
        tag_temp = pos_tag([word], tagset='universal')[0][1]
        if tag_temp == 'VERB':
            tag = wordnet.VERB
        elif tag_temp == 'ADJ':
            tag = wordnet.ADJ
        elif tag_temp == 'ADV':
            tag = wordnet.ADV
        else:
            tag = wordnet.NOUN
        return tag

    def tokenizer(preprocesed_text: str) -> List[str]:
        primar_tokens = word_tokenize(preprocesed_text)
        english_stops = stopwords.words('english')
        secondary_tokens = []
        for word in primar_tokens:
            word = word.lower()
            if word not in english_stops:
                if word.isalnum():
                    secondary_tokens.append(word)
        preprocesed_tokens = []
        for token in secondary_tokens:
            preprocesed_tokens.append(lemmatizer.lemmatize(token, pos_tag_transform(token)))
        return preprocesed_tokens

    def submain(raw_text: str) -> List[str]:

        preprocesed_text = preambels_endings_remover(raw_text)
        #except ValueError:
        #    preprocesed_text = raw_text
        preprocesed_tokens = tokenizer(preprocesed_text)
        return preprocesed_tokens

    return submain(path)