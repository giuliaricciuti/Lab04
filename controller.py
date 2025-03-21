import time
import flet as ft
import model as md

class SpellChecker:



    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None

    def handleChangeLan(self, e):
        language = e.control.value
        self._view.setTxtout(f"hai scelto {language}")
        self._view.page.update()

    def handleChangeSearch(self, e):
        search = e.control.value
        self._view.setTxtout2(f"hai scelto {search}")
        self._view.page.update()

    def handleSpellCheck(self, e):
        txtIn = self._view.getFrase()
        language = self._view.getLanguage()
        modality = self._view.getSearch()
        if txtIn=="" or modality=="" or language=="":
            self._view.showWarning()
        else:
            errate= self.handleSentence(txtIn, language, modality)[0]
            time= self.handleSentence(txtIn, language, modality)[1]
            self._view.showResult(txtIn, errate, time)


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text