from plyer import filechooser
import cv2

class Video:
    def __init__(self):
        self.lstPaths = []
        self.imageIndexes = []
        self.totalFrameCount = []

    def open_file(self):
        pathOpen = filechooser.open_file(title="Selecione uma imagem ou vídeo", multiple=True)

        lstPaths = []
        folderPath = pathOpen[0]

        for i in range(len(pathOpen)):
            lstPaths.append(pathOpen[i])

        barra = "\\"
        lst = []

        for pos, char in enumerate(folderPath):
            if char == barra:
                lst.append(pos)

        self.lstPaths = lstPaths

    def lst_frames(self):
        for i in range (len(self.lstPaths)):
            print("arquivo"+str(i))
            videoframes = cv2.VideoCapture(self.lstPaths[i])
            self.imageIndexes.append(videoframes.read())

    def save_frames(self):
        vidcap = cv2.VideoCapture(self.lstPaths[0])
        self.totalFrameCount = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        success, image = vidcap.read()
        count = 0

        for i in range(self.totalFrameCount):
            cv2.imwrite("frame%d.jpg" % count, image)
            sucecss, image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1

    def compare_chars(self):
        pass

    def save_data_in_bd(self):
        pass