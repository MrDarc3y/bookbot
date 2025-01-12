def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    count_words_in_book = count_words(file_contents)
    print(count_words_in_book)

def count_words(text):
    return len(text.split())

main()