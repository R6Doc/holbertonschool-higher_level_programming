#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        numero = 0
        deml = 0
        for tup in my_list:
            numero += (tup[0] * tup[1])
            deml += tup[1]
        return (numero / deml)
    return 0
