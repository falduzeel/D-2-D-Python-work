print("🔍 Prime Number Checker! 🧮")
print("Enter 'quit' to exit 😊\n")

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

while True:
    num = input("📝 Check number: ").strip()
    
    if num.lower() == 'quit':
        print("👋 Bye! Happy checking! ✨")
        break
    
    try:
        n = int(num)
        result = "✅ PRIME!" if is_prime(n) else "❌ NOT PRIME"
        print(f"{n} → {result}\n")
    except:
        print("😅 Please enter a valid number!\n")