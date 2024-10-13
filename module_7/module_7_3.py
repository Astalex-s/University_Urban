import re


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            list_words = []
            with open(i, encoding='utf-8') as file:
                for j in file:
                    j = re.sub("[,.=!?;:-]", ' ', j).lower().split()
                    list_words += j
                all_words.update({i: list_words})
        return all_words

    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                result[name] = words.index(word.lower()) + 1
        return result

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            count = words.count(word.lower())
            if count > 0:
                result[name] = count
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
