class book:
    def __init__(self):
        self.title=''
        self.author=''
        self.price=0
    def read(self):
        self.title=input("enter book title: ")
        self.author=input("enter book author: ")
        self.price=float(input("enter book price: "))
    def display(self):
        print("title : ",self.title)
        print("author : ",self.author)
        print("price : ",self.price)
my_books=[]
ch='y'
while(ch=='y'):
    print('''1. add new book\n 2.display books''')
    choice=int(input("enter choice: "))
    if(choice==1):
        book=book()
        book.read()
        my_books.append(book)
    elif(choice==2):
        for i in my_books:
            i.display()
    else:
        print("invalid choice")
    ch=input("do you want to continue..")
print("bye!")