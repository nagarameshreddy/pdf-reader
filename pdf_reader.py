import PyPDF2
import pyttsx3

# path of the PDF file
path = open('concalls\\gls_feb2023.pdf', 'rb')


# creating a PdfFileReader object
pdfReader = PyPDF2.PdfReader(path)

start_page=2
end_page=17

while start_page < end_page:
    print(f"Reading page {start_page}")
    from_page = pdfReader.pages[start_page]
    text = from_page.extract_text()
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()
    start_page+=1
    resp = input("Want read the next page(y/n)?")
    if resp == 'y':
        pass
    else:
        break