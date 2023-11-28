net_prices = [1000, 2500, 100_000, 12_000]
vat_rate_in_percent = 27
# gross_prices = []
#
# for i in net_prices:
#     # gross_price = i * (1 + vat_rate_in_percent / 100)
#     # gross_prices.append(gross_price)
#     gross_prices.append(i * (1 + vat_rate_in_percent / 100))

gross_prices = [i * (1 + vat_rate_in_percent / 100) for i in net_prices]
print(gross_prices)

values = [1, 2, 3, 4, 5, 6, 7, 3, 4, 5, 7, 6, 8, 1, 2, 0, 0, 1]
grades = [i for i in values if 0 < i < 6]
print(grades)

accepted_values = [1, 2, 3]
accepted_list = [i for i in values if i in accepted_values]
print(accepted_list)

matrix = []
# matrix = [
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
# ]

# for i in range(5):
#     row = []
#     for j in range(5):
#         row.append(j)
#     matrix.append(row)
#
# print(matrix)
#         [     row           ]
matrix = [[j for j in range(5)] for _ in range(5)]
print(matrix)

flatten_matrix = [item for row in matrix for item in row]
print(flatten_matrix)

# for row in matrix:
#     print(row)

# flatten_matrix = []
# for row in matrix:
#     for item in row:
#         flatten_matrix.append(item)
#
# print(flatten_matrix)

rpg_games = [
    ['Earthdawn', 'M.A.G.U.S', 'D&D'],
    ['Rifts', 'Shadownrun', 'Cyberpunk 2020', 'Star Wars'],
    ['Vampire', 'Call of Cthulhu']
]

flatten_games = [game for row in rpg_games for game in row if len(game) > 7]
print(flatten_games)
