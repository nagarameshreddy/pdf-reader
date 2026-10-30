from pypdf import PdfReader
import subprocess

# page range The Art of Spending money-2025.pdf
# start_page = 69
# end_page = 167
# resp = 'y'

start_page = 54
end_page = 162
resp = 'y'

# Open PDF safely
with open('pdfs/Books/The Great Mental Models Vol 1.pdf', 'rb') as file:
    pdf_reader = PdfReader(file)

    while start_page < end_page:
        if resp == 'c':
            #print("resp is ", resp)
            start_page += 1
            resp = input(f"Page {start_page} - Read(y)/Skip(c)/Quit(n)? ")
            continue
        elif resp == 'n':
            break

        print(f"Reading page {start_page}")

        page = pdf_reader.pages[start_page]
        text = page.extract_text()
        text = text.replace('\n', ' ').strip()

        if text:
            # subprocess.run(['say', '-v', 'Samantha', '-r', '165', text])
            # subprocess.run(['say', '-v', 'Aman', '-r', '170', text])
            # subprocess.run(['say', '-v', 'Tara', '-r', '165', text])
            subprocess.run(['say', '-r', '162', text])
            # subprocess.run(['say', '-v', 'D', '-r', '165', text])
            # subprocess.run(['say', '-v', 'D', '-r', '165', text])

                # if start_page%2==0:
                #     subprocess.run(['say', '-v', 'Samantha', '-r', '165', text])
                # else:
                #     subprocess.run(['say', '-v', 'Rishi', '-r', '170', text])
        else:
            print("⚠️ No extractable text on this page")

        start_page += 1
        resp = input(f"Page {start_page} - Read(y)/Skip(c)/Quit(n)? ")
