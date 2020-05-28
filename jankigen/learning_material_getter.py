from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *
from jamdict import Jamdict
from jamdict.jmdict import JMDEntry
from jamdict.jmdict import Sense
from jamdict.jmdict import SenseGloss
from jamdict.jmdict import KanaForm
import csv


class LearningMaterialGetter:
    def __init__(self, user_dict="", user_dict_en=""):
        self.dict_en = {}
        self.jmd = Jamdict()
        if user_dict != "":
            self.tokenizer = Tokenizer(user_dict, udic_type="simpledic", udic_enc="utf8")
        else:
            self.tokenizer = Tokenizer()
        self.token_filters = [POSStopFilter(['記号', '助詞']), TokenCountFilter(att='base_form')]
        if user_dict_en != "":
            with open(user_dict_en, newline='', encoding="utf-8") as csvfile:
                dic_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in dic_reader:
                    if len(row) >= 3:
                        self.dict_en[row[0]] = {
                            'reading': row[1],
                            'meaning': row[2]
                        }

    def tokenize(self, text):
        a = Analyzer(tokenizer=self.tokenizer, token_filters=self.token_filters)
        return a.analyze(text)

    def getDictionaryInfos(self, pairs):
        infos = []
        for token, v in pairs:
            match = re.match("[\u30A1-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]", token)
            if match:
                dic_info = self.jmd.lookup(token)
                if len(dic_info.entries) > 0 or len(dic_info.chars) > 0:
                    # Inject custom dictionary meaning
                    if len(dic_info.entries) == 0 and token in self.dict_en:
                        meaning = self.dict_en[token]['meaning']
                        reading = self.dict_en[token]['reading']
                        d = JMDEntry()
                        d.senses = [Sense()]
                        d.kana_forms = [KanaForm()]
                        d.kana_forms[0].text = reading
                        d.senses[0].gloss.append(SenseGloss("", "", meaning))
                        dic_info.entries.append(d)
                    infos.append((token, dic_info))

        return infos
