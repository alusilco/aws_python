
with open('preproinsulin_seq.txt', 'r') as file:
    lines = file.readlines()

print(lines) 

lines_content = lines[1:-1]
content_together = 'analucia'.join(lines_content)
print (lines_content) 

print (content_together)

clean_content = ''.join(filter(str.isalpha, content_together))
print (clean_content)

