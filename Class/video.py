from plyer import filechooser
import cv2


class Video:
    def __init__(self):
        self.lstPaths = []
        self.imageIndexes = []
        self.totalFrameCount = []
        self.pathOfFrames = None
        self.frameWEdgeRemoved = None
        self.threshFrame = None
        self.repairedKernelFrame = None
        self.preResultFrame = None
        self.frameBGR = None

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

    # def binary(self, frame):
    #     originalImage = cv2.imread(frame)
    #     grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    #
    #     (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    #
    #     return blackAndWhiteImage

    def binary(self, frame):
        originalImage = cv2.imread(frame)
        self.frameWEdgeRemoved = originalImage.copy()
        gray = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
        gray = cv2.blur(gray, (5, 5))
        self.threshFrame = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    def remove_vertical_lines(self):
        vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 40))
        remove_vertical = cv2.morphologyEx(self.threshFrame, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
        cnts = cv2.findContours(remove_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            cv2.drawContours(self.frameWEdgeRemoved, [c], -1, (255, 255, 255), 15)

    def remove_horizontal_lines(self):
        horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))
        remove_horizontal = cv2.morphologyEx(self.threshFrame, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
        cnts = cv2.findContours(remove_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            cv2.drawContours(self.frameWEdgeRemoved, [c], -1, (255, 255, 255), 5)

    def repair_kernel(self):
        self.repairedKernelFrame = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        removed = 255 - self.frameWEdgeRemoved
        dilate = cv2.dilate(removed, self.repairedKernelFrame, iterations=5)
        dilate = cv2.cvtColor(dilate, cv2.COLOR_BGR2GRAY)
        self.preResultFrame = cv2.bitwise_and(dilate, self.threshFrame)

    def finish_ip_proccess(self):
        result = cv2.morphologyEx(self.preResultFrame, cv2.MORPH_CLOSE, self.repairedKernelFrame, iterations=5)
        final = cv2.bitwise_and(result, self.threshFrame)

        invert_final = 255 - final

        dim = (1280, 720)

        invert_final = cv2.resize(invert_final, dim, cv2.INTER_AREA)
        invert_final = cv2.GaussianBlur(invert_final, (5, 5), 0)

        return invert_final

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
