import random
from intents.base import Intent


class FallbackIntent(Intent):
    def __init__(self, client_name):
        super().__init__(name='fallback')
        self.client_name = client_name

        self.responses = [
            'Hmm não entendi isso 🤨',
            'Não conta para ninguem, mas meu desenvolvedor não me preparou para isso 🤐',
            'Desculpe %NAME%, mas eu não entendi o que você quis dizer',
            'Ops.. não entendi 😶']

    def maps(self, msg) -> (bool, str):
        try:
            return True, random.choice(self.responses).replace('%NAME%', self.client_name.capitalize())
        except Exception as e:
            print(e)
            return False, ''


if __name__ == '__main__':
    intent = FallbackIntent('lucas')
    mapped, response = intent.maps('babaca')
    if mapped:
        print(response)