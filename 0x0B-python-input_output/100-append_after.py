def append_after(filename="", search_string="", new_string=""):
    """
    function that appends a new string unto a line after reading the peruse
    in a UTF-8 text file.
    """

    with open(filename, 'r', encoding='UTF-8') as file:
        peruse = file.readlines()
    
    appended = False

    with open(filename, 'w', encoding='UTF-8') as file:
        for line in peruse:
            file.write(line)
            if '\n' in line and not appended:
                file.write(new_string)

        print("success")

append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
