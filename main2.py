class numbers:
    def __init__(self):
        self.values = []
    def find_max(self):
        max=''
        for i in self.values:
            if(i>max):
                max=i
        print('max element is : %r' %max)
    def insert_element(self):
        value=input("enter the value: ")
        self.values.append(value)
        x=numbers()
        ch='y'
        while(ch == 'y'):
            x.insert_element()
            ch=input("do you wish to enetr more elements?")
        x.find_max()