sentence = input("Hey! Type any sentence: ")
print(f"Wow, that's {len(sentence)} characters total! 🎉")

clean_text = sentence.replace(" ", "")
print(f"Without spaces: {len(clean_text)} chars")

letters = sum(c.isalpha() for c in sentence)
print(f"Letters: {letters} 💬")

numbers = sum(c.isdigit() for c in sentence)
print(f"Numbers: {numbers} 🔢")

spaces = sentence.count(" ")
print(f"Spaces: {spaces} ⏳")

others = len(sentence) - letters - numbers - spaces
print(f"Others (punctuation etc.): {others} ❓")