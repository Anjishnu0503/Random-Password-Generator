# Random Password Generator
# Overview


# Table of Contents
- Features
- Installation
- Usage
- Code Explanation
   - Libraries Used
   - Functions
   - Customization
- Contributing
- License

# Features
- Generate passwords of customizable lengths (8 to 24 characters).
- Choose from four different password strengths: Poor, Average, Hard, and Advanced.
- Simple and intuitive graphical user interface (GUI).
- Display the generated password in a separate window.

# Installation
1. Ensure you have Python 3.x installed on your machine.

2. Install Tkinter if it's not already installed. For most Python installations, Tkinter comes pre-installed. You can check if it is available by running:
```bash
python -m tkinter
```
3. Clone the repository or download the source code:
```bash
git clone https://github.com/yourusername/random-password-generator.git
cd random-password-generator
```
# Usage
To run the password generator, simply execute the script:
```bash 
python password_generator.py
```
## Instruction
1. Choose the desired password strength using the radio buttons (Poor, Average, Hard, Advanced).
2. Set the desired password length using the spinbox (from 8 to 24 characters).
3. Click the "Generate Password" button to create a new password.
4. The generated password will appear in a new window.

# Code Explanation
## Libraries Used
1. tkinter: The standard GUI toolkit for Python, used to create the application's interface.
2. random: A module for generating random numbers and selecting random items from sequences.
3. string: A module providing easy access to common string constants, such as ASCII characters.

## Functions
- passgen():
   - Generates a password based on the selected strength and length.
   - Logic:
      - If "Poor" is selected, it uses uppercase and lowercase letters.
      - If "Average" is selected, it includes lowercase letters and digits.
      - If "Hard" is selected, it includes lowercase letters, uppercase letters, and digits.
      - If "Advanced" is selected, it includes lowercase letters, uppercase letters, digits, and punctuation.
- callback():
   - Retrieves the generated password from passgen() and updates the UI.
- password_window(password):
   - Creates a new window to display the generated password.
- select():
   - Updates the selected password strength based on user input.

## GUI Components
- Radio Buttons: Allow users to select the desired password strength.
- Spinbox: Enables users to specify the length of the password.
- Labels: Display static text and the generated password.
- Button: Initiates the password generation process.

# Contribution
Contributions are welcome! If you have suggestions for improvements or new features, please create a pull request or open an issue in the repository.

# License
MIT License Copyright (c) 2024 Anjishnu0503

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
