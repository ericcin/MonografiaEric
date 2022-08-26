from Class.urna import *
import easyocr

urna = Urna()

class Ocr:
    def __init__(self):
        self.readOcrIndexes = []
        self.federalCandidateBRead = ""
        self.numberKeysBRead = 0
        self.warningBRead = ""
        self.messageBRead = ""
        self.wordBRead = ""
        self.allBRead = []

        self.wasCandidateRead = False

    def uppercase_all_str(self, list):
        for i in range(len(list)):
            list[i] = list[i].upper()
        return list

    def apply_ocr(self, frame):
        reader = easyocr.Reader(['pt', 'en'])
        textread = reader.readtext(frame, detail=0)
        textread = self.uppercase_all_str(textread)
        return textread

    def apply_ocr_in_frames(self, lstpaths, totalframecount):

        for j in range(totalframecount):
            readocrinframes = self.apply_ocr('C:\\Users\\eafs3\\Documents\\GitHub\\MonografiaEric\\Resources\\' +
                                             'frame' + str(j) + ".jpg")
            self.readOcrIndexes.append(readocrinframes)
            print(self.readOcrIndexes)

    def set_federal_candidate_b_read(self, federal_candidate):
        self.federalCandidateBRead = federal_candidate

    def set_number_keys_b_read(self, number_key):
        self.numberKeysBRead = number_key

    def set_warning_b_read(self, warning):
        self.warningBRead = warning

    def set_message_b_read(self, message):
        self.messageBRead = message

    def set_word_b_read(self, word):
        self.wordBRead = word

    def find_federal_candidate(self, candidate):
        for i in urna.federalCandidates:
            if i == candidate:
                self.set_federal_candidate_b_read(i)
                self.wasCandidateRead = True
                break

    def find_number_keys(self, candidate):
        for position, item in enumerate(urna.federalCandidates):
            if item == candidate:
                self.set_number_keys_b_read(position)

    def find_warning(self, warning): # talvez isso possa ser irrelevante
        warning_not_been_read = True
        for i in urna.warnings:
            if i == warning:
                self.set_warning_b_read(warning)
                warning_not_been_read = False
        if warning_not_been_read:
            self.set_warning_b_read(None)

    def find_message(self, message):
        message_not_been_read = True
        for i in urna.messages:
            if i == message:
                self.set_message_b_read(message)
                message_not_been_read = False
        if message_not_been_read:
            self.set_message_b_read(None)

    def find_word(self, word):
        word_not_been_read = True
        for i in urna.words:
            if i == word:
                self.set_word_b_read(word)
                word_not_been_read = False
        if word_not_been_read:
            self.set_word_b_read(None)

    def set_all_b_read_array(self, federal_candidate, number_keys, warning, message, word):
        self.allBRead.append([federal_candidate, number_keys, warning, message, word])

    def make_full_b_read_list(self):
        pass

    def compare_string(self):
        for i in self.readOcrIndexes:
            for j in i:
                self.find_federal_candidate(j)

                if self.wasCandidateRead:
                    self.find_number_keys(self.federalCandidateBRead)
                    self.find_warning(j)
                    self.find_message(j)
                    self.find_word(j)

            self.set_all_b_read_array(self.federalCandidateBRead, self.numberKeysBRead, self.warningBRead,
                                      self.messageBRead, self.wordBRead)

                    # self.set_number_keys_b_read(self.numberKeys[count-1])
                    #
                    # if j == 'NÚMERO ERRADO' or "NUMERO ERRADO":
                    #     self.set_warning_b_read(self.warnings[0])
                    # else:
                    #     self.set_warning_b_read(None)
                    #
                    # for l in self.messages:
                    #     if l == j:
                    #         self.set_message_b_read(j)
                    #         break
                    # if j == "NOME":
                    #     self.set_word_b_read(self.words[0])

