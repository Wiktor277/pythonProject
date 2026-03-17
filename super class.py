class User(object):
    def __init__(self,email):
        self.email = email
        print('init complete')

    def sign_in(self):
        print('logged in')


class wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def atack(self):
        print(f'atacking for {self.power} dmg')

class archer(User):
    def __init__(self,name,num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows


    def check_arrows(self):
        print(f'you have {self.num_of_arrows} left')


arch1 = archer('maggie', 10)

print(arch1.check_arrows())

class megaborg(wizard,archer):
    def __init__(self,name,power,num_of_arrows):
        archer.__init__(self, name, num_of_arrows)
        wizard.__init__(self,name,power)

mb1 = megaborg('terminator',10,50)

print(mb1.num_of_arrows)


