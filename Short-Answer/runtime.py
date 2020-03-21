from datetime import datetime


def first(n):
    start = datetime.now()
    a = 0
    while (a < n * n * n):

        a = a + n * n
    else:
        end = datetime.now()
        print(end-start)
        return a

# first(50)

def second(n):
    sum = 0
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            sum += 1
        else:
            return sum

print(second(12))