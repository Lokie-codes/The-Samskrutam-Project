# Program to extract text from PDF
from pypdf import PdfReader

reader = PdfReader("Ashtadhyayi.pdf")
num_of_pages = len(reader.pages)
page = reader.pages[81]
text = page.extract_text()
print("Total Pages : {}".format(num_of_pages))
print(text)