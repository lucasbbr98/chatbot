import random
from intents.base import Intent


class ConfirmIntent(Intent):
    def __init__(self, client_name):
        super().__init__(name='confirm')
        self.client_name = client_name
        self.triggers = [
            's', 'sim', 'yes', 'y', 'si', 'confirmado', 'confirmados', 'confirmo', 'certo', 'ok', 'proximo', 'proxima',
            'verdade', 'vdd'
        ]

        self.responses = [
           'Beleza %NAME%', 'Entendi %NAME%', 'Certo %NAME%', 'Perfeito %NAME%'
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
    intent = ConfirmIntent('lucas')
    mapped, response = intent.maps('s')
    if mapped:
        print(response)