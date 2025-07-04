import algorithms
import algorithms.max_centered

DATA = {'p1': {'accounts': [1.0, 2.0, 3.0], 'weight': 1.0}, 'p2': {'accounts': [0.1, 117.0], 'weight': 2.0}, 'p3': {'accounts': [0.0], 'weight': 1.0}}
DEFAULT_ALGO = algorithms.max_centered.MaxCentered()

class Spliter:
    def __init__(self,data = {}):
        self.people:dict = data
        self.total = 0
        self.average_cost = 0
        self.algo = DEFAULT_ALGO

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
            payable_amount = self.average_cost * weight
            balance = payable_amount - sum(person['accounts'])
            person['payable_amount'] = payable_amount
            person['balance'] = balance
            result = self.algo.run(self.people)
        return self.total,self.average_cost

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
    set_output(spliter.calculate())
    set_output(spliter.people)