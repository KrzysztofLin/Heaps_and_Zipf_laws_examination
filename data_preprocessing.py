from typing import List
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet, stopwords
from nltk.tokenize import word_tokenize
# recomment this if some of those packages are not installed
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


# function used
def preprocess_data(path: str) -> List[str]:
    # removing information about book and license
    def preambels_endings_remover(text_to_process: str) -> str:
        sub_string1 = " ***"
        sub_string2 = "*** END"
        index1 = text_to_process.index(sub_string1)
        index2 = text_to_process.index(sub_string2)
        preprocesed_file = text_to_process[index1 + len(sub_string1) + 1: index2]
        return preprocesed_file

    # function used to determine word tag
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

    # main function used to 'clear' tokens, removing stopwords, not alphanumeric signs
    def tokenizer(preprocesed_text: str) -> List[str]:
        primary_tokens = word_tokenize(preprocesed_text)
        english_stops = stopwords.words('english')
        secondary_tokens = []
        for word in primary_tokens:
            word = word.lower()
            if word not in english_stops:
                if word.isalnum():
                    secondary_tokens.append(word)
        preprocessed_tokens = []
        lemmatizer = WordNetLemmatizer()
        for token in secondary_tokens:
            preprocessed_tokens.append(lemmatizer.lemmatize(token, pos_tag_transform(token)))
        return preprocessed_tokens

    # function used to activated preprocessing scheme
    def submain(raw_text: str) -> List[str]:
        preprocessed_text = preambels_endings_remover(raw_text)
        preprocessed_tokens = tokenizer(preprocessed_text)
        return preprocessed_tokens

    return submain(path)
