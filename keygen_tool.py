import os
import base64

def generate_key(length=32):
    key = os.urandom(length)
    return base64.urlsafe_b64encode(key).decode('utf-8')

def save_key_to_file(filename, key):
    with open(filename, 'w') as file:
        file.write(key)

if __name__ == "__main__":
    key = generate_key()
    print("Generated Key:", key)
    save_key_to_file("secret.key", key)
