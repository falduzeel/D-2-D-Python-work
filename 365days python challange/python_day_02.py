import random

print("🚀 100 TIMES MATH CHALLENGE!")
print("Press ENTER after each answer!")

score = 0

for i in range(100):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    correct = a + b
    
    print(f"\nQ{i+1}: {a} + {b} = ?", end=" ")
    your_ans = int(input())
    
    if your_ans == correct:
        print("✅")
        score += 1
    else:
        print(f"❌ ({correct})")

print(f"\n🏆 FINAL SCORE: {score}/100")
print(f"Percentage: {(score/100)*100:.0f}%")