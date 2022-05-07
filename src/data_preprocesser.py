from typing import List

from nltk import pos_tag
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# recomment this if some of those packages are not installed
"""
import nltk
nltk.download('omw-1.4')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('snowball_data')
nltk.download('universal_tagset')
nltk.download('averaged_perceptron_tagger')
"""


def preprocess_data(raw_text: str) -> List[str]:
    preprocessed_text = preambels_endings_remover(raw_text)
    preprocessed_tokens = tokenizer(preprocessed_text)
    return preprocessed_tokens


# removing information about book and license
def preambels_endings_remover(text_to_process: str) -> str:
    sub_string1 = " ***"
    sub_string2 = "*** END"
    index1 = text_to_process.index(sub_string1)
    index2 = text_to_process.index(sub_string2)
    preprocessed_text = text_to_process[index1 + len(sub_string1) + 1 : index2]
    return preprocessed_text


# main function used to 'clear' tokens, removing stopwords, not alphanumeric signs
def tokenizer(preprocessed_text: str) -> List[str]:
    raw_tokens = word_tokenize(preprocessed_text)
    early_preprocessed_tokens = []
    for word in raw_tokens:
        word = word.lower()
        if word not in stopwords.words("english"):
            if word.isalnum():
                early_preprocessed_tokens.append(word)
    preprocessed_tokens = []
    for token in early_preprocessed_tokens:
        preprocessed_tokens.append(
            WordNetLemmatizer().lemmatize(token, _pos_tag_transform(token))
        )
    return preprocessed_tokens


# function used to determine word tag
def _pos_tag_transform(word: str) -> str:
    tag_temp = pos_tag([word], tagset="universal")[0][1]
    if tag_temp == "VERB":
        tag = wordnet.VERB
    elif tag_temp == "ADJ":
        tag = wordnet.ADJ
    elif tag_temp == "ADV":
        tag = wordnet.ADV
    else:
        tag = wordnet.NOUN
    return tag
