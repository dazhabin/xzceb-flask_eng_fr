from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    #write the code here
    frenchText = MyMemoryTranslator(source='english', target='french').translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    englishText = MyMemoryTranslator(source='french', target='english').translate(frenchText)
    return englishText
