import PyPDF2
import pyttsx3

# path of the PDF file (macOS compatible path)
path = open('pdfs/Concalls/Aiaeng.pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfReader(path)



start_page = 5
end_page = 19

resp = 'y'

# Initialize text-to-speech for this page
speak = pyttsx3.init()

speak.setProperty(
'voice',
'com.apple.voice.compact.en-US.Samantha'
)

# Reduce speaking speed
speak.setProperty('rate', 165)



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
    #print(text)

    

    # Set female voice
    #voices = speak.getProperty('voices')
    # for voice in voices:
    #     if 'rishi' in voice.name.lower() or 'female' in voice.name.lower():
    #         speak.setProperty('voice', voice.id)
    #         break

    

    speak.say(text)
    speak.runAndWait()
    #speak.stop()

    start_page += 1
    resp = input(f"Page {start_page} - Read(y)/Skip(c)/Quit(n)? ")

path.close()