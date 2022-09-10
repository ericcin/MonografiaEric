import easyocr
import re

class Ocr:
    def __init__(self, federalCandidates, numberKeys, digits, warnings, messages, words):

        self.readOcrIndexes = []

        self.federalCandidateBRead = ""
        self.numberKeysBRead = 0
        self.warningBRead = ""
        self.digitBRead = ""
        self.messageBRead = ""
        self.wordBRead = ""
        self.allBRead = []

        self.physicalFederalCandidates = federalCandidates
        self.physicalNumberKeys = numberKeys
        self.physicalDigits = digits
        self.physicalWarnings = warnings
        self.physicalMessages = messages
        self.physicalWords = words

        self.justNumbersInFrame = None

        self.wasCandidateRead = False

        self.candidateWasFound = False
        self.digitWasFound = False
        self.warningWasFound = False
        self.messageWasFound = False
        self.wordWasFound = False

        self.lstPosLastItemRead = 0



    def uppercase_all_str(self, list):
        for i in range(len(list)):
            list[i] = list[i].upper()
        return list

    def apply_ocr(self, frame):
        reader = easyocr.Reader(['pt'], gpu=True)
        textread = reader.readtext(frame, detail=0)

        textread = self.uppercase_all_str(textread)
        return textread

        # ocr = PaddleOCR(use_angle_cls=True, lang='pt', use_gpu=False)
        # result = ocr.ocr(frame)

        return result

    def apply_ocr_in_frames(self, lstpaths, totalframecount):

        for j in range(totalframecount):
            #jeito inicial
            # readocrinframes = self.apply_ocr('C:\\Users\\eafs3\\Documents\\GitHub\\MonografiaEric\\Resources\\' +
            #                                  'frame' + str(j) + ".jpg")
            # abaixo modo que testei pra poder aplicar OCr em arquivos na pasta antes do resources pois no main, nos
            # meus testes, ta salvando fora da pasta Resources por algum motivo (conferir depois se na app geral ta
            # lendo os arquivos da pasta resources mesmo

            readocrinframes = self.apply_ocr('C:\\Users\\eafs3\\Documents\\GitHub\\MonografiaEric\\Resources\\' +
                                             'frame' + str(j) + ".jpg")

            self.readOcrIndexes.append(readocrinframes)
            self.remove_fake_numbers()
            self.replace_wrong_word()

            print(self.readOcrIndexes)

    def set_federal_candidate_b_read(self, federal_candidate):
        self.federalCandidateBRead = federal_candidate

    def set_number_keys_b_read(self, number_key):
        self.numberKeysBRead = self.physicalNumberKeys[number_key]

    def set_digit_b_read(self, digit):
        self.digitBRead = digit

    def set_warning_b_read(self, warning):
        self.warningBRead = warning

    def set_message_b_read(self, message):
        self.messageBRead = message

    def set_word_b_read(self, word):
        self.wordBRead = word

    def find_federal_candidate(self, candidate):
        for i in self.physicalFederalCandidates:
            if i == candidate:
                self.set_federal_candidate_b_read(i)
                self.candidateWasFound = True
                break

    def find_number_keys(self, candidate):
        for position, item in enumerate(self.physicalFederalCandidates):
            if item == candidate:
                self.set_number_keys_b_read(position)
                break

    def find_numbers_only(self, lst):
        all_b_read = ""
        for i in lst:
            all_b_read = all_b_read+i

        self.justNumbersInFrame = re.sub('[^0-9]', '', all_b_read)

    def find_number_digit(self, lst, digit):
        previous_just_numbers_in_frame = None
        for i in self.physicalDigits:
            if i == digit[0]:
                if self.justNumbersInFrame != None:
                    previous_just_numbers_in_frame = self.justNumbersInFrame
                self.find_numbers_only(lst)
                self.set_digit_b_read(self.justNumbersInFrame)
                self.digitWasFound = True
                break
        if not self.digitWasFound:
            self.set_digit_b_read(None)
            # BEFORE THIS CHANGE, THE ERROR APPEAR: local variable 'previous_just_numbers_in_frame' referenced before assignment
        if self.digitWasFound and self.justNumbersInFrame != None and previous_just_numbers_in_frame != None:
            if len(self.justNumbersInFrame) < len(previous_just_numbers_in_frame):
                self.set_digit_b_read(None)
                
    def find_blank_digit(self, digit):
        pass

    def find_corret_digit(self, digit):
        pass

    def find_confirm_digit(self, digit):
        pass

    def find_warning(self, warning): # talvez isso possa ser irrelevante
        for i in self.physicalWarnings:
            if i == warning:
                self.set_warning_b_read(warning)
                self.warningWasFound = True
                break
        if not self.warningWasFound:
            self.set_warning_b_read(None)

    def find_message(self, message):
        for i in self.physicalMessages:
            if i == message:
                self.set_message_b_read(message)
                self.messageWasFound = True
                break
        if not self.messageWasFound:
            self.set_message_b_read(None)

    def find_word(self, word):
        for i in self.physicalWords:
            if i == word:
                self.set_word_b_read(word)
                self.wordWasFound = True
                break
        if not self.wordWasFound:
            self.set_word_b_read(None)

    def remove_fake_numbers(self):
        last_array_item_number = len(self.readOcrIndexes) - 1
        fake_number_find = False

        for lst_position, lst_item in enumerate(self.readOcrIndexes[last_array_item_number]):
            if lst_item == "ÁUDIO ATIVADO" or lst_item == "AUDIO ATIVADO" or lst_item == "NOME" \
                    or lst_item == "INOME" or lst_item == "INOME:" or lst_item == "NOME:" or lst_item == "VOTO NULO"\
                    or lst_item == "NUMERO ERRADO" or lst_item == "NÚMERO ERRADO":
                finalposition = lst_position + 1
                fake_number_find = True

        if fake_number_find:
            for i in range(finalposition, len(self.readOcrIndexes[last_array_item_number])):
                self.readOcrIndexes[last_array_item_number][i] = self.readOcrIndexes[last_array_item_number][i].\
                    replace(self.readOcrIndexes[last_array_item_number][i], "Fake")

    def replace_wrong_word(self):
        last_array_item_number = len(self.readOcrIndexes) - 1
        fake_word_find = False

        for lst_position, lst_item in enumerate(self.readOcrIndexes[last_array_item_number]):
            if lst_item == "DEPUTADO ESTAQUAL" or lst_item == "DEPUTADO ESTAQDUAL" or lst_item == "DEPUTADO ESTADQUAL":
                finalposition = lst_position
                fake_word_find = True

        if fake_word_find:
            self.readOcrIndexes[last_array_item_number][finalposition] = self.readOcrIndexes[last_array_item_number][finalposition]. \
                replace(self.readOcrIndexes[last_array_item_number][finalposition], "DEPUTADO ESTADUAL")

    def set_all_b_read_array(self, federal_candidate, number_keys, digit, warning, message, word):
        self.allBRead.append([federal_candidate, number_keys, digit, warning, message, word])

    def make_full_b_read_list(self):
        pass

    def create_final_list(self):
         for i in self.readOcrIndexes:
            self.candidateWasFound = False
            self.digitWasFound = False
            self.warningWasFound = False
            self.messageWasFound = False
            self.wordWasFound = False

            for item in i:
                if not self.candidateWasFound:
                    self.find_federal_candidate(item)
                if self.candidateWasFound:
                    self.find_number_keys(self.federalCandidateBRead)
                if not self.digitWasFound:
                    self.find_number_digit(i, item)
                if not self.warningWasFound:
                    self.find_warning(item)
                if not self.messageWasFound:
                    self.find_message(item)
                if not self.wordWasFound:
                    self.find_word(item)

            self.set_all_b_read_array(self.federalCandidateBRead, self.numberKeysBRead, self.digitBRead,
                                      self.warningBRead, self.messageBRead, self.wordBRead)



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

