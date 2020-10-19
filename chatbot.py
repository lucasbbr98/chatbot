from datetime import datetime
from parsers.string import remove_diacritics
from intents.badwords import BadwordsIntent
from intents.emoji import EmojiIntent
from intents.greet import GreetIntent
from intents.sentiment import SentimentIntent
from intents.start import StartIntent
from intents.confirm import ConfirmIntent
from intents.deny import DenyIntent
from intents.fallback import FallbackIntent


class ChatBot:
    def __init__(self, client_name: str):
        client_name = str(client_name)
        if ' ' in client_name:
            self.client_name = remove_diacritics(client_name.split(' ')[0].strip()).capitalize()
        else:
            self.client_name = remove_diacritics(client_name.strip()).capitalize()
        self.project = ''
        self.motivation = ''
        self.category = ''
        self.progress = 0
        self.project_done = False

        # Train Variables
        self.intents = [
            BadwordsIntent(),
            GreetIntent(self.client_name),
            ConfirmIntent(self.client_name),
            DenyIntent(self.client_name),
            EmojiIntent(),
            SentimentIntent(),
            FallbackIntent(self.client_name),
        ]

        self.fallback = FallbackIntent(self.client_name)

    def start(self):
        return StartIntent(self.client_name).maps('start_msg')[1]

    def reply(self, sentence):
        try:
            msg = self.fallback.maps('default_msg')[1]
            if sentence is None or not isinstance(sentence, str) or sentence.strip() == '':
                return msg

            if not self.project_done and self.progress > 0:
                if self.progress == 1:
                    self.project = sentence
                if self.progress == 2:
                    self.motivation = sentence
                if self.progress == 3:
                    self.category = sentence
                if self.progress == 4:
                    return self.next_progress()
                self.progress += 1
                return self.next_progress()

            mapped_intent = None
            for i in self.intents:
                mapped, msg = i.maps(sentence)
                if mapped:
                    mapped_intent = i
                    break

            if mapped_intent is None:
                return self.fallback.maps('default_msg')[1]

            if self.progress == 0:
                if mapped_intent.name == 'confirm':
                    self.progress += 1

                if mapped_intent.name == 'deny':
                    self.progress += -1


            return msg + '\r\n' + self.next_progress()

        except Exception as e:
            print(e)
            return 'Hmm estou tendo dificuldades em processar isso...'


    def next_progress(self):
        if self.project_done:
            return ''
        if self.progress < 0:
            self.project_done = True
            return f'{self.client_name} quando você tiver um projeto em mente, saiba que você pode contar com a gente para desenvolvê-lo.' \
                   f'\r\nSó para você saber, nós criamos diversas soluções digitais, como:' \
                   f'\r\nWebsites, Macros de Excel, Leitura de Emails Automáticos, Exportação de Bases para Bancos de Dados, Batimentos no FTS e Muito Mais 😉' \
                   f'\r\nSe quiser, pode continuar conversando comigo, ou digite "humano" para conversar com um de nossos especialistas 😃'

        if self.progress == 0:
            return self.start()

        if self.progress == 1:
            return f'{self.client_name} você já deu o primeiro passo, deixe-nos ajudar a dar o segundo! 😉' \
                   f'\r\nQual seria o nome do seu projeto?' \

        if self.progress == 2:
            return f'Muito bem! 😊\r\n' \
                   f'Qual seria a motivação para esse projeto?\r\n' \
                   f'Por exemplo: Diminuir a quantidade de emails diários'

        if self.progress == 3:
            return f'Quase acabamos! 😃\r\n' \
                   f'Qual seria o produto final do seu projeto?\r\n' \
                   f'Por exemplo: Website, Excel, Não Sei?'

        if self.progress == 4:
            self.project_done = True
            return f'Isso foi tudo! 🥳\r\n' \
                   f'{self.client_name} obrigado por mudar o banco!\r\n' \
                   f'Em breve, um especialista irá entrar em contato com você.'

    @staticmethod
    def greeting():
        now = datetime.now()
        if now.hour > 18:
            return 'Boa noite'
        if now.hour < 12:
            return 'Bom dia'

        return 'Boa tarde'


if __name__ == '__main__':
    bot = ChatBot(client_name='Lucas')
    print(bot.start())
    while True:
        msg = input()
        print(bot.reply(sentence=msg))
