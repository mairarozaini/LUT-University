
def input_integers(integers):

    for i in range(len(integers)):
        for j in range(i + 1, len(integers)):
            if integers[i] > integers[j]:
                integers[i], integers[j] = integers[j], integers[i]
    return integers
    
def main():
    integers = list(map(int, input("Give integers separated by comma:\n").split(",")))
#   print(input_integers(integers))
    
    element = int(input("Give an integer:\n"))

    chosen_element = input_integers(integers)
    
    if element <= len(integers):
        print(f"{element}th smallest element is {chosen_element[element-1]}")
    else:
        print("Not suitable")
                  
main()

    
