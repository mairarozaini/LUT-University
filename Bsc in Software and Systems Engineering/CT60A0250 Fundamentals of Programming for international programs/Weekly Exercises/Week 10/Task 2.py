def reading_content_file(filename):
    try:
        file =  open(filename, "r") 
        reader = file.read()
        return reader
    except FileNotFoundError:
        return None
    
def main():
    filename = input("Enter the file name:\n")
    contents = reading_content_file(filename)
    if contents is not None:
        print("File content:\n" + contents)
    else:
        print("Error: File not found.")
    
main()
