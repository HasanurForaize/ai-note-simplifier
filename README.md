# AI Note Simplifier

A simple Flask web app that simplifies university notes into plain, easy English using the OpenAI API.

---

## Project Structure

```
ai-note-simplifier/
├── app.py               ← Flask backend
├── templates/
│   └── index.html       ← Frontend (HTML + CSS)
├── requirements.txt     ← Python dependencies
├── .env.example         ← Template for your API key
├── .gitignore           ← Files to exclude from GitHub
└── README.md            ← This file
```

---

## Part 1 — Run Locally

### Step 1 — Make sure Python is installed
Open Terminal and run:
```bash
python3 --version
```
You should see Python 3.x. If not, download it from https://python.org

---

### Step 2 — Open the project folder in Terminal
```bash
cd Desktop/ai-note-simplifier
```

---

### Step 3 — Create a virtual environment
```bash
python3 -m venv venv
```

Activate it:
- **Mac / Linux:**
  ```bash
  source venv/bin/activate
  ```
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

---

### Step 4 — Install dependencies
```bash
pip install -r requirements.txt
```

---

### Step 5 — Add your OpenAI API key

1. Copy `.env.example` and rename the copy to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` in any text editor and replace `your_openai_api_key_here` with your real key:
   ```
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
   ```

You can get an API key at: https://platform.openai.com/api-keys

---

### Step 6 — Run the app
```bash
python app.py
```

Open your browser and go to: **http://127.0.0.1:5000**

---

## Part 2 — Upload to GitHub

### Step 1 — Create a new repository on GitHub
1. Go to https://github.com and log in.
2. Click the **+** button → **New repository**.
3. Name it `ai-note-simplifier`.
4. Leave it **Public** (or Private if your professor allows it).
5. Do **NOT** tick "Add a README" — you already have one.
6. Click **Create repository**.

---

### Step 2 — Push your code from Terminal

Run these commands one by one inside your project folder:

```bash
git init
git add .
git commit -m "Initial commit - AI Note Simplifier"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-note-simplifier.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

> Your `.env` file is listed in `.gitignore` so it will NOT be uploaded. Your API key stays private.

---

## Part 3 — Submit on Brightspace

1. Copy your GitHub repository link, e.g.:
   `https://github.com/YOUR_USERNAME/ai-note-simplifier`
2. Log in to Brightspace.
3. Go to your assignment submission page.
4. Paste the GitHub link in the text field.
5. Click **Submit**.

---

## Technologies Used

- Python 3
- Flask
- OpenAI API (gpt-3.5-turbo)
- HTML / CSS
- python-dotenv
