import sys
from stats import count_words, count_characters, sort_characters


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    path = sys.argv[1]
    contents = get_book_text(path)
    result = count_characters(contents)
    sorted_chars = sort_characters(result)
    words_total = count_words(contents)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {words_total} total words')
    print('--------- Character Count -------')
    for word_dict in sorted_chars:
        if word_dict['char'].isalpha():
            print(str(word_dict['char']) + ': ' + str(word_dict['num']))
    print('============= END ===============')


if __name__ == "__main__":
    main()
