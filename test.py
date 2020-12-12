# print("Hello World!")

# 演算
# print(1+1)

# 変数
# unko = 'Hello World2!'
# print(unko)


# class Card:
#     def __init__(self, date, user_name):
#         self.date = date
#         self.user_name = user_name
#     def message(self):
#         return 'この投稿は' + self.user_name + 'さんが' + self.date + 'に投稿しました'

# date_a = '2020-01-01'
# user_name_a = 'Taro'
# card_a = Card(date_a, user_name_a)

# date_b = '2020-01-03'
# user_name_b = 'Hanako'
# card_b = Card(date_b, user_name_b)

# print(card_a.date, card_a.user_name, card_a.message())
# print(card_b.message())


# import module_name ... モジュール(変数・関数・クラス等を汎用的に使えるようにまとめたコード群)をインポートする
import math
print(math.pi)

# 外部モジュール
# NumPy
# Pandas
# Flask
# Django

import numpy

numpy_list = [3, 1, 5, 10 , 1093, 48]
print(numpy.sum(numpy_list))