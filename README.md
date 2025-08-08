<img width="3188" height="1202" alt="frame (3)" src="https://github.com/user-attachments/assets/517ad8e9-ad22-457d-9538-a9e62d137cd7" />


# The Un-Linguist 🤖🎯


## Basic Details
### Team Name: Errors


### Team Members
- Team Lead: Kailas M S - Sahrdaya College of Engineering and Technology(Autonomous)
- Member : Mohammed Roshan A N - Sahrdaya College of Engineering and Technology(Autonomous)

### Project Description
A web app that takes perfectly coherent AI-generated responses… and then gleefully scrambles them into a chaotic mess of multilingual gibberish. Sometimes it’s French, sometimes it’s Russian, sometimes it’s just confusion in a trench coat.

### The Problem (that doesn't exist)
The world suffers from too much clarity in communication. Messages are being understood, conversations are flowing smoothly, and misunderstandings are at an all-time low. Disgusting.

### The Solution (that nobody asked for)
We inject glorious confusion into AI responses by translating them into random languages sentence-by-sentence and adding optional ciphered text to keep everyone guessing. It’s like Google Translate on a roller coaster.

## Technical Details
### Technologies/Components Used
For Software:
-Languages: Python, HTML, CSS
-Frameworks: Django
-Libraries: OpenAI API (via OpenRouter), NLTK, Requests, python-dotenv, LibreTranslate API
-Tools: Docker (for LibreTranslate), Git, VS Code
For Hardware:
- A working laptop
-A stable internet connection (sometimes stable, mostly not)
-A brain that enjoys chaos



### Implementation
For Software:

Installation
bash
Copy
Edit
git clone https://github.com/your-repo/unlinguist.git
cd unlinguist
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Run
bash
Copy
Edit
# Start LibreTranslate (Docker)
docker run -ti --rm -p 5080:5000 libretranslate/libretranslate

# Run Django server
python manage.py runserver
### Project Documentation
For Software:

# Screenshots (Add at least 3)
<img width="827" height="882" alt="image" src="https://github.com/user-attachments/assets/ee2cfae3-b2fb-4ee4-b8fe-e28804bacc2f" />

First Visit
The user opens the page and sees:

A title/header like "The Un-Linguist".

A text box inviting them to type anything they want.

A “Send” button below the box.

The page looks clean and minimal, with enough spacing so the main focus is on the input.

<img width="767" height="892" alt="image" src="https://github.com/user-attachments/assets/203521e0-b8e7-4929-94f2-3067af02cee5" />

The user types something like:
Hello, how are you today?
The typing area behaves like any normal input field — they can edit, delete, or paste text.
Absurd Multilingual Output
The same answer, but jumbled through multiple languages and back.

It looks weird, mismatched, and funny.

<img width="777" height="895" alt="image" src="https://github.com/user-attachments/assets/2714a746-4ca8-4092-a530-18f788b21667" />
Morse Code
The answer is also shown in Morse code.

<img width="532" height="912" alt="image" src="https://github.com/user-attachments/assets/8e9ca83e-9f9c-4272-9e83-b33df047550d" />

Clue to solve the morse code

<img width="786" height="892" alt="image" src="https://github.com/user-attachments/assets/224c2f9c-4d0f-475a-ae12-e84ac5ff2af2" />

 AI’s Coherent Response



WorkflowDiagrams
<img width="1227" height="547" alt="image" src="https://github.com/user-attachments/assets/a4c53758-342e-4084-9883-8f77a2889fda" />

┌─────────────┐
│   User      │
│ (Web Form)  │
└─────┬───────┘
      │
      ▼
┌───────────────────────────┐
│ Django View: index(request)│
│ - Handles POST form input  │
└───────────┬───────────────┘
            │
            ▼
┌─────────────────────────────┐
│ generate_response()         │
│ - Calls OpenRouter API       │
│ - Sends user message         │
│ - Receives AI response       │
└───────────┬─────────────────┘
            │
            ▼
┌─────────────────────────────┐
│ jumble_translate()          │
│ - Sends AI text to LibreTranslate│
│ - Multiple translations + jumble │
└───────────┬─────────────────┘
            │
            ▼
┌─────────────────────────────┐
│ extra fun:                  │
│ - additive_shift_cipher()    │
│ - morse_code() + clue        │
└───────────┬─────────────────┘
            │
            ▼
┌───────────────────────────┐
│ Django Template (index.html)│
│ - Shows:                    │
│   1. Absurd multilingual text│
│   2. Ciphered output         │
│   3. Morse code + clue       │
└───────────┬─────────────────┘
            │
            ▼
┌─────────────┐
│   User      │
│ Laughs /    │
│ Gets Confused│
└─────────────┘



<img width="796" height="888" alt="image" src="https://github.com/user-attachments/assets/05ea6f51-30c0-4340-a83d-806c25a6fde2" />



### Project Demo
# Video

https://github.com/user-attachments/assets/a7c61a25-9ff4-4f1c-b100-e348c0197a11
When a user visits The Un-Linguist web app, they are greeted with a clean and minimal interface featuring a text input box and a “Send” button. The user simply types any message — from casual greetings to curious questions — and submits it. Upon submission, the page refreshes to display three distinct outputs: a coherent AI-generated response, a humorously distorted “absurd multilingual” version created by passing the original reply through multiple translations, and a Morse code version accompanied by a small decoding clue. This simple yet quirky interface allows the user to repeatedly input new messages and instantly see these playful transformations without any complicated navigation or clutter.

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
Team Contributions
Kailas M S: Django backend setup, API integration, LibreTranslate Docker wizardry.
Mohammed Roshan A N: NLTK setup, GPT prompt engineering, cipher & chaos logic, frontend design.


---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--25-25?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)



