search_text = "null"
replace_text = "0"

with open('subProfile3a.txt', 'r') as file:
    data = file.read()
    data = data.replace(search_text, replace_text)

with open('subProfile3b.txt', 'w') as file:
    file.write(data)
