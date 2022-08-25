from Class.urna import *
import easyocr

urna = Urna()

class Ocr:
    def __init__(self):
        self.readOcrIndexes = []
        self.federalCandidatesBRead = []
        self.numberKeysBRead = []
        self.warningsBRead = []
        self.messagesBRead = []
        self.wordsBRead = []
        self.allBRead = []
        self.wasCandidateRead = False

    def apply_ocr(self, frame):
        reader = easyocr.Reader(['pt', 'en'])
        textread = reader.readtext(frame, detail=0)
        return str(textread)

    def apply_ocr_in_frames(self, lstpaths, totalframecount):

        for j in range(totalframecount):
            readocrinframes = self.apply_ocr('C:\\Users\\eafs3\\Documents\\GitHub\\MonografiaEric\\Resources\\' + 'frame' + str(j) + ".jpg")
            self.readOcrIndexes.append(readocrinframes)
            print(self.readOcrIndexes)

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

    def set_all_b_read_array(self, federal_candidate, number_keys, warning, message, word):
        self.allBRead.append([federal_candidate, number_keys, warning, message, word])

    def find_federal_candidate(self, candidate):
        for k in urna.federalCandidates:
            if k == candidate:
                self.set_federal_candidate_b_read(k)
                self.wasCandidateRead = True
                break

    def find_number_keys(self, candidate):
        for position, item in enumerate(urna.federalCandidates):
            if item == candidate:
                self.set_number_keys_b_read(position)

    def find_warning(self, warning):
        pass

    def find_message(self, message):
        pass

    def find_word(self, word):
        pass

    def make_full_b_read_list(self):
        pass

    def compare_string(self):
        for i in Ocr.readOcrIndexes:
            for j in i:
                self.find_federal_candidate(j)

                if self.wasCandidateRead:
                    self.find_number_keys(self.federalCandidatesBRead)


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

