from datetime import datetime
import re
import tkinter


class Customer():
    date = datetime.now()
    trs_date = f"{date.day}\{date.month}\{date.year}"

    def __init__(self):

        self.name = None
        self.surname = None
        self.id_number = None
        self.account_number = None
        self.insert_money = None
        self.withdraw = None
        self.email = None
        self.telephone = None
        self.password = None

    def get_customer_from_txt(self, id_number):

        with  open('users.txt', 'r', encoding='utf8') as file_name:
            koor = re.search(id_number, file_name.read())
            if koor != None:
                if type(koor.span()) is tuple:
                    file_name.seek(koor.span()[0] + 1)
                    return file_name.readline()
                else:
                    return None

    def set_customer_information(self, id_number):
        customer_text = self.get_customer_from_txt(id_number)
        if customer_text != None:
            customer_text = customer_text.split()
            self.name = customer_text[2]
            self.surname = customer_text[3]
            self.id_number = customer_text[0]
            self.telephone = customer_text[4]
            self.email = customer_text[5]
            self.password = customer_text[1]

            return True
        return False

    # def customer_info(self):
    #     with  open('users.txt', 'r', encoding='utf8') as file_name:
    #         koor = re.search(self.id_number, file_name.read())
    #         file_name.seek(koor.start())
    #         return file_name.readline()

    def change_info(self):
        user_kies = input('Enter A to change Email of Enter B to change Telephone: ')
        if user_kies == "A":
            info = input('Please enter the previous email:')
            with  open('users.txt', 'r+', encoding='utf8') as file_name:
                file_name.seek(re.search(info, file_name.read()).start())
                new_email = (input(f"Please enter the your new email: "))
                patern = r'\w*[@]\w+[.]\D{3}'
                if type(re.search(patern, new_email).span()) is tuple:
                    file_name.write(f'\t{new_email}{" " * 5}')
            return f'Your info updated'
        elif user_kies == "B":
            info = input('Please enter the previous Telephone number:')
            with  open('users.txt', 'r+', encoding='utf-8') as file_name:
                koor = re.search(info, file_name.read())
                file_name.seek(koor.start())
                new_telephone = (input(f"Please enter the your new Telephone number: "))
                if len(info) == 9:
                    file_name.write(f'\t{new_telephone}\t')
            return f'Your info updated'

    @property
    def check_balance(self):  # amount of money(finaly)
        with  open('banktransaction.txt', 'r', encoding='utf-8') as transactions:
            koor = re.search(f'{self.id_number}', transactions.read())
            transactions.seek(koor.end())
            a = transactions.readline().split()
            return (a[-1])

    def add_money(self):
        self.new_balance(int(self.check_balance) + self.insert_money)
        return

    def withdraw_money(self):
        self.new_balance(int(self.check_balance) + self.withdraw)
        return

    def new_balance(self,amount):
        # dosya ya degisen hesap bakiyesini eklemek icin kullanilir
        with open('banktransaction.txt', 'r+') as transactions:
            customer_transaction_lines_list = transactions.readlines()
            print("test")
            # if self.id_number in str(customer_transaction_lines_list):
            for customer_transaction_line in customer_transaction_lines_list:
                print("test1")
                if self.id_number in customer_transaction_line:
                    index = customer_transaction_lines_list.index(customer_transaction_line)
                    customer_transaction_lines_list[index] = str(customer_transaction_line).strip('\n') + " Balance " + str(amount) + '\n'
            print(customer_transaction_lines_list[0])
            print(customer_transaction_lines_list[1])
            transactions.seek(0)

            transactions.writelines(customer_transaction_lines_list)


            # if type(koor.span()) is tuple:
            # transactions.seek(koor.span()[0] + 1)
            # return transactions.readline()


class Bank:
    file_name = 0
    def __init__(self):
        pass

    def money_transfer(self,sender_id,receiver_id, amount):
        sender_customer_1 = Customer()
        sender_customer_1.set_customer_information(sender_id)
        receiver_customer_2 = Customer()
        if receiver_customer_2.set_customer_information(receiver_id) and self.is_avaliable(sender_id, amount):
            sender_customer_1.withdraw = -amount
            sender_customer_1.withdraw_money()
            receiver_customer_2.insert_money = amount
            receiver_customer_2.add_money()



    def login_id_password_check(self, id, password):
        customer_1 = Customer()
        if customer_1.set_customer_information(id) == True:
            if customer_1.password == password:
                return True
            else:
                return False


    def is_user(self, id):
        customer_1 = Customer()
        if customer_1.set_customer_information(id) == True:
            return True
        else:
            return False


    def is_avaliable(self,id, amount):
        customer_1 = Customer()
        if customer_1.set_customer_information(id) == True:
            if int(customer_1.check_balance) >= amount:
                return True
            else:
                return False
        else:
            return False

obje = Customer()
# print(obje.get_customer_from_txt('12345699999'))
obje.set_customer_information('12345699999')
print(obje.name)
print(obje.surname)
print(obje.password)
print(obje.id_number)
print(obje.email)
print(obje.telephone)
# obje.insert_money = -1000
# obje.new_balance()
# print(obje.check_balance)

banka_1 = Bank()

print(banka_1.login_id_password_check('12345699999', "1235"))
print(banka_1.login_id_password_check('12345699999', "6789"))
print(banka_1.is_avaliable('12345699999', 5000))
print(banka_1.login_id_password_check('12345699900', "1235"))
print(banka_1.login_id_password_check('12345699999', "6789"))

banka_1.money_transfer("12345699999","12345678910",1000)
