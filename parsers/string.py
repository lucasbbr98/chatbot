import unidecode
import itertools

stop_words = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'e', 'com', 'uma', 'os', 'no',
              'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas ', 'foi', 'ao', 'ele', 'das', 'tem',
              'a', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'ha', 'nos', 'ja', 'esta', 'eu', 'tambem',
              'so', 'pelo', 'pela', 'ate', 'isso', 'ela', 'entre', 'era', 'depois', 'sem', 'mesmo', 'aos',
              'ter', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'estao', 'voce', 'tinha', 'foram', 'essa',
              'num', 'nem', 'suas', 'meu', 'as ', 'minha ', 'tem ', 'numa ', 'pelos ', 'elas', 'ela', 'havia', 'seja',
              'qual', 'sera', 'nos', 'tenho', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'fosse',
              'dele', 'tu', 'te', 'voces', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas',
              'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele',
              'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estao', 'estive',
              'esteve', 'estivemos', 'estiveram', 'estava', 'estavamos', 'estavam', 'estivera', 'estiveramos', 'esteja',
              'estejamos', 'estejam', 'estivesse', 'estivessemos', 'estivessem', 'estiver', 'estivermos', 'estiverem',
              'hei', 'ha', 'havemos', 'hao', 'houve', 'houvemos', 'houveram', 'houvera', 'houveramos', 'haja',
              'hajamos', 'hajam', 'houvesse', 'houvessemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei',
              'houvera', 'houveremos', 'houverao', 'houveria', 'houveriamos', 'houveriam', 'sou', 'somos', 'sao', 'era',
              'eramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'foramos', 'seja', 'sejamos', 'sejam', 'fosse',
              'fossemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'sera', 'seremos', 'serao', 'seria', 'seriamos',
              'seriam', 'tenho', 'tem', 'temos', 'tem', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos',
              'tiveram', 'tivera', 'tiveramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivessemos', 'tivessem',
              'tiver', 'tivermos', 'tiverem', 'terei', 'tera', 'teremos', 'terao', 'teria', 'teriamos', 'teriam']


def tokenize(string: str, unique=False):
    if unique:
        if isinstance(string, list):
            string = ' '.join(string)
        string = ' '.join([''.join(c[0] for c in itertools.groupby(string))])
    tokens = [remove_diacritics(t.lower().strip()) for t in string.split(' ')]
    return [t for t in tokens if t not in stop_words]


def remove_diacritics(string: str):
    return unidecode.unidecode(string)


if __name__ == '__main__':
    x = tokenize('kkkkkk', unique=True)
    print(x)