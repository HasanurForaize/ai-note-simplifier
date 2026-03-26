# AI Note Simplifier

---

## The Problem

As a university student, I found myself spending way too much time trying to understand long, complicated lecture notes. Sometimes the notes are full of technical terms, dense paragraphs, or just written in a way that is hard to follow especially when you are revising the night before an exam and I belive many student face this issues when exams are so near and they need to complete chapters and revise when exam hits.

A lot of students deal with this. We copy down notes in class, or download a lecture PDF, and then later you sit there reading the same paragraph three times trying to figure out what it actually means. It slows down your study time and makes revision stressful.

I wanted a simple tool that could take those confusing notes and just explain them in plain English — without changing what they mean.

---

## The Solution

AI Note Simplifier is a web app where you paste your notes, click a button, and get back a simpler, easier-to-understand version of the same content.

It uses the OpenAI API in the background to rewrite your notes into clear, everyday English. The key idea is that it does not add new information or make things up, it just takes what you wrote and explains it more simply. That way you are not learning something wrong, you are just reading it in a way that is easier to understand.

---

## How the Application Works

Using the app is straightforward:

1. **Open the app** in your browser
2. **Paste your notes** into the large text box on the page
3. **Click the "Simplify Notes" button**
4. The app sends your notes to the OpenAI API with instructions to simplify the language
5. **The simplified version appears** on the same page below the button
6. If you leave the text box empty and click the button, the app shows an error message asking you to enter something first

The whole process takes a few seconds. You get back the same information, just written in a way that is much easier to read and understand.

---

## Technologies Used

- **Python** — the main programming language used for the backend
- **Flask** — a lightweight Python web framework used to build and run the app
- **HTML** — used to build the structure of the web page
- **CSS** — used to style the page and make it look clean and simple
- **OpenAI API** — used to process the notes and return a simplified version
- **python-dotenv** — used to securely load the API key from a `.env` file

---

## Features

- Paste any notes and get a simplified version in seconds
- Clean and simple interface that is easy to use
- Keeps the original meaning of the notes — does not add or remove important information
- Shows an error message if the text box is left empty
- Your notes stay in the text box after you click the button so you can compare both versions
- API key is stored securely and never uploaded to GitHub

---

## How to Run the Application

Follow these steps to run the app on your own computer:

**1. Clone or download the project**
```bash
git clone https://github.com/HasanurForaize/ai-note-simplifier.git
cd ai-note-simplifier
```

**2. Create and activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install the required packages**
```bash
pip install -r requirements.txt
```

**4. Add your OpenAI API key**

Create a file called `.env` in the project folder and add this line:
```
OPENAI_API_KEY=your_api_key_here
```
You can get a free API key from https://platform.openai.com/api-keys

**5. Run the app**
```bash
python app.py
```

**6. Open in your browser**

Go to: `http://127.0.0.1:5000`

The app should now be running and ready to use.

---

## Project Structure

```
ai-note-simplifier/
├── app.py               ← Flask backend
├── templates/
│   └── index.html       ← Frontend (HTML + CSS)
├── requirements.txt     ← List of dependencies
├── .env.example         ← Template for the API key
├── .gitignore           ← Stops .env from being uploaded
└── README.md            ← This file
```

---
