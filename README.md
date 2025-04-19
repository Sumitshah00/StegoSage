# StegoSage

# Steganography Tool

A simple Python-based steganography tool to encode and decode hidden messages in images.

## Features
- Hide secret messages inside images.
- Retrieve hidden messages from encoded images.
- Secure messages using a passcode.

## Requirements
Ensure you have Python installed (preferably Python 3.x). The following Python modules are required:

```sh
pip install pillow
```

## Usage

### Encoding a Message
To hide a message inside an image:

1. Run the script:
   ```sh
   python main.py
   ```
2. Select option `[1] Encode a message`.
3. Enter the full path of the image.
4. Type your secret message.
5. Set a passcode to secure the hidden message.
6. The encoded image will be saved as `encoded.png` in the same directory.

### Decoding a Message
To retrieve a hidden message from an encoded image:

1. Run the script:
   ```sh
   python main.py
   ```
2. Select option `[2] Decode a message`.
3. Enter the full path of the encoded image.
4. Provide the correct passcode.
5. If the passcode is correct, the hidden message will be displayed.

## Fixing File Permission Issues
If you get an error like `[✘] Image not found! Please check the path.` even when the file exists, you might need to adjust the file permissions. Run:

```sh
chmod +r /path/to/image.png
```

For example:
```sh
chmod +r /home/sumit/Desktop/stenography/encoded.png
```
This ensures the script has read access to the file.

## Example Output

```
Dev    :- sumit shah
Version :- 0.0.1

[1] Encode a message
[2] Decode a message

Enter your choice (1 or 2): 2
Enter full path of the image: /home/sumit/Desktop/stenography/encoded.png
Enter the passcode: 123
[✔] Decoded text: hey its sumit
```


---
Developed by sumit shah (HACKSAGE)

