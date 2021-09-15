from bs4 import BeautifulSoup

NEW_VALUE = "closed"

with open("demo.html") as demo_file:    
    soup = BeautifulSoup(demo_file, "html.parser")

for element in soup.find_all("span", { "class": "red"}):
    element.string = NEW_VALUE

with open("out.html", "w") as out_file:
    out_file.write(str(soup))