import urllib2
import json

class Translator():
    def getTranslatedWord(self,keyword):
        translatorAPIKey="trnsl.1.1.20161024T195702Z.b306b5c031a2ac5e.12c39e368a8b60f0c7d74ed76e03b3699c2fa1a1"
        keyword=keyword.encode('utf-8')
        try:
            translateResponse = urllib2.urlopen("https://translate.yandex.net/api/v1.5/tr.json/translate?key="+translatorAPIKey+"&text="+keyword+"&lang=es-en", timeout=5).read()
            JSONTranslateResponse = json.loads(translateResponse)
            translatedKeyword = JSONTranslateResponse['text'][0]
        except urllib2.URLError, e:
            translatedKeyword = ''
        return translatedKeyword