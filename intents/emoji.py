import os
import random
import pandas as pd
from intents.base import Intent, TRAIN_BASES_PATH


class EmojiIntent(Intent):
    def __init__(self):
        super().__init__(name='emoji')
        self.emojis = pd.read_csv(os.path.join(TRAIN_BASES_PATH, 'emojis.csv'), sep=';')
        self.emojis['Tags'] = self.emojis['Tags'].str.split(', ')
        self.emojis = self.emojis.explode('Tags').reset_index(drop=True)
        self.emojis['Tags'] = self.emojis['Tags'].str.strip()

    def maps(self, msg) -> (bool, str):
        try:
            msg = self.tokenize(msg)
            responses = self.emojis[self.emojis['Tags'].isin(msg)]
            if responses.empty:
                msg = self.tokenize(msg, unique=True)
                responses = self.emojis[self.emojis['Tags'].isin(msg)]

            if responses.empty:
                return False, ''

            return True, ' ' + responses['Icon'].sample(n=1).iloc[0] + ' '

        except Exception as e:
            print(e)
            return False, ''

    @classmethod
    def happy(cls):
        return random.choice(["😀", "😃", "😄", "😁", "😆"])

    @classmethod
    def sad(cls):
        return random.choice(['😔', '😩', '😢', '😪', '😕'])

    @classmethod
    def funny(cls):
        return random.choice(['😂', '🤣', '😜', '😆'])


if __name__ == '__main__':
    intent = EmojiIntent()
    mapped, response = intent.maps('kkkkkkkkk')
    if mapped:
        print(response)
