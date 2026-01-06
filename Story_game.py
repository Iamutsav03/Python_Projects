with open("story.txt", "r") as file:
    content = file.read()
    
words =set()
start_word = -1
target_word = '<'
end_word = '>'
for i, char in enumerate(content):
    if char == target_word:
        start_word = i
        
    if char == end_word and start_word != -1:
        word = content[start_word : i+1]
        words.add(word)
        start_word = -1
        
answer = {}
for word in words:
    temp = input("Please enter the respective word to build a story --> "+ word+" ")
    answer[word] = temp
    
for word in words:
    content = content.replace(word , answer[word])

print(content)
        
