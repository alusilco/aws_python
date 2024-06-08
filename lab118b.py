def create_fragment_file(text, filename, start, finish):
    fragment = text[start:finish]
    with open(filename, 'w') as outfile:
        outfile.write(fragment)

with open('preproinsulin_seq.txt', 'r') as input_file:
    lines = input_file.readlines()

lines_content = lines[1:-1]
content_together = ''.join(lines_content)
clean_content = ''.join(filter(str.isalpha, content_together))

create_fragment_file(clean_content, 'lsinsulin-seq-clean.txt', 0, 24)
create_fragment_file(clean_content, 'binsulin-seq-clean.txt', 24, 54)
create_fragment_file(clean_content, 'cinsulin-seq-clean.txt', 54, 89)
create_fragment_file(clean_content, 'ainsulin-seq-clean.txt', 89, 110)
