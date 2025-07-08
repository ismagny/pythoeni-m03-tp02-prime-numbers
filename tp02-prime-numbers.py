# TP 02 - Prime numbers

# Step n°1

def prime_numbers(limit = 1000):
    for i in range(2, limit+1):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
        if prime:
            print(i)

prime_numbers(100)