from pypdf import PdfReader
import subprocess

# page range
start_page = 26
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

        print(f"Reading page {start_page}")

        page = pdf_reader.pages[start_page]
        text = page.extract_text()
        text = text.replace('\n', ' ').strip()

        if text:
            subprocess.run(['say', '-v', 'Samantha', '-r', '165', text])
        else:
            print("⚠️ No extractable text on this page")

        start_page += 1
        resp = input(f"Page {start_page} - Read(y)/Skip(c)/Quit(n)? ")
