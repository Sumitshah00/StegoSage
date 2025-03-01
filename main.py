import os
from PIL import Image
from colorama import Fore, Style

# Colored Banner
def print_banner():
    banner = f"""{Fore.RED}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠾⠛⢉⣉⣉⣉⡉⠛⠷⣦⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠋⣠⣴⣿⣿⣿⣿⣿⡿⣿⣶⣌⠹⣷⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣆⠉⠻⣧⠘⣷⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠈⠀⢹⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⣿⠛⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⢸⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⢿⡆⠈⠛⠻⠟⠛⠉⠀⠀⠀⠀⠀⠀⣾⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡀⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⠿⣦⣄⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣦⠀⠀⠈⠉⠛⠓⠲⠶⠖⠚⠋⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣄⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.CYAN}Dev    :- sumit shah
Version :- 0.0.1
{Style.RESET_ALL}"""
    print(banner)

# Convert text to binary
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

# Convert binary to text
def binary_to_text(binary):
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

# Encrypt message with password
def encrypt_text(text, password):
    encrypted_text = "".join(chr(ord(c) ^ ord(password[i % len(password)])) for i, c in enumerate(text))
    return encrypted_text

# Decrypt message with password
def decrypt_text(encrypted_text, password):
    decrypted_text = "".join(chr(ord(c) ^ ord(password[i % len(password)])) for i, c in enumerate(encrypted_text))
    return decrypted_text

# Encode text into image
def encode_image(image_path, secret_text, password, output_image="encoded.png"):
    img = Image.open(image_path)
    pixels = img.load()
    
    encrypted_text = encrypt_text(secret_text, password)
    binary_secret = text_to_binary(encrypted_text) + '1111111111111110'  # EOF marker
    data_index = 0
    binary_length = len(binary_secret)

    for y in range(img.height):
        for x in range(img.width):
            if data_index < binary_length:
                r, g, b = pixels[x, y]

                r = (r & 0xFE) | int(binary_secret[data_index])  
                data_index += 1
                
                if data_index < binary_length:
                    g = (g & 0xFE) | int(binary_secret[data_index])
                    data_index += 1
                
                if data_index < binary_length:
                    b = (b & 0xFE) | int(binary_secret[data_index])
                    data_index += 1
                
                pixels[x, y] = (r, g, b)

    img.save(output_image)
    print(f"{Fore.GREEN}[✔] Secret text encoded successfully in {output_image}{Style.RESET_ALL}")

# Decode text from image
def decode_image(image_path, password):
    img = Image.open(image_path)
    pixels = img.load()

    binary_data = ""
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

    binary_data = binary_data.split('1111111111111110')[0]  # Stop at EOF marker
    encrypted_text = binary_to_text(binary_data)

    try:
        hidden_text = decrypt_text(encrypted_text, password)
        print(f"{Fore.CYAN}[✔] Decoded text: {hidden_text}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}[✘] YOU ARE NOT AUTH{Style.RESET_ALL}")

# Main Program
def main():
    print_banner()
    
    print(f"{Fore.YELLOW}[1] Encode a message")
    print(f"[2] Decode a message{Style.RESET_ALL}")
    choice = input("\nEnter your choice (1 or 2): ").strip()

    if choice == "1":
        msg = input("Enter secret message: ")
        password = input("Enter a passcode: ")
        image_path = input("Enter full path of the image: ")

        if not os.path.exists(image_path):
            print(f"{Fore.RED}[✘] Image not found! Please check the path.{Style.RESET_ALL}")
            return
        
        encode_image(image_path, msg, password)

    elif choice == "2":
        image_path = input("Enter full path of the image: ")
        password = input("Enter the passcode: ")

        if not os.path.exists(image_path):
            print(f"{Fore.RED}[✘] Image not found! Please check the path.{Style.RESET_ALL}")
            return

        decode_image(image_path, password)

    else:
        print(f"{Fore.RED}[✘] Invalid choice! Please enter 1 or 2.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
