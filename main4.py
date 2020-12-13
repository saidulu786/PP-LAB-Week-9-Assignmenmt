import datetime
class product:
    def __init__(self):
        self.manufacture=datetime.datetime.strptime(input("enter manufacturing date(mm/dd/yyyy): "),"%m%d%y")
        self.expiry=datetime.datetime.strptime(input("enter expiry date(mm/dd/yyyy): "),"%m/%d/%y")
    def time_to_expire(self):
        today=datetime.datetime.now()
        if(today>self.expiry):
            print("product has already expired")
        else:
            time_left=self.expiry.date()-datetime.datetime.now().date()
            print("timeleft:",time_left)
    def show(self):
        print("expiry: ",self.expiry)
        print("manufacturing:",self.manufacture)
x=product()
x.time_to_expire()