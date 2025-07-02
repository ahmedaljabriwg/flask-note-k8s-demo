from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

NOTES_DIR = "notes"
NOTES_FILE = os.path.join(NOTES_DIR, "notes.txt")

os.makedirs(NOTES_DIR, exist_ok=True)
if not os.path.exists(NOTES_FILE):
    with open(NOTES_FILE, "w") as f:
        pass  # Create empty file

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        note = request.form["note"]
        with open(NOTES_FILE, "a") as f:
            f.write(note + "\n")
    with open(NOTES_FILE, "r") as f:
        notes = f.readlines()
    return render_template_string("""
        <h1>My Notes</h1>
        <form method="POST">
            <input name="note">
            <input type="submit">
        </form>
        <pre>{{ notes }}</pre>
    """, notes="".join(notes))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
