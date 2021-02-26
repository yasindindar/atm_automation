from datetime import date, datetime
class Customer():
    trs_date=datetime .now()
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
            list=[ i.strip()  for i in lines[0:6]]
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
     
            
   
            
            
            
                
obje=Customer(name="Ahmet",surname="Erkek",id_number="12345678910",account_number="5555555555",insert_money=0,withdraw=1000)
#print(obje.check_balance())
print(obje.__str__())
print(obje.new_balance())
#print(obje.add_money())