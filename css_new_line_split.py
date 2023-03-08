with open("styles.css", "r") as file:
    data = file.read()

lines = []
current_line = ""
for char in data:
    current_line += char
    if char == "}" or char == ";":
        lines.append(current_line.strip())
        current_line = ""

if current_line:
    lines.append(current_line.strip())

with open("styles.css", "w") as file:
    file.write("\n".join(lines))

