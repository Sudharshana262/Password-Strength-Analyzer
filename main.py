password = input("Enter a password: ")

#Password Length Check
if len(password) >= 8:
    print("Length Check: PASS")
else:
    print("Length Check: FAIL")

#Uppercase Check
has_upper = False

for char in password:
    if char.isupper():
        has_upper = True

if has_upper:
    print("Uppercase Check: PASS")
else:
    print("Uppercase Check: FAIL")

#Lowercase Check
has_lower = False

for char in password:
    if char.islower():
        has_lower = True

if has_lower:
    print("Lowercase Check: PASS")
else:
    print("Lowercase Check: FAIL")

#Number Check
has_digit = False

for char in password:
    if char.isdigit():
        has_digit = True

if has_digit:
    print("Number Check: PASS")
else:
    print("Number Check: FAIL")

#Special Character Check
special_characters = "!@#$%^&*()_+-="

has_special = False

for char in password:
    if char in special_characters:
        has_special = True

if has_special:
    print("Special Character Check: PASS")
else:
    print("Special Character Check: FAIL")

#Score System
score = 0

if len(password) >= 8:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

#Password Strength Calculate
if score <= 2:
    print("Password Strength: WEAK")

elif score <= 4:
    print("Password Strength: MEDIUM")

else:
    print("Password Strength: STRONG")