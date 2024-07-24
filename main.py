def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()   
    
    words_counted = word_count(file_contents)
    chars_counted = count_chars(file_contents)
    print(chars_counted)

def word_count(text):
    words = text.split()
    count = len(words)
    return count

def count_chars(text):
    string = text.lower()
    character_count = {}
    for char in string:
        character_count[char] = character_count.get(char, 0) + 1
    return character_count 

main()