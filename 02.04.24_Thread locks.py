import threading
import time
# Класс BankAccount должен отражать банковский счет с балансом
# и методами для пополнения и снятия денег.


class BankAccount:
    def __init__(self):
        self.lock = threading.Lock()
        self.balance = 1000

        print(f'Банковский счет с балансом: {self.balance}')

    def deposit_task(self):
        amount = 100
        for _ in range(5):
            time.sleep(1)
            self.lock.acquire()
            self.balance += amount
            print(f'Deposited {amount}, new balance is {self.balance}')
            self.lock.release()

    def withdraw_task(self):
        amount = 150
        for _ in range(5):
            time.sleep(1)
            if self.balance >= amount:
                self.lock.acquire()
                self.balance -= amount
                print(f'Withdraw {amount}, new balance is {self.balance}')
                self.lock.release()
            else:
                print("Недостаточно средств на счете")


s = BankAccount()
deposit_thread = threading.Thread(target=s.deposit_task)
withdraw_thread = threading.Thread(target=s.withdraw_task)
deposit_thread.start()
deposit_thread.join()
withdraw_thread.start()
withdraw_thread.join()
