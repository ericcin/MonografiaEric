from Class.video import *
from Class.ocr import *

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

