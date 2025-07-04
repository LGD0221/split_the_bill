from split_the_bill import Payment

class MaxCentered():
    def __init__(self):
        pass

    def run(self,people:dict) -> list[Payment]:
        names = []
        totals = []
        for name,person in people.items():
            names.append(name)
            total = sum(person['accounts'])
            totals.append(total)
        max_index = totals.index(max(totals))
        max_name = names[max_index]
        payments = []
        for name,person in people.items():
            balance = person['balance']
            if name != max_name and balance:
                payment = Payment(name,max_name,balance)
                payments.append(payment)
        return payments

