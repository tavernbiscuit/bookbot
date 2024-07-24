def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()   
    
    words_counted = word_count(file_contents)
    chars_counted = count_chars(file_contents)
    dict_list = dict_as_list(chars_counted)
    dict_list.sort(reverse=True, key=sort_on)


    print("--- Begin report of books/frankenstein.txt ---\n")
    print(f"{words_counted} found in the document\n")
    
    for entry in dict_list:
        print(f"The letter '{entry['character']}' was found {entry['count']} times.")
    print("\n--- End Report ---")

def word_count(text):
    words = text.split()
    count = len(words)
    return count

def count_chars(text):
    string = text.lower()
    character_count = {}
    for char in string:
        if char.isalpha():
            character_count[char] = character_count.get(char, 0) + 1
    return character_count 

def dict_as_list(dict):
    char_list = []
    for char, count in dict.items():
        char_list.append({"character": char, "count": count})
    return char_list

def sort_on(list):
    return list["count"]


main()