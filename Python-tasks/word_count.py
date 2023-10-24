import PyPDF2
def result(file2):
    with open(file2, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        pdf_text = ''                  # Initialize pdf_text to store the extracted text
        for page in reader.pages:
            pdf_text += page.extract_text()
            print(pdf_text)     # Print the extracted text  of pages after the loop
    words = pdf_text.split()
    word_count = {}              # Initialize word_count to store count of  words & loop to count words
    for word in words:
        word = word.strip('.')
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for word, count in word_count.items():        # to display word count
        print(f"{word}: {count}")
file2 = 'data/unique_words_pdf.pdf'              # Pdf file location
result(file2)