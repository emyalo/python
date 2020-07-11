#Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со
# средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json
profit = {}
pr = {}
prof = 0
profit_average = 0
i = 0
with open('007.txt', 'r') as file:
    for line in file:
        name, firm, revenue, cost = line.split()
        profit[name] = int(revenue) - int(cost)
        if profit.setdefault(name) >= 0:
            prof += profit.setdefault(name)
            i += 1
    if i != 0:
        profit_average = prof / i
        print(f'Average profit - {profit_average}')
    else:
        print(f'NO PROFIT')
    pr = {'Average profit': round(profit_average)}
    profit.update(pr)
    print(f'Average profit of each company: {profit}')

with open('007.txt.json', 'w') as write_js:
    json.dump(profit, write_js)
    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')