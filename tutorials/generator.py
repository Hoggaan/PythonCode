def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

filename = 'tutorials/generatorsData.csv'
csv_gen = csv_reader(filename)
row_count = 0

for row in csv_gen:
    row_count += 1

# print(f"Row count is {row_count}")

gen = (row for row in open(filename))
rows = 0
for row in gen:
    rows += 1
# print(rows)

# Square Numbers using both list comprehension and generators
lst_comp = [num ** 2 for num in range(1000)]
gen = (num ** 2 for num in range(1000))

import sys
print(sys.getsizeof(gen))
print(sys.getsizeof(lst_comp))