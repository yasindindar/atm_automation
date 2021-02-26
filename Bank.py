class Bank():
    file_name = 0
    def __init__(self):
        pass

    def login_id_password_check(self, id, password):
        with open('Credentials.txt', 'r')as self.file_name:
            lines = self.file_name.readlines()
            list = [i.strip() for i in lines[:]]
            print(list)
            for i in list:
                # We need separated user id and password with split.
                new_list = i.split()
                # We checked both user id and password.
                if new_list[0] == id and new_list[1] == password:
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


    def is_avaliable(id, amount):
        pass



newbank = Bank()

print(newbank.login_id_password_check("12345678910", "password"))
print(newbank.is_user("82345671910"))
