def main():
    print("--- Begin report of books.frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    print(f"{len(words)} found in the document\n")
    final_dict = dict_to_list(count_chars(words))
    final_dict.sort(reverse=True, key=sort_on)
    for item in final_dict:
        print(f"The '{item['char']} character was found {item['num']} times")
    print("--- End report ---")

def count_chars(words):
    chars = {}
    for word in words:
        lowered_word = word.lower()
        for char in lowered_word:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def dict_to_list(chars):
    list_of_dicts = []
    for k, v in chars.items():
        if k.isalpha():
            list_of_dicts.append({"char": k, "num": v})
    return list_of_dicts




main()
