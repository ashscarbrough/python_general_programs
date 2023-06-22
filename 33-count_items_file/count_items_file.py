'''
Program to count the lines, words, and chars in a file
'''


def count_words(file_line):
    '''
    Function to count number of words in a file
    '''
    words = file_line.split()
    return len(words)

def count_characters(file_line):
    '''
    Function to count number of words in a file
    '''
    char_count = 0
    for char in file_line:
        if char.isalpha():
            char_count += 1
    return char_count

def main():
    '''
    Main driver to open file and read lines
    '''
    # Count tracker: [lines, words, chars]
    count = [0, 0, 0]

    file_input = input("Provide a file name for evaluation: ")

    with open(file_input, "r", encoding="UTF-8") as infile:
        # infile.read()
        for line in infile:
            count[0] +=1
            count[1] += count_words(line)
            count[2] += count_characters(line)

    print(f'{count[0]} lines were in the file {file_input}')
    print(f'{count[1]} words were in the file {file_input}')
    print(f'{count[2]} characters were in the file {file_input}')

if __name__ == "__main__":
    main()
