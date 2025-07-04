import algorithms
import algorithms.max_centered

DATA = {'p1': {'accounts': [0.01], 'weight': 1.0}, 'p2': {'accounts': [0.01], 'weight': 2.0}, 'p3': {'accounts': [0.0], 'weight': 1.0}}

class Spliter:
    def __init__(self,data = {}):
        DEFAULT_ALGO = algorithms.max_centered.MaxCentered()
        self.people:dict = data
        self.total = 0
        self.average_cost = 0
        self.algo = DEFAULT_ALGO
        self.payments = {}

    def add_person(self):
        name = get_input('\n请输入姓名：')
        if name not in self.people:
            accounts = []
            weight = 1.0
            input_accounts = get_input('请输入金额，多项用空格分隔:')
            input_weight = get_input('请输入权重，留空为1：')
            for amount in input_accounts.split():
                if is_number(amount):
                    accounts.append(float(amount))
                else:
                    pass
            if is_number(input_weight):
                weight = float(input_weight)
            self.people[name] = {'accounts':accounts,'weight':weight}

    def calculate(self):
        self.total = sum([sum(person['accounts']) for person in self.people.values()])
        self.average_cost = round(self.total / len(self.people),2)
        total_weight = sum([p['weight'] for p in self.people.values()])
        for person in self.people.values():
            weight = person['weight'] / total_weight
            payable_amount = self.total * weight
            balance = payable_amount - sum(person['accounts'])
            payable_amount,balance = round(payable_amount,2),round(balance,2)
            person['payable_amount'] = payable_amount
            person['balance'] = balance
        self.payments = self.algo.run(self.people)

class Payment:
    def __init__(self,from_who:str,to_who:str,amount:float):
        if amount == 0:
            return None
        if amount < 0:
            amount = abs(amount)
            from_who,to_who = to_who,from_who
        self.from_who,self.to_who,self.amount = from_who,to_who,amount
    
    def __str__(self):
        return '{}向{}转账{}元'.format(self.from_who,self.to_who,self.amount)

def is_number(string):
    try:
        float(string)
        return True
    except:
        pass
    return False

def get_input(prompt):
    return input(prompt)

def set_output(message):
    print(message)

if __name__ == "__main__":
    spliter = Spliter(DATA)
    spliter.calculate()
    print(sum([p['payable_amount'] for p in spliter.people.values()]),spliter.total)
    for payment in spliter.payments:
        set_output(payment)