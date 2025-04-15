def get_book_text(path_to_file):
    
    with open(path_to_file) as f:
        file_contets = f.read()
    return file_contets

from stats import get_num_words, characterCounter, prettifyDict
import sys


def main():
    
    book = get_book_text(sys.argv[1])
    ChaaracterCount = prettifyDict(characterCounter(book))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")
    print("--------- Character Count -------")
    for x in range(len(ChaaracterCount)):
        print(f"{ChaaracterCount[x]['char']}: {ChaaracterCount[x]['count']}")

    print("============= END ===============")



if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
elif len(sys.argv) > 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()

