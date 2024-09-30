


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


# Homework Helper App | Goal of this project...

Many applications available on the Android Store are designed to assist students with a variety of problems across different categories. The goal of CortaAI was not only to facilitate my entry into the app development ecosystem but also to create an application capable of addressing virtually any problem effectively. This was achieved by using GPT-3.

#### Program Explanation

#### User Interface

A minimalistic and user-friendly interface was designed using the Kivy UI framework. It features a text input field for users to enter their queries, and a microphone icon and an instructional label prompting users to "Enter text to start...". The interface includes two buttons: a "Submit" button to send the user's input to the AI and a "Clear" button to reset the input and output fields. The design emphasizes a clean aesthetic with a blue-gray theme and includes a logo image at the top for branding. Responses from the AI are displayed in a flat button format, enhancing readability while ensuring a smooth user experience.

## Back-end Processes

The back-end program is a hosted web application that communicates with the front-end app on Android using HTTP requests, specifically handling both GET and POST requests. The function `respond()` retrieves user input from the query parameter text using `request.args.get("text", None)`. This is how the front end sends data to the server. After the input is processed, the response is sent back to the front end in JSON format using `jsonify(response)`. This allows the front end to easily parse and display the response.

#### Problem Solving Method
Depending on whether the input is identified as a math problem or not, the program prepares different prompts for GPT-3:
- If it is a math problem, it constructs a prompt for math-related queries using prompt_chat_math.
- If it is not a math problem, it uses a general prompt defined in prompt_chat_wordbased.
The constructed prompt includes the user's input and asks GPT-3 for a response.


## Deployment
This program was deployed using Flask and hosted on the [PythonAnywhere platform](https://www.pythonanywhere.com/).

Get API key at https://products.wolframalpha.com/api

Download python packages

```bash
    pip install -r requirements.txt
```

## Links

➊ Github: https://github.com/AumkarMali/

➋ Youtube: https://www.youtube.com/channel/UC7rhCKur9bF01lV0pNJNkvA
## Demo

https://www.youtube.com/watch?v=5zzBfvukYqk

## Documentation

[Documentation](hhttps://reference.wolfram.com/language/ref/WolframAlpha)
[Buildozer](https://readthedocs.org/projects/buildozer/downloads/pdf/latest/#:~:text=Buildozer%20manages%20a%20file%20named,Android%2C%20iOS%2C%20and%20more)


## Authors

- [@AumkarMali](https://www.github.com/AumkarMali)

