class Urna:
    def __init__(self):
        self.federalCandidates = ['DEPUTADO FEDERAL', 'DEPUTADO ESTADUAL',
                                  'SENADOR', 'GOVERNADOR', 'PRESIDENTE']
        self.numberKeys = [4, 5, 3, 2, 2]
        self.digit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "CONFIRMA", "BRANCO", "CORRIGE"]
        self.warnings = ['NÚMERO ERRADO', 'NUMERO ERRADO']
        self.messages = ['VOTO EM BRANCO', 'EM BRANCO', 'BRANCO', 'VOTO NULO', 'FIM']
        self.words = ["NOME", "INOME"]

        self.twoDigits = {
            '1-1': None, '1-2': None, '1-3': None, '1-4': None, '1-5': None, '1-6': None, '1-7': None, '1-8': None,
            '1-9': None, '1-0': None, '1-CONFIRMA': None, '1-BRANCO': None, '1-CORRIGE': None,

            '2-1': None, '2-2': None, '2-3': None, '2-4': None, '2-5': None, '2-6': None, '2-7': None, '2-8': None,
            '2-9': None, '2-0': None, '2-CONFIRMA': None, '2-BRANCO': None, '2-CORRIGE': None,

            '3-1': None, '3-2': None, '3-3': None, '3-4': None, '3-5': None, '3-6': None, '3-7': None, '3-8': None,
            '3-9': None, '3-0': None, '3-CONFIRMA': None, '3-BRANCO': None, '3-CORRIGE': None,

            '4-1': None, '4-2': None, '4-3': None, '4-4': None, '4-5': None, '4-6': None, '4-7': None, '4-8': None,
            '4-9': None, '4-0': None, '4-CONFIRMA': None, '4-BRANCO': None, '4-CORRIGE': None,

            '5-1': None, '5-2': None, '5-3': None, '5-4': None, '5-5': None, '5-6': None, '5-7': None, '5-8': None,
            '5-9': None, '5-0': None, '5-CONFIRMA': None, '5-BRANCO': None, '5-CORRIGE': None,

            '6-1': None, '6-2': None, '6-3': None, '6-4': None, '6-5': None, '6-6': None, '6-7': None, '6-8': None,
            '6-9': None, '6-0': None, '6-CONFIRMA': None, '6-BRANCO': None, '6-CORRIGE': None,

            '7-1': None, '7-2': None, '7-3': None, '7-4': None, '7-5': None, '7-6': None, '7-7': None, '7-8': None,
            '7-9': None, '7-0': None, '7-CONFIRMA': None, '7-BRANCO': None, '7-CORRIGE': None,

            '8-1': None, '8-2': None, '8-3': None, '8-4': None, '8-5': None, '8-6': None, '8-7': None, '8-8': None,
            '8-9': None, '8-0': None, '8-CONFIRMA': None, '8-BRANCO': None, '8-CORRIGE': None,

            '9-1': None, '9-2': None, '9-3': None, '9-4': None, '9-5': None, '9-6': None, '9-7': None, '9-8': None,
            '9-9': None, '9-0': None, '9-CONFIRMA': None, '9-BRANCO': None, '9-CORRIGE': None,

            '0-1': None, '0-2': None, '0-3': None, '0-4': None, '0-5': None, '0-6': None, '0-7': None, '0-8': None,
            '0-9': None, '0-0': None, '0-CONFIRMA': None, '0-BRANCO': None, '0-CORRIGE': None,
        }
