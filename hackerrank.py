from datetime import date, datetime
class Customer():
    trs_date=datetime .now()
    def __init__(self,id_number):
        with open(f'{self.id_number}.txt', 'r') as self.file_name:
            lines = self.file_name.readlines()
            liste1 = [i.strip() for i in lines[:]]
        liste1
        self.name = liste1[0]
        self.surname = liste1[1]
        self.id_number=liste1[2]
        self.balance = liste1[-1]
        # self.file_name=(self.id_number[:3])+(self.account_number[:3])

    def __init__(self,name,surname,id_number,account_number,insert_money,withdraw):
        self.name=name
        self.surname=surname
        self.id_number=id_number
        self.account_number=account_number
        self.insert_money=insert_money
        self.withdraw=withdraw
        self.file_name=(self.id_number[:3])+(self.account_number[:3])

    def customer_info(self): 
        with  open(f'{self.id_number}.txt','r') as self.file_name:           
            lines=self.file_name.readlines()
            list=[ i.strip()  for i in lines[1:6]]
            return f'{(" ".join (list))}'

    @property
    def check_balance(self): #amount of money(finaly) 
        with  open(f'{self.id_number}.txt','r') as self.file_name:
            lines=self.file_name.readlines()
            list=[ i.strip()  for i in lines[-1:]]
            for i in list:
                return (i)
    def new_balance(self):        
        with  open(f'{self.id_number}.txt','a+') as self.file_name:  #dosya ya degisen hesap bakiyesini eklemek icin kullanilir
            self.file_name.write( f'\n{self.add_money()}')
            return f"Balance updated...{self.check_balance} euro"
    def add_money(self): 
        if self.insert_money>0:
            return int(self.check_balance)+(self.insert_money)
        elif self.withdraw>0:
            return int(self.check_balance)-(self.withdraw)
    def __str__(self):        
        return f"{self.customer_info()}\nBalance:{self.check_balance}euro"       

class Bank():
    file_name = 0
    def __init__(self):
        pass

    def login_id_password_check(self, id, password):
        with  open(f'{id}.txt','r') as self.file_name:
            lines=self.file_name.readlines()
            list=[ i.strip()  for i in lines[:]]
            print(list)
            # We checked both user id and password.
            if list[0] == password:
                return True
            else:
                return False


    def is_user(self, id):
        with open('Credentials.txt', 'r')as self.file_name:
            lines = self.file_name.readlines()
            list = [i.strip() for i in lines[:]]
            for i in list:
                # We need separated user id and password with split.
                new_list = i.split()
                if new_list[0] == id:
                    return True
            return False


    def is_avaliable(self,customer, amount):
        if int(customer.check_balance) >= amount:
            return True
        else:
            return False


obje=Customer(name="Ahmet",surname="Erkek",id_number="12345678910",account_number="5555555555",insert_money=0,withdraw=1000)
#print(obje.check_balance())
newbank = Bank()
print(newbank.login_id_password_check(12345678910,"password"))
print(newbank.is_avaliable(obje,1000))
print(obje.__str__())
print(obje.new_balance())
print(obje.customer_info())

#print(obje.add_money())

