import PyPDF2
import pyttsx3

# path of the PDF file (macOS compatible path)
path = open('pdfs/aiaeng.pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfReader(path)

# initialize text-to-speech once (more efficient)
speak = pyttsx3.init()

# Set female voice (macOS default female voice is Samantha)
voices = speak.getProperty('voices')

for voice in voices:
    if 'rishi' in voice.name.lower() or 'female' in voice.name.lower():
        speak.setProperty('voice', voice.id)
        break


# Reduce speaking speed (default is 200, lower is slower)
speak.setProperty('rate', 180)

start_page = 3
end_page = 17

resp = 'y'

while start_page < end_page:
    if resp == 'c':
        start_page += 1
        continue
    elif resp == 'y':
        pass
    elif resp == 'n':
        break

    print(f"Reading page {start_page}")
    from_page = pdfReader.pages[start_page]
    text = from_page.extract_text()
    speak.say(text)
    speak.runAndWait()
    start_page += 1
    resp = input(f"Page {start_page} - Read(y)/Skip(c)/Quit(n)? ")

path.close()