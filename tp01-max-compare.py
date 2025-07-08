#  TP 01 - Max et Compare

#  Function n°1
def get_max(a, b):
    if a > b:
        return a
    else:
        return b

# Function n°2
def get_compare(a, b):
    if a == b:
        return 0
    elif a > b:
        return 1
    else:
        return -1

# Function n°3
def test_max_and_compare():
    a = int(input("Saisissez un nombre : "))
    b = int(input("Saisissez un nombre à nouveau : "))
    result_max = get_max(a, b)
    result_compare = get_compare(a, b)
    print(f"La valeur la plus grande est {result_max}")
    print(f"Le résultat de la comparaison est {result_compare}")


test_max_and_compare()
