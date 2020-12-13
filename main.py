
class student:
    __marks=[]
    def set_data(self,r,n,m1,m2,m3):
        student.__rollno=r
        student.__name=n
        student.__marks.append(m1)
        student.__marks.append(m2)
        student.__marks.append(m3)
    def display_data(self):
        print("student details")
        print("roll number :",student.__rollno)
        print("name:",student.__name)
        print("marks:",self.total())
    def total(self):
        m=student.__marks
        return m[0]+m[1]+m[2]

r=int(input("enter the roll number: "))
n=input("enter the name: ")
m1=int(input("enter the first subject marks: "))
m2=int(input("enter the second subject marks: "))
m3=int(input("enter the third subject marks: "))
s1=student()
s1.set_data(r,n,m1,m2,m3)
s1.display_data()