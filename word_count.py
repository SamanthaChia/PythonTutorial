def count_words(filename):
    """Count the approximate number of words in a file."""
    for book in filename:
        try:
            with open(book) as f_obj:
                contents = f_obj.read()
        except FileNotFoundError:
            pass
        else:
            #Count the approximate number of words in the file
            words = contents.split()
            num_words = len(words)
            print("The file " + book + " has about " + str(num_words) + " words.")

filename = ['alice.txt','moby_dick.txt']
count_words(filename)