from Class.video import *
from Class.ocr import *

# testes = Video()
video = Video()
ocr = Ocr()

# testes.open_file()
# print(testes.lstPaths)
# testes.lst_frames()
# print(testes.imageIndexes)
# print(len(testes.imageIndexes[0]))

# testes.save_frames()

# ocr.apply_ocr_in_frames(testes.lstPaths, testes.totalFrameCount)
# print(ocr.readOcrIndexes)

#CÓDIGO ANTERIOR SALVANDO FRAMES DE VIDEO


lstPaths = ['1']

for i in range(18):
    # patch = 'C:\\Users\\eafs3\\Documents\\GitHub\\MonografiaEric\\Resources\\' + 'frame' + str(i) + '.jpg'
    # binaryimg = testes.binary(patch)
    # cv2.imwrite("frame%d.jpg" % i, binaryimg)

    patch = 'C:\\Users\\eafs3\\Documents\\GitHub\\MonografiaEric\\Resources\\' + 'frame' + str(i) + '.jpg'
    video.binary(patch)
    video.remove_vertical_lines()
    video.remove_horizontal_lines()
    video.repair_kernel()
    finalFrame = video.finish_ip_proccess()

    cv2.imwrite("frame%d.jpg" % i, finalFrame)

ocr.apply_ocr_in_frames(lstPaths, 18)
print(ocr.readOcrIndexes)

print("FIM DAS LEITURAS INICIAIS")
ocr.compare_string()
print(ocr.allBRead)