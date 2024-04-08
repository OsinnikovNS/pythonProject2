requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]

count, product1, product2, product3 = 0, 0, 0, 0
for i in requests:
    count += 1
# print(requests)
# print(f' elements in the list: {count}')

for i in range(count):
    d = requests[i]
    i += 1
    a, b, c = str(d[0]), str(d[1]), int(d[2])
    if a == str('product1') and b == str('receipt'):
        product1 += c
    if a == str('product1') and b == str('shipment'):
        product1 -= c

    if a == str('product2') and b == str('receipt'):
        product2 += c
    if a == str('product2') and b == str('shipment'):
        product2 -= c

    if a == str('product3') and b == str('receipt'):
        product3 += c
    if a == str('product3') and b == str('shipment'):
        product3 -= c

    # print(a, b, c)
print(f'product1: {product1}, product2: {product2}, product3: {product3}')


# class WarehouseManager:
#     # класс менеджера склада
#     def __init__(self, data, *args, **kwargs):
#         self.data = {}
#
#
#     def process_request(self):
#
#         pass
#
#
# manager = WarehouseManager()
# requests = [
#     ("product1", "receipt", 100),
#     ("product2", "receipt", 150),
#     ("product1", "shipment", 30),
#     ("product3", "receipt", 200),
#     ("product2", "shipment", 50)
#     ]
# # Запускаем обработку запросов
# manager.run(requests)
# # Выводим обновленные данные о складских запасах
# print(manager.data)
