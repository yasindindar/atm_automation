from tkinter import *
from Customer import *
import tkinter as tk


class ATM_GUI():
    def __init__(self, root):

        self.root = root
        self.user_id = 0

        self.container_frame = LabelFrame(self.root, border=0)
        self.container_frame.grid(row=1, column=1, columnspan=10, rowspan=10)

        self.user_id_entry_label = Label(self.container_frame, text=' User ID ')
        self.user_id_entry_label.grid(row=2, column=2, sticky=W)
        self.username_entry = Entry(self.container_frame)
        self.username_entry.grid(row=2, column=3)

        self.password_entry_label = Label(self.container_frame, text=' Password ')
        self.password_entry_label.grid(row=3, column=2, sticky=W)
        self.password_entry = Entry(self.container_frame, show='*')
        self.password_entry.grid(row=3, column=3)

        self.receiver_id_entry_label = Label(self.container_frame, text=' Receiver ID ')
        self.receiver_id_entry_label.grid(row=2, column=2, sticky=W)
        self.receiver_id_entry = Entry(self.container_frame)
        self.receiver_id_entry.grid(row=2, column=3)

        self.amount_of_transfer_entry_label = Label(self.container_frame, text=' Amount of Transfer ')
        self.amount_of_transfer_entry_label.grid(row=2, column=2, sticky=W)
        self.amount_of_transfer_entry = Entry(self.container_frame)
        self.amount_of_transfer_entry.grid(row=2, column=3)

        self.telephone_entry_label = Label(self.container_frame, text=' New Telephone')
        self.telephone_entry_label.grid(row=2, column=2, sticky=W)
        self.telephone_entry = Entry(self.container_frame)
        self.telephone_entry.grid(row=2, column=3)

        self.email_entry_label = Label(self.container_frame, text=' New E-mail ')
        self.email_entry_label.grid(row=2, column=2, sticky=W)
        self.email_entry = Entry(self.container_frame)
        self.email_entry.grid(row=2, column=3)

        # self.home_frame_label = tk.Label(self.container_frame)
        # self.home_frame_label.grid()


        self.withdraw_amount_label = Label(self.container_frame, text=' Enter amount ')
        self.withdraw_amount_label.grid(row=3, column=2, sticky=W)
        self.withdraw_entry = Entry(self.container_frame)
        self.withdraw_entry.grid(row=3, column=3)

        self.insert_money_amount_label = Label(self.container_frame, text=' Enter amount ')
        self.insert_money_amount_label.grid(row=3, column=2, sticky=W)
        self.insert_money_entry = Entry(self.container_frame)
        self.insert_money_entry.grid(row=3, column=3)

        self.check_balance_btn = tk.Button(self.container_frame, text='CHECK BALANCE', command=self.show_check_balance, width=20, height=2)
        self.check_balance_btn.grid(row=1, column=3)
        self.check_balance_label = Label(self.container_frame)
        self.withdraw_btn = tk.Button(self.container_frame, text='WITHDRAW', command=self.withdraw_frame_show, width=20, height=2)
        self.withdraw_btn.grid(row=3, column=3)
        self.insert_money_btn = tk.Button(self.container_frame, text='INSERT MONEY', command=self.insert_money_frame_show, width=20, height=2)
        self.insert_money_btn.grid(row=5, column=3)
        self.transfer_money_btn = tk.Button(self.container_frame, text='TRANSFER MONEY', command=self.show_transfer_money_frame, width=20, height=2)
        self.transfer_money_btn.grid(row=1, column=6)
        # self.change_info_btn = tk.Button(self.container_frame, text='CHANGE INFO', command=self.show_change_info_frame, width=20, height=2)
        # self.change_info_btn.grid(row=3, column=6)
        self.back_btn = tk.Button(self.container_frame, text='BACK', command=self.back_performer, width=20, height=2)
        self.back_btn.grid(row=5, column=6)
        self.exit_btn = tk.Button(self.container_frame, text='EXIT', command=self.exit_performer, width=20, height=2)
        self.exit_btn.grid(row=5, column=6)
        self.ok_btn = tk.Button(self.container_frame, text='OK', command=None, width=20, height=2)
        self.ok_btn.grid(row=5, column=6)
        self.login_btn = tk.Button(self.container_frame, text='LOGIN', command=self.login_user)
        self.login_btn.grid(row=4, column=3)
        self.message_label = Label(self.container_frame, text="Wrong Entry", fg="red")


        self.show_login_page()

    def hide_all_container_frame_items(self):

        self.user_id_entry_label.grid_forget()
        self.username_entry.grid_forget()
        self.password_entry.grid_forget()
        self.password_entry_label.grid_forget()
        self.login_btn.grid_forget()
        self.withdraw_amount_label.grid_forget()
        self.withdraw_entry.grid_forget()
        self.check_balance_btn.grid_forget()
        self.check_balance_label.grid_forget()
        self.withdraw_btn.grid_forget()
        self.insert_money_btn.grid_forget()
        self.transfer_money_btn.grid_forget()
        # self.change_info_btn.grid_forget()
        self.back_btn.grid_forget()
        self.exit_btn.grid_forget()
        self.ok_btn.grid_forget()
        self.insert_money_amount_label.grid_forget()
        self.insert_money_entry.grid_forget()
        self.receiver_id_entry_label.grid_forget()
        self.receiver_id_entry.grid_forget()
        self.amount_of_transfer_entry_label.grid_forget()
        self.amount_of_transfer_entry.grid_forget()
        self.message_label.grid_forget()
        self.telephone_entry.grid_forget()
        self.telephone_entry_label.grid_forget()
        self.email_entry.grid_forget()
        self.email_entry_label.grid_forget()

    def show_change_info_frame(self):
        self.hide_all_container_frame_items()
        self.telephone_entry_label.grid(row=1, column=1, sticky=W)
        self.telephone_entry.grid(row=1, column=2)
        self.email_entry_label.grid(row=2, column=1, sticky=W)
        self.email_entry.grid(row=2, column=2)
        self.back_btn.grid(row=4, column=2)
        self.exit_btn.grid(row=5, column=2)
        self.ok_btn.grid(row=3, column=2)
        self.ok_btn.config(command=self.telephone_email_performer)

    def withdraw_frame_show(self):
        self.hide_all_container_frame_items()
        self.withdraw_amount_label.grid(row=1, column=1, sticky=W)
        self.withdraw_entry.grid(row=1, column=2)
        self.ok_btn.config(command=self.withdraw_money)
        self.ok_btn.grid(row=2, column=2)
        self.back_btn.grid(row=3, column=4)
        self.exit_btn.grid(row=4, column=4)

    def insert_money_frame_show(self):
        self.hide_all_container_frame_items()
        self.insert_money_amount_label.grid(row=1, column=1, sticky=W)
        self.insert_money_entry.grid(row=1, column=2)
        self.ok_btn.config(command=self.insert_money)
        self.ok_btn.grid(row=2, column=2)
        self.back_btn.grid(row=3, column=4)
        self.exit_btn.grid(row=4, column=4)



    def show_login_page(self):
        self.hide_all_container_frame_items()
        self.user_id_entry_label.grid(row=1, column=1)
        self.username_entry.grid(row=1, column=2)
        self.password_entry.grid(row=2, column=2)
        self.password_entry_label.grid(row=2, column=1)
        self.login_btn.grid(row=4, column=3)

    def show_transfer_money_frame(self):
        self.hide_all_container_frame_items()
        self.receiver_id_entry_label.grid(row=1, column=1, sticky=W)
        self.receiver_id_entry.grid(row=1, column=3)
        self.amount_of_transfer_entry_label.grid(row=2, column=1, sticky=W)
        self.amount_of_transfer_entry.grid(row=2, column=3)
        self.ok_btn.config(command=self.transfer_money_performer)
        self.ok_btn.grid(row=3, column=3)
        self.back_btn.grid(row=4, column=3)
        self.exit_btn.grid(row=5, column=3)



    def show_home_page(self):
        self.hide_all_container_frame_items()
        self.check_balance_btn.grid(row=1, column=1)
        self.withdraw_btn.grid(row=2, column=1)
        self.insert_money_btn.grid(row=2, column=2)
        self.transfer_money_btn.grid(row=1, column=2)
        # self.change_info_btn.grid(row=2, column=2)
        self.exit_btn.grid(row=4, column=2)


    def exit_performer(self):
        self.container_frame.quit()

    def telephone_email_performer(self):
        customer_0 = Customer()
        customer_0.set_customer_information(self.user_id)
        if self.email_entry.get() != "":
            customer_0.new_email = self.email_entry.get()
            customer_0.change_email()
        if self.telephone_entry.get() != "":
            customer_0.new_telephone = self.telephone_entry.get()
            customer_0.change_telephone()



    def withdraw_money(self):
        customer_0 = Customer()
        customer_0.set_customer_information(self.user_id)
        customer_0.withdraw = self.withdraw_entry.get()
        customer_0.withdraw_money()

    def login_user(self):
        print("login user method")
        user_id = "12345678910"
        password = "1235"
        check_login_user = Authentication()
        if check_login_user.login_user(self.username_entry.get(), self.password_entry.get()) == True:
            self.user_id = user_id
            self.message_label.grid_forget()
            self.show_home_page()
        else:
            self.message_label = Label(self.container_frame, text = "Wrong Entry", fg="red")
            self.message_label.grid(row=5, column=3)

    def insert_money(self):
        customer_0 = Customer()
        customer_0.set_customer_information(self.user_id)
        customer_0.insert_money = self.insert_money_entry.get()
        customer_0.add_money()

    def show_check_balance(self):
        self.hide_all_container_frame_items()
        # self.all_buttons_hider()
        print("test2")

        rows = 0
        while rows < 10:
            self.root.rowconfigure(rows, weight=1)
            self.root.columnconfigure(rows, weight=1)
            rows += 1

        customer_0 = Customer()
        customer_0.set_customer_information(self.user_id)
        print(customer_0.check_balance)

        self.check_balance_label.config(text=f'{customer_0.check_balance}')
        self.check_balance_label.grid(row=0, column=3)

        self.withdraw_btn.grid_forget()

        self.back_btn.grid(row=1, column=3)
        self.exit_btn.grid(row=2, column=3)

    def back_performer(self):
        self.show_home_page()

    def transfer_money_performer(self):
        bank_0 = Bank()
        bank_0.money_transfer(self.user_id, self.receiver_id_entry.get(), int(self.amount_of_transfer_entry.get()))

class Authentication:

    def __init__(self):
        pass

    def login_user(self, user_id, password):

        '''Check username and password entered are correct'''
        bank_0 = Bank()
        # self.user_id = self.username.get()
        # self.user_passw = self.password.get()

        self.user_id = user_id
        self.user_passw = password

        # if  bank_0.login_id_password_check(self.user_id, self.user_passw):
        if bank_0.login_id_password_check(self.user_id, self.user_passw):
            return True
        else:
            return False


root = Tk()
root.geometry('425x425+0+0')
root.title("ATM AUTOMATION - GROUP 6 - YASIN - EMRAH")
ATM_GUI(root)
root.mainloop()

#
