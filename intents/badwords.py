import os
import random
from intents.base import Intent, TRAIN_BASES_PATH
import pandas as pd


class BadwordsIntent(Intent):
    def __init__(self):
        super().__init__(name='badwords')
        self.bad_words = pd.read_csv(os.path.join(TRAIN_BASES_PATH, 'badwords.csv')).iloc[:, 0].tolist()
        self.responses = [
           'Eu não vou responder a isso 🙁', 'Isso não é legal 😱' , 'Desculpe 🙁'
        ]

    def maps(self, msg) -> (bool, str):
        try:
            if any(word in self.bad_words for word in self.tokenize(msg)):
                return True, random.choice(self.responses)

            return False, ''
        except Exception as e:
            print(e)
            return False, ''


if __name__ == '__main__':
    intent = BadwordsIntent()
    mapped, response = intent.maps('babaca')
    if mapped:
        print(response)