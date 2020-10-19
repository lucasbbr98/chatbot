import random
from intents.base import Intent


class StartIntent(Intent):
    def __init__(self, client_name):
        super().__init__(name='start')
        self.client_name = client_name

        self.responses = [
            '%NAME%, você tem um projeto em mente?',
            'Vamos criar uma ideia juntos %NAME%?',
            'Cansou de fazer tarefas repetitivas %NAME%?',
            '%NAME%, você já pensou em robotizar algum processo do seu dia a dia?',
            '%NAME%, você já pensou em criar um sistema para a sua área utilizar?']

    def maps(self, msg) -> (bool, str):
        try:
            return True, random.choice(self.responses).replace('%NAME%', self.client_name.capitalize())
        except Exception as e:
            print(e)
            return False, ''


if __name__ == '__main__':
    intent = StartIntent('lucas')
    mapped, response = intent.maps('babaca')
    if mapped:
        print(response)