from cryptography.fernet import Fernet
import base64

def create_encrypted_script(input_file, output_file, password):
    # Read the input script
    with open(input_file, 'r') as f:
        code = f.read()
    
    # Generate key from password
    key = base64.urlsafe_b64encode(password.encode().ljust(32)[:32])
    encrypted = Fernet(key).encrypt(code.encode())
    
    # Create output script with decryption code
    output_code = f'''
from cryptography.fernet import Fernet
import base64

# Change this password to decrypt and run the code
PASSWORD = "password"

# Encrypted code
ENCRYPTED = {encrypted}

# Decrypt and run
key = base64.urlsafe_b64encode(PASSWORD.encode().ljust(32)[:32])
code = Fernet(key).decrypt(ENCRYPTED).decode()
exec(code)
'''
    
    # Save the output script
    with open(output_file, 'w') as f:
        f.write(output_code)

if __name__ == "__main__":
    # Example usage
    create_encrypted_script("input.py", "encrypted_output.py", "password")
