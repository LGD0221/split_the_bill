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
        set_output('欢迎使用自助分账系统。')

    # 增加一个人的数据
    def add_person(self):
        name = ''
        while name == '':
            name = get_input('请输入姓名：')
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

    # 计算
    def calculate(self):
        self.total = round(sum([sum(person['accounts']) for person in self.people.values()]),2)  # 总金额
        self.average_cost = round(self.total / len(self.people),2)      # 人均金额，未使用
        total_weight = sum([p['weight'] for p in self.people.values()])     # 权重总和，作为个人权重的分母
        for person in self.people.values():
            weight = person['weight'] / total_weight    # 个人权重
            payable_amount = self.total * weight    # 理论需支付金额
            balance = payable_amount - sum(person['accounts'])  # 减去已支付金额后的实际结余
            payable_amount,balance = round(payable_amount,2),round(balance,2)
            person['payable_amount'] = payable_amount
            person['balance'] = balance
        self.payments = self.algo.run(self.people)
    
    # 展示明细，如总金额
    def show_detail(self):
        set_output('\n总金额{}元'.format(spliter.total))
        for name,person in self.people.items():
            set_output('{}需支付{}元'.format(name,person['payable_amount']))
        set_output('\n转账方案：')
        for payment in self.payments:
            set_output(payment)

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
    spliter = Spliter()
    n = int(get_input('请输入总人数：'))
    if n > 0:
        for i in range(n):
            set_output('\n第{}人'.format(i+1))
            spliter.add_person()
    spliter.calculate()
    # print(sum([p['payable_amount'] for p in spliter.people.values()]),spliter.total)
    spliter.show_detail()
    input('按回车键退出')