import easyocr

from Class.video import Video
from Class.ocr import Ocr

testes = Video()
ocr = Ocr()

testes.open_file()
print(testes.lstPaths)
testes.lst_frames()
print(testes.imageIndexes)
print(len(testes.imageIndexes[0]))

testes.save_frames()
ocr.apply_ocr_in_frames(testes.lstPaths, testes.totalFrameCount)
print(ocr.readOcrIndexes)
# testes.apply_ocr_in_frames()
# print(testes.readOcrIndexes)

