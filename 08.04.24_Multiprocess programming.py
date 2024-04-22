"""Движение товаров на складе, запросы на обновление информации о поступлении товаров и отгрузке товаров."""
import multiprocessing
import time


class WarehouseManager(multiprocessing.Process):
    def run(self):
        requests = [
            ("product1", "receipt", 100),
            ("product2", "receipt", 150),
            ("product1", "shipment", 30),
            ("product3", "receipt", 200),
            ("product2", "shipment", 100),

        ]
        count, product1, product2, product3 = 0, 0, 0, 0
        for _ in requests:
            count += 1
        print(f'количество запросов: {count}')
        for i in range(count):
            d = requests[i]
            i += 1
            product, request, data = str(d[0]), str(d[1]), int(d[2])
# -------------------------- Поступление товара на склад -----------------------------
            if product == str('product1') and request == str('receipt'):
                product1 += data
            if product == str('product2') and request == str('receipt'):
                product2 += data
            if product == str('product3') and request == str('receipt'):
                product3 += data
# -------------------------- Отгрузка товара со склада -----------------------------
            if product == str('product1') and request == str('shipment'):
                if product1 >= data:
                    product1 -= data
                else:
                    print(f'Для отгрузки, товара на складе недостаточно, product1 = {product1}')
            if product == str('product2') and request == str('shipment'):
                if product2 >= data:
                    product2 -= data
                else:
                    print(f'Для отгрузки, товара на складе недостаточно, product2 = {product2}')
            if product == str('product3') and request == str('shipment'):
                if product == str('product3') and request == str('shipment'):
                    if product3 >= data:
                        product3 -= data
                    else:
                        print(f'Для отгрузки, товара на складе недостаточно, product3 = {product3}')

        prod = {f'product1: {product1}, product2: {product2}, product3: {product3}'}
        print(prod)


if __name__ == '__main__':
    manager = WarehouseManager()
    manager.start()
    manager.join()
    print('Все процессы завершены')
