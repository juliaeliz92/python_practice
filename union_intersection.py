#Create a program that finds the intersection and union of two sets

def getUnionIntersection(a, b):
    print(f'union {a | b}')
    print(f'intersection {a & b}')

p = {1, 2, 3, 4, 5}
q = {2, 4, 6}

print(f'{p}')
print(f'{q}')

getUnionIntersection(p, q)