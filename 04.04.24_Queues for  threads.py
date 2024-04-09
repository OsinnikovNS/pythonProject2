from collections import defaultdict
import queue
import threading
import random

CUSTOMER = (None, 1, 2, 3, 4, 5,)
class Table:
    pass
class Cafe(threading.Thread):
    def __init__(self, table_for_customer=10, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.customers = []
        self.table_for_customer = table_for_customer
        self.tank = queue.Queue(maxsize=3)
        self.catch = defaultdict(int)
    # def customer_arrival(self, number):
    #     customer = Customer(number=number, table=self.table_for_customer, tank=self.tank)
    #     self.customers.append(customer)

    def customer_arrival(self):
        print(f'Посетитель номер <номер посетителя> прибыл.', flush=True)
        for customer in self.customers:
            customer.start()
        while True:
            try:
                customer = self.tank.get(timeout=1)
                print(f'Столик в кафе принял {customer}', flush=True)
                self.catch[customer] += 1
            except queue.Empty:
                print(f'Столики свободны в течении 1 сек.')
                if not any(customer.is_alive() for customer in self.customers):
                    break
        for customer in self.customers:
            customer.join()
        print(f'Кафе закрывается')


cafe = Cafe(table_for_customer=10)
for number in CUSTOMER:
    cafe.customer_arrival()

cafe.start()
cafe.join()




# Customer - класс (поток) посетителя. Запускается, если есть свободные столы.
# class Customer(threading.Thread):
#     def __init__(self, number, busy, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.number = number
#         self.busy = busy
#     def run(self):
#         customer = random.choice(CUSTOMER)
#         if customer is None:
#             print(f'{self.number}, посетителей нет.', flush=True)
#         else:
#             print(f'Посетитель номер {self.number}, сел за стол. (начало обслуживания)', flush=True)
#             if self.busy.full():
#                 print(f'Посетитель номер {self.number}, ожидает свободный стол. (помещение в очередь)', flush=True)