from plyer import filechooser
import cv2


class Video:
    def __init__(self):
        self.lstPaths = []
        self.imageIndexes = []
        self.totalFrameCount = []
        self.pathOfFrames = None

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

        self.pathOfFrames = folderPath[0:56]
        self.lstPaths = lstPaths

    def lst_frames(self):
        for i in range (len(self.lstPaths)):
            print("arquivo"+str(i))
            videoframes = cv2.VideoCapture(self.lstPaths[i])
            self.imageIndexes.append(videoframes.read())

    def binary(self, frame):
        originalImage = cv2.imread(frame)
        grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

        (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

        return blackAndWhiteImage

    def save_frames(self):
        vidcap = cv2.VideoCapture(self.lstPaths[0])
        vidcap.set(3, 1280)
        vidcap.set(4, 720)
        self.totalFrameCount = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        success, image = vidcap.read()
        count = 0

        for i in range(self.totalFrameCount):
            cv2.imwrite("frame"+str(count)+".jpg", image)
            binaryimg = self.binary('C:\\Users\\eafs3\\Documents\\GitHub\\MonografiaEric\\Resources\\' + 'frame' + str(i) + ".jpg")
            cv2.imwrite("frame%d.jpg" % count, binaryimg)
            success, image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1

        vidcap.release()
