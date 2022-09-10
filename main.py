import easyocr.config

from Class.video import *
#from Class.ocr import *
#from Class.urna import Urna
import time

start_time = time.time()

# testes = Video()
video = Video()

video.open_file()
print(video.lstPaths)

for i in range(len(video.lstPaths)):
    video.pathOfFrames = None
    video.frameWEdgeRemoved = None
    video.threshFrame = None
    video.repairedKernelFrame = None
    video.preResultFrame = None
    video.imageIndexes = []
    video.totalFrameCount = []

    video.urna.currentCandidate = None
    video.urna.currentNumber = None
    video.urna.corrigeWasPressed = False
    video.urna.confirmaWasPressed = False
    video.urna.currentDigit = None
    video.urna.currentFrame = None
    video.urna.changeInScreen = False
    video.urna.timeBetweenFrames = None

    video.urna.ocr.readOcrIndexes = []
    video.urna.ocr.federalCandidateBRead = ""
    video.urna.ocr.numberKeysBRead = 0
    video.urna.ocr.warningBRead = ""
    video.urna.ocr.digitBRead = ""
    video.urna.ocr.messageBRead = ""
    video.urna.ocr.wordBRead = ""
    video.urna.ocr.allBRead = []
    video.urna.ocr.justNumbersInFrame = None
    video.urna.ocr.candidateWasFound = False
    video.urna.ocr.digitWasFound = False
    video.urna.ocr.warningWasFound = False
    video.urna.ocr.messageWasFound = False
    video.urna.ocr.wordWasFound = False

    video.lst_frames(i)

    print(video.imageIndexes)
    print(len(video.imageIndexes[0]))

    video.save_frames(i)

    video.urna.ocr.apply_ocr_in_frames(video.lstPaths, video.totalFrameCount)
    print(video.urna.ocr.readOcrIndexes)

    video.urna.ocr.create_final_list()
    print(video.urna.ocr.allBRead)

    print ("time elapsed: {:.2f}s".format(time.time() - start_time))

    video.urna.set_digits(video.urna.ocr.allBRead)

video.urna.save_excel_table()

#CÓDIGO AUTOMATIZADO ACIMA

#CÓDIGO MANUAL ABAIXO
#lstPaths = ['1']

#CODIGO MANUAL ABAIXO
# lstPaths = ['1']
#
# for i in range(18):
#     # patch = 'C:\\Users\\eafs3
#     # \\Documents\\GitHub\\MonografiaEric\\Resources\\' + 'frame' + str(i) + '.jpg'
#     # binaryimg = testes.binary(patch)
#     # cv2.imwrite("frame%d.jpg" % i, binaryimg)
#
#     patch = 'C:\\Users\\eafs3\\Documents\\GitHub\\MonografiaEric\\Resources\\' + 'frame' + str(i) + '.jpg'
#     video.binary(patch)
#     video.remove_vertical_lines()
#     video.remove_horizontal_lines()
#     video.repair_kernel()
#     finalFrame = video.finish_ip_proccess()
#
#     cv2.imwrite("frame%d.jpg" % i, finalFrame)