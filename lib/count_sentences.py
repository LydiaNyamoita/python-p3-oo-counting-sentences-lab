#!/usr/bin/env python3

class MyString:
    
    def __init__(self, value = ""):
        self.value = value


    def set_value (self, value):
        if type(value) == str:
            self._value = value
        else: 
            print("Value must be a string")

    def is_sentence (self):
        if self.value.endswith("."):
            return True
        else:
            return False
    def is_question(self):
        if self.value.endswith("?"):
            return True
        else:
            return False

    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        else:
            return False
    

    def count_sentences(self):
        value = self.value
        for punc in ['!','?']:
            value = value.replace(punc, '.')

        sentences = [s for s in value.split('.') if s]

        return len(sentences)
      


string = MyString()
string.value = "This is a string! It has three sentences. Right? No way! Yes was. got it! No can do?"
print(string.count_sentences())
