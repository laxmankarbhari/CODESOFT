import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

length = int(input("Enter password length: "))

password = ""
for i in range(length):
    password += random.choice(chars)

print("Generated Password:", password)