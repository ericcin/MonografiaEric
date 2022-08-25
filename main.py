from Class.video import *
from Class.ocr import *

testes = Video()
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
ocr.apply_ocr_in_frames(lstPaths, 18)
print(ocr.readOcrIndexes)

print("FIM DAS LEITURAS INICIAIS")
ocr.compare_string()
print(ocr.allBRead)