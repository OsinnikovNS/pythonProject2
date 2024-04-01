import threading
# import time
# Класс BankAccount должен отражать банковский счет с балансом
# и методами для пополнения и снятия денег.


class BankAccount:
    def __init__(self):
        self.locker = None
        self.lock = threading.Lock()
        self.balance = 1000
        print(f'Банковский счет с балансом: {self.balance}')

    def deposit_task(self):
        amount = 100
        for _ in range(5):
            self.balance += amount
            print(f'Deposited {amount}, new balance is {self.balance}')

    def withdraw_task(self):
        amount = 150
        for _ in range(5):
            if self.balance >= amount:
                self.balance -= amount
                print(f'Withdraw {amount}, new balance is {self.balance}')
            else:
                print("Недостаточно средств на счете")


s = BankAccount()
deposit_thread = threading.Thread(target=s.deposit_task())
withdraw_thread = threading.Thread(target=s.withdraw_task())
# deposit_thread.start()
# withdraw_thread.start()
# deposit_thread.join()
# withdraw_thread.join()
# s.display()
