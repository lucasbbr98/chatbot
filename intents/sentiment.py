import os
import random
import pandas as pd
from intents.base import Intent, TRAIN_BASES_PATH
from intents.emoji import EmojiIntent


class SentimentIntent(Intent):
    def __init__(self, emoji_intent: EmojiIntent = EmojiIntent()):
        super().__init__(name='sentiment')
        self.emojis = emoji_intent
        self.sentiments = pd.read_csv(os.path.join(TRAIN_BASES_PATH, 'sentiment.csv'))

    def maps(self, msg) -> (bool, str):
        try:
            msg = self.tokenize(msg)
            responses = self.sentiments[self.sentiments['Value'].isin(msg)]
            if responses.empty:
                msg = self.tokenize(msg, unique=True)
                responses = self.sentiments[self.sentiments['Value'].isin(msg)]

            if responses.empty:
                return False, ''

            sentiment = responses['Sentiment'].sum()
            if sentiment < 0:
                return True, self.negative_msg()

            if sentiment > 0:
                return True, self.positive_msg()

            return True, self.neutral_msg()

        except Exception as e:
            print(e)
            return True, self.neutral_msg()


    def neutral_msg(self):
        return random.choice(
            [
                f'Hmmm...',
                f'🤨',
                f'🤔'            ]
        )

    def positive_msg(self):
        return random.choice(
            [
                f'Felicidade {self.emojis.happy()}',
                f'Fico feliz {self.emojis.happy()}',
                f'Bacana {self.emojis.happy()}',
                f'Ótimo {self.emojis.happy()}'
            ]
        )

    def negative_msg(self):
        return random.choice(
            [
                f'Puxa {self.emojis.sad()}',
                f'Sinto muito {self.emojis.sad()}',
                f'Anotado {self.emojis.sad()}',
                f'Foi mal {self.emojis.sad()}'
            ]
        )


if __name__ == '__main__':
    intent = EmojiIntent()
    mapped, response = intent.maps('kkkkkkkkk')
    if mapped:
        print(response)
