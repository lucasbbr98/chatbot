import os
import random
from intents.base import Intent


class GreetIntent(Intent):
    def __init__(self, client_name):
        super().__init__(name='greet')
        self.client_name = client_name
        self.triggers = [
            'oi', 'ola', 'oie', 'hi', 'coe', 'iai', 'eae', 'tudo bem', 'td bem', 'bom dia', 'boa tarde', 'boa noite',
            'como esta', 'como vc esta', 'como vai', 'de boa', 'e ai', 'alo'
        ]

        self.responses = [
           'Oi %NAME%', 'Olá %NAME%', 'Tudo bem %NAME% ?', ''
        ]

    def maps(self, msg) -> (bool, str):
        try:
            if any(word in self.triggers for word in self.tokenize(msg)):
                return True, random.choice(self.responses).replace('%NAME%', self.client_name.capitalize())

            return False, ''
        except Exception as e:
            print(e)
            return False, ''


if __name__ == '__main__':
    intent = GreetIntent()
    mapped, response = intent.maps('babaca')
    if mapped:
        print(response)