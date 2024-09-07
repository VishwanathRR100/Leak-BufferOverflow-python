#normal method
def sq(num):
    sq = []
    for i in range(1,num+1):
        sq.append(i*i)
    return sq
print(sq(5))

# using generators

def sq_gen(num):
    for i in range(1,num+1):
        yield i*i

sq_val = sq_gen(5)
print(sq_val)

# print(sq_val)

for i in sq_val:
    print(i,end=" ")