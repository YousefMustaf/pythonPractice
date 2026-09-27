sentence = input("Enter your sentence: ").lower()
words = sentence.split(" ")

counts = {}
for word in words:
    word = word.strip(",!.")
    if word in counts:
       counts[word] = counts[word] + 1
    else:
        counts[word] = 1

print(counts) 

