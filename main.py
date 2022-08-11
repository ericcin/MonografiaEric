from plyer import filechooser
import cv2
import easyocr


def apply_ocr(frame):
    reader = easyocr.Reader(['pt', 'en'])
    textread = reader.readtext(frame, detail=0)
    return str(textread)

class Videos:
    def __init__(self, lstfiles):
        self.lstFiles = lstfiles
        self.imageIndexes = []
        self.readOcrIndexes = []
        self.totalFrameCount = []

    def open_file(self):
        pathOpen = filechooser.open_file(title="Selecione uma imagem ou vídeo", multiple=True)

        lstFiles = []
        folderPath = pathOpen[0]

        for i in range(len(pathOpen)):
            lstFiles.append(pathOpen[i])

        barra = "\\"
        lst = []

        for pos, char in enumerate(folderPath):
            if char == barra:
                lst.append(pos)

        self.lstFiles = lstFiles

    def lst_frames(self):
        for i in range (len(self.lstFiles)):
            print("arquivo"+str(i))
            videoframes = cv2.VideoCapture(self.lstFiles[i])
            self.imageIndexes.append(videoframes.read())

    def save_frames(self):
        vidcap = cv2.VideoCapture(self.lstFiles[0])
        self.totalFrameCount = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        success, image = vidcap.read()
        count = 0

        for i in range(self.totalFrameCount):
            cv2.imwrite("frame%d.jpg" % count, image)
            sucecss, image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1

    def apply_ocr_in_frames(self):
        for i in range(len(self.lstFiles)):
            self.readOcrIndexes.append(i)
            for j in range(self.totalFrameCount):
                readocrinframes = apply_ocr('C:\\Users\\eafs3\\Documents\\GitHub\\MonografiaEric\\Resources\\'+'frame'+str(j)+".jpg")
                self.readOcrIndexes.append(readocrinframes)

    def compare_chars(self):
        pass

    def save_data_in_bd(self):
        pass

testes = Videos(None)

testes.open_file()
print(testes.lstFiles[0])
# testes.lst_frames()
# print(testes.imageIndexes)
# print(len(testes.imageIndexes[0]))

testes.save_frames()
testes.apply_ocr_in_frames()
print(testes.readOcrIndexes)
# testes.apply_ocr_in_frames()
# print(testes.readOcrIndexes)

