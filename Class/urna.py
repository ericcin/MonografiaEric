from Class.ocr import *


class Urna:
    def __init__(self):
        self.federalCandidates = ['DEPUTADO FEDERAL,', 'DEPUTADO ESTADUAL',
                                  'SENADOR', 'GOVERNADOR', 'PRESIDENTE']
        self.numberKeys = [4, 4, 3, 2, 2]
        self.warnings = ['NÚMERO ERRADO']
        self.messages = ['VOTO EM BRANCO', 'VOTO NULO', 'FIM']
        self.words = ["NOME"]

        self.federalCandidatesBRead = []
        self.numberKeysBRead = []
        self.warningsBRead = []
        self.messagesBRead = []
        self.wordsBRead = []

    def set_federal_candidate_b_read(self, federal_candidate):
        self.federalCandidatesBRead.append(federal_candidate)

    def set_number_keys_b_read(self, number_key):
        self.numberKeysBRead.append(number_key)

    def set_warning_b_read(self, warning):
        self.warningsBRead.append(warning)

    def set_message_b_read(self, message):
        self.messagesBRead.append(message)

    def set_word_b_read(self, word):
        self.wordsBRead.append(word)

    def compare_string(self):
        was_candidate_read = False

        for i in Ocr.readOcrIndexes:
            for j in i:
                count = 0
                for k in self.federalCandidates:
                    if k == j:
                        self.set_federal_candidate_b_read(k)
                        was_candidate_read = True
                        break
                    count += 1

                    if was_candidate_read:
                        self.set_number_keys_b_read(self.numberKeys[count-1])

                        if j == 'NÚMERO ERRADO' or "NUMERO ERRADO":
                            self.set_warning_b_read(self.warnings[0])
                        else:
                            self.set_warning_b_read(None)

                        for l in self.messages:
                            if l == j:
                                self.set_message_b_read(j)
                                break
                        if j == "NOME":
                            self.set_word_b_read(self.words[0])





