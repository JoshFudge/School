from fileinput import filename


FILENAME = "groceries.html"

print()
print("HTML File Converter")
print()

with open(FILENAME,newline="") as file:
    text=file.read()
    for row in text:
        
        text = text.replace("<html>", "")
        text = text.replace("</h1>", "")
        text = text.replace("<h1>", "")
        text = text.replace("</li>", "")
        text = text.replace("<li>", "* ")
        text = text.replace("</ul>", "")
        text = text.replace("<ul>", "")
        text = text.replace("</html>", "")
        
        Empty_lines = text.split('\n')
        for text in Empty_lines:
            if text.strip() != "":
                text = text.strip()
                print(text)
        