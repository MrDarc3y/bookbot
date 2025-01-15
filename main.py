def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    count_words_in_book = count_words(file_contents)
    count_letters_in_book = count_letters(file_contents)

    print("--- Begin report of books/frankensein.txt ---")
    print(f"{count_words_in_book} words found in the document")
    print("")
    create_report(count_letters_in_book)
    print("--- End report ---")

def count_words(text):
    return len(text.split())

def count_letters(text):
    count={}
    lowered = text.lower()
    for c in lowered:
        count[c] = count.get(c, 0) + 1
    return count

def sort_on(dict):
    return dict["num"]

def create_report(letters):
    report_list = []
    for letter in letters:
        if letter.isalpha():
            report_list.append({"letter": letter, "num": letters[letter]})
    report_list.sort(key=sort_on, reverse=True)

    for letter in report_list:
        print(f"The {letter['letter']} character was found {letter['num']} times")

main()