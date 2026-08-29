from stats import count_words, count_char, sort_dict
import sys

def get_book_text(file_name):
    with open(file_name) as f:
        file_contents = f.read()
        return file_contents
 
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    
    text = get_book_text(sys.argv[1])
    print(count_words(text))

    print("--------- Character Count -------")
    character = count_char(text)
    
    sorted = sort_dict(character)
    for d in sorted:
        if d["char"].isalpha():
            print(f"{d['char']}: {d['num']}")

    print("============= END ===============")
    

main()

