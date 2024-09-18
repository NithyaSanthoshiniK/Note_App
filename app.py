from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# A list to store the notes
notes = []

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/thankyou', methods=["POST"])
def thankyou():
    # To Get the note from the form
    note = request.form.get("note")
    if note:
        notes.append(note)
    return render_template("thankyou.html")

@app.route('/viewnotes', methods=["GET"])
def view_notes():
    # To Display all the notes
    return render_template("viewnotes.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
