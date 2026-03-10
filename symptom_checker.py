symptom = input("Enter your symptom: ").lower()

if symptom == "fever":
    print("Possible illness: Viral Infection. Drink fluids and rest.")
elif symptom == "cough":
    print("Possible illness: Cold or respiratory infection.")
elif symptom == "headache":
    print("Possible illness: Stress or dehydration.")
else:
    print("Please consult a doctor.")

