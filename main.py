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
video.lst_frames()
print(video.imageIndexes)
print(len(video.imageIndexes[0]))

video.save_frames()

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