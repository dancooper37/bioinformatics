from itertools import product
lexOrder = ["A", "B", "C", "D", "E", "F", "G"]
n = 3

combinations = product(lexOrder, repeat=n)

for item in combinations: print(("").join(item))







