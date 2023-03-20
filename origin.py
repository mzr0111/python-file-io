import re

pattern = re.compile(r'\b(?:inherit(?:able|ance|ed)?|heritable)\b', re.IGNORECASE)

with open('origin.txt', 'r') as in_stream:
    with open('newfile.txt', 'w') as out_stream:
        for line_num, line in enumerate(in_stream, start=1):
            matches = pattern.findall(line)
            for match in matches:
                out_stream.write(f"{line_num}\t{match}\n")

print("Done!")
