import threading
import queue
import time


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        for i in range(1, 21):
            time.sleep(.01)
            print(f"Посетитель номер {i} прибыл")
            time.sleep(.1)
            customer = {"number": i}
            self.queue.put(customer)

    def serve_customer(self, customer):

        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer['number']} сел за стол {table.number}")
                time.sleep(.5)
                table.is_busy = False
                print(f"Посетитель номер {customer['number']} покушал и ушёл")
                return
        print(f"Посетитель номер {customer['number']} ожидает свободный стол")
        self.queue.put(customer)



def customer_thread(cafe):
    while True:
        customer = cafe.queue.get()
        cafe.serve_customer(customer)
        cafe.queue.task_done()
        if cafe.queue.empty():
            break

table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

for _ in range(3):
    t = threading.Thread(target=customer_thread, args=(cafe,))
    t.start()

customer_arrival_thread.join()


#
# class Table:
#     def __init__(self, number):
#         self.number = number
#         print(f'Создали столик {number}')
#
#
# class Cafe(threading.Thread):
#     def __init__(self, *args, **kwargs):
#         # super().__init__(*args, **kwargs)
#         self.customers = ()
#         self.table_for_customer = queue.Queue(maxsize=3)
#         # self.tables = 3
#         self.catch = defaultdict(int)
#
#     def customer_arrival(self):
#         for self.customers in range(10):
#             self.customers += 1
#             time.sleep(.1)
#             print(f'Посетитель номер {self.customers} прибыл.', flush=True)
#
#     def serve_customer(self, ncustomer):
#         if self.tables is None:
#             print(f'Посетитель номер {ncustomer}, ожидает свободный стол. (помещение в очередь)', flush=True)
#         else:
#             print(f'Посетитель номер {ncustomer}, сел за стол. (начало обслуживания)', flush=True)
#             while True:
#                 try:
#                     customer = self.customers.get(timeout=5)
#                     print(f'Столик в кафе принял {customer}', flush=True)
#                     self.catch[customer] += 1
#                 except queue.Empty:
#                     print(f'Столики свободны в течении 1 сек.')
#                     if not any(customer.is_alive() for customer in self.customers):
#                         break
#         for customer in self.customers:
#             customer.join()
#         print(f'Кафе закрывается')
#         print(f'Посетитель номер {self.number}, сел за стол. (начало обслуживания)', flush=True)
#
#
# class Customer:
#     def __init__(self):
#         pass
#
#
# table1 = Table(1)
# table2 = Table(2)
# table3 = Table(3)
# tables = [table1, table2, table3]
#
# cafe = Cafe(tables)

