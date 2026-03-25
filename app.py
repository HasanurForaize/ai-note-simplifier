import os
from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Create the OpenAI client using your API key from .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@app.route("/", methods=["GET", "POST"])
def index():
    simplified = None
    original = ""
    error = None

    if request.method == "POST":
        original = request.form.get("notes", "").strip()

        # Show error if the text box is empty
        if not original:
            error = "Please paste some notes before clicking Simplify."
        else:
            try:
                # Send notes to OpenAI and ask it to simplify them
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a helpful assistant that simplifies university notes. "
                                "Rewrite the notes in plain, easy English. "
                                "Keep the original meaning. Do not add new information. "
                                "Make the text shorter and clearer."
                            ),
                        },
                        {
                            "role": "user",
                            "content": f"Please simplify these notes:\n\n{original}",
                        },
                    ],
                )
                # Extract the simplified text from the response
                simplified = response.choices[0].message.content

            except Exception as e:
                error = f"Something went wrong: {str(e)}"

    return render_template("index.html", simplified=simplified, original=original, error=error)


if __name__ == "__main__":
    app.run(debug=True)
