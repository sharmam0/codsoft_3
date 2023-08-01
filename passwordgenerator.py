def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Welcome to the Password Generator!")

    length = int(input("Enter the desired length of the password: "))

    password = generate_password(length)

    print("Generated Password:", password)

password_generator()