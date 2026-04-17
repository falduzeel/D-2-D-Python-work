print("🔢 Simple Math Game")
print("Guess the answer!")

# Very simple addition
a = 5
b = 7
answer = a + b

guess = int(input(f"What is {a} + {b}? "))
if guess == answer:
    print("✅ CORRECT! 🎉")
else:
    print(f"❌ Wrong! It is {answer}")