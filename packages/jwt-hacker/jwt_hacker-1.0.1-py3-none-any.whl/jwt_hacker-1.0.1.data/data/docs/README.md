# JWT Decoder & Multi-Decoder Tool

Welcome to the **JWT Decoder & Multi-Decoder Tool**! This powerful Python-based application combines state-of-the-art decoding capabilities with a sleek hacker-themed GUI. Decode, decipher, and analyze JWT tokens and other encoded data effortlessly.

---

## 🚀 Features

- **JWT Token Decoding**: Automatically decodes JWT headers and payloads.
- **Multi-Decoder Support**:
  - Base64
  - Base58
  - Hexadecimal
  - URL Decoding
  - Gzip
  - Zlib
  - AES (decryption with a key)
  - RSA (requires private key)
  - And many more!
- **Thread-Safe GUI**: Ensures seamless decoding while preventing UI freezes.
- **Sci-Fi Hacker Theme**: Immerse yourself in a futuristic green-on-black interface.
- **Save Decoded Results**: Export your decoded output for further analysis.
- **Automatic Detection**: Automatically applies appropriate decoding techniques to pasted data.

---

## 🔧 Requirements

Ensure you have the following installed:

- Python 3.8+
- pip (Python package manager)

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## 🖥️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/JWT-Multi-Decoder.git
```

2. Navigate to the project directory:

```bash
cd JWT-Multi-Decoder
```

3. Installation Process:
_You may need to setup Python Environment first;_
```bash 
python3 -m venv venv

source venv/bin/activate
```
_Install the Requirements:
```bash
pip install -r requirements.txt
```

4. Run the tool:

```bash
python JWT_Decoder.py
```

---

## 🕹️ Usage

1. **Paste Your Encoded Data**:
   - Enter a JWT token or any encoded data in the input box.

2. **Decode**:
   - Press the `Decode` button to analyze and decode the data.

3. **Save Output**:
   - Save your decoded results for further use.

---

## 🎨 Screenshots

### Hacker-Themed GUI
![Screenshot of the GUI with black-and-green theme](screenshot.png)

---

## 📜 Supported Decoding Types

| Encoding Type      | Description                             |
|--------------------|-----------------------------------------|
| Base64             | Standard Base64 encoding.              |
| Base58             | Bitcoin-friendly encoding.             |
| Hexadecimal        | Converts hex strings to text.          |
| URL Decoding       | Decodes URL-encoded strings.           |
| Gzip               | Decompresses Gzip-compressed data.     |
| Zlib               | Decompresses Zlib-compressed data.     |
| AES (with key)     | AES decryption (key required).         |
| RSA (private key)  | RSA decryption (key required).         |
| JWT Parsing        | Parses JWT headers and payloads.       |
| Custom Decoding    | Easily extendable to more algorithms.  |

---

## 🛠️ Extending the Tool

1. **Add New Decoding Methods**:
   - Open the `decoder.py` file.
   - Add your decoding logic in the `Decoder` class.

2. **Customize the GUI**:
   - Modify the `JWT_Decoder.py` file to adjust the GUI theme and layout.

---

## 🤝 Contributions

We welcome contributions to improve the tool!

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
Please review the terms before using this software..

---

## 🌐 Connect

- [GitHub](https://github.com/GreyNodeSecurity)
- [Project Issues](https://github.com/GreyNodeSecurity/JWT-Multi-Decoder/issues)

---

### Made with ❤️ by [Grey Node Security](https://greynodesecurity.com)
