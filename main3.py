class string:
    def __init__(self):
        self.vowels=0
        self.spaces=0
        self.consonants=0
        self.uppercase=0
        self.lowercase=0
        self.string=str(input("enter the string: "))
    def count_uppercase(self):
        for letter in self.string:
            if(letter.isupper()):
                self.uppercase+=1
    def count_lowercase(self):
        for letter in self.string:
            if(letter.islower()):
                self.lowercase+=1
    def count_vowels(self):
        for letter in self.string:
            if(letter in ('a','e','i','o','u')):
                self.vowels+=1
            elif(letter in ('A','E','I','O','U')):
                self.vowels+=1
    def count_spaces(self):
        for letter in self.string:
            if(letter ==' '):
                self.spaces+=1
    def count_consonants(self):
        for letter in self.string:
            if(letter not in('a','e','i','o','u','A','E','I','O','U',)):
                self.consonants+=1
    def compute_stat(self):
        self.count_uppercase()
        self.count_lowercase()
        self.count_vowels()
        self.count_spaces()
        self.count_consonants()
    def show_stat(self):
        print("vowels:%d"%self.vowels)
        print("consonants:%d"%self.consonants)
        print("spaces:%d"%self.spaces)
        print("uppercase:%d"%self.uppercase)
        print("lowercase:%d"%self.lowercase)
s=string()
s.compute_stat()
s.show_stat()