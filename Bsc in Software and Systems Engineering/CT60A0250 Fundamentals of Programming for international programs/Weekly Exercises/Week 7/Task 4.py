def count_lines(my_file):
    my_file = open(my_file, 'r')
       
    line_number = 0
    for line in my_file:
        line_number += 1
    print(f"Number of lines: {line_number}")
   
    my_file.close()

def count_words(my_file):
    my_file = open(my_file, 'r')
    
    lines = str(my_file.readlines())
    word_number = len(lines.split())   
    print(f"Number of words: {word_number}")
    
    my_file.close()

def main():
    my_file = input("Give the text file to analyze:\n")
    count_lines(my_file)
    count_words(my_file)
    
main()
