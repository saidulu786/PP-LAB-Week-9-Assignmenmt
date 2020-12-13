class store:
    __item_code=[]
    __price=[]
    def get_data(self):
        for i in range(5):
            self.__item_code.append(int(input("enter the code of item: ")))
            self.__price.append(int(input("enter the price: ")))
    def display_data(self):
        print("item code \t price")
        for i in range (5):
            print(self.__item_code[i],"\t\t",self.__price[i])
    def calculate_bill(self,quant):
        total_amount=0
        for i in range(5):
            total_amount=total_amount+self.__price[i]*quant[i]
        print("*****bill*****")
        print("item \t price \t quantity \t subtotal")
        for i in range(5):
            print(self.__item_code[i],"\t",self.__price[i],"\t",quant[i],"\t",quant[i]*self.__price[i])
        print("total= ",total_amount)
s=store()
s.get_data()
s.display_data()
q=[]
print("enter the quqntity of each item")
for i in range(5):
   q.append(int(input()))
s.calculate_bill(q)