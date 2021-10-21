per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
banks = (" ".join(per_cent.keys()))
invest = input("Сумма инвестиций:")
deposit = [int(invest)*per_cent['ТКБ']/100, int(invest)*per_cent['СКБ']/100, int(invest)*per_cent['ВТБ']/100, int(invest)*per_cent['СБЕР']/100]
deposit_max = max(deposit)
print(banks[0:3], ":", deposit[0], ",", banks[4:7], ":", deposit[1], ",", banks[8:11], ":", deposit[2], ",", banks[12:17], ":", deposit[3])
print("Максимальная сумма, которую вы можете заработать:", deposit_max)