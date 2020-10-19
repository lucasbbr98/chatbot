from intents.base import Intent


class JokeIntent(Intent):
    def __init__(self):
        super().__init__(name='joke')

    def maps(self, msg) -> (bool, str):
        pass

    def get_response(self, msg=None) -> str:
        pass