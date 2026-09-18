email = input("Enter you email: ")

index = email.index("@")

username = email[0:index] 
domain = email[index + 1:]

print(f"your usename is {username} and domain is {domain}")