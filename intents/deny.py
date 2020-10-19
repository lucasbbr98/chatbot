import random
from intents.base import Intent


class DenyIntent(Intent):
    def __init__(self, client_name):
        super().__init__(name='deny')
        self.client_name = client_name
        self.triggers = [
            'n', 'ñ', 'nao', 'no', 'nop', 'naum', 'nan', 'errado', 'errou',
            'nenhum', 'nenhuma', 'nunca', 'jamais', 'errei', 'mentira'
        ]

        self.responses = [
           'Puxa %NAME% 😬', 'Hmmm 🤔', 'Entendi %NAME%...'
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
    intent = DenyIntent('lucas')
    mapped, response = intent.maps('s')
    if mapped:
        print(response)