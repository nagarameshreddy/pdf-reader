from pypdf import PdfReader
import pyttsx3

# page range
start_page = 12
end_page = 356
resp = 'y'



# Open PDF safely
with open('pdfs/Books/annas-arch-b1e0c9675943.pdf', 'rb') as file:
    pdf_reader = PdfReader(file)

    while start_page < end_page:
        if resp == 'c':
            start_page += 1
            continue
        elif resp == 'n':
            break
        # resp == 'y' → fall through

        print(f"Reading page {start_page}")

        # Initialize text-to-speech
        speak = pyttsx3.init()

        speak.setProperty(
            'voice',
            'com.apple.voice.compact.en-US.Samantha'
        )

        # Reduce speaking speed
        speak.setProperty('rate', 165)

        page = pdf_reader.pages[start_page]
        text = page.extract_text()
        text = text.replace('\n', ' ').strip()

        if text:  # guard against empty pages
            speak.say(text)
            speak.runAndWait()
            speak.stop()
        else:
            print("⚠️ No extractable text on this page")

        start_page += 1
        resp = input(f"Page {start_page} - Read(y)/Skip(c)/Quit(n)? ")
