import easyocr

def apply_ocr(frame):
    reader = easyocr.Reader(['pt', 'en'])
    textread = reader.readtext(frame, detail=0)
    return str(textread)

class Ocr:
    def __init__(self):
        self.readOcrIndexes = []

    def apply_ocr_in_frames(self, lstpaths, totalframecount):
        for i in range(len(lstpaths)):
            self.readOcrIndexes.append(i)
            for j in range(totalframecount):
                readocrinframes = apply_ocr(
                    'C:\\Users\\eafs3\\Documents\\GitHub\\MonografiaEric\\Resources\\' + 'frame' + str(j) + ".jpg")
                self.readOcrIndexes.append(readocrinframes)
