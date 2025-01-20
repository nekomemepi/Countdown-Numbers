from itertools import chain, combinations_with_replacement, permutations, zip_longest

# Define the two lists
numbers = [75, 5, 9, 3, 8, 10]
operators = ['+', '-', '*', '/']

# Generate all possible partitions of the numbers
step1 = [c for i in range(2, len(numbers)+1) for c in permutations(numbers, i)]

# Generate partitions for each tuple
step2 = list(chain.from_iterable([[[l[:i], l[i:j], l[j:]]
                                   for i in range(1,len(l)+1)
                                   for j in range(i+1,len(l)+1)]
                                  for l in step1]))

# remove empty lists
step3 = ([i for i in y if i] for y in step2)

# convert to a list of strings, removing commas
step4 = (' '.join((map(str, i))).replace(',', '').split(' ') for i in step3)

# Generate the Cartesian product of all permutations of numbers and operators
cartesian_product = ((x, y)
    for x in step4
    for y in [list(p)
              for r in range(2, 7)
              for p in combinations_with_replacement(operators, r - 1)]
    if len(x) == len(y) + 1)

# Zip the Cartesian product using itertools.zip_longest

result = (i for i in (''.join( tuple(item for sublist in zip_longest(*x, fillvalue='') for item in sublist)) for x in cartesian_product) if eval(i) == 699)

print(list(result))
