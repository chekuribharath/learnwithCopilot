
from flask import Flask, render_template, request, Markup
import sys
import os
import re

# Add the parent directory to sys.path so we can import Err.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Err  # Import your Err.py as a module


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'change_this_secret_key')

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        name = request.form.get("name", "")
        # Sanitize input: allow only letters, spaces, and hyphens
        name = re.sub(r'[^a-zA-Z\s-]', '', name)
        # Validation: max 10 chars, no numbers
        if len(name) > 10:
            error = "Name must not be longer than 10 characters."
        elif re.search(r'\d', name):
            error = "Name must not contain numbers."
        elif not name.strip():
            error = "Name cannot be empty."
        else:
            from io import StringIO
            import contextlib
            buf = StringIO()
            with contextlib.redirect_stdout(buf):
                Err.greet(name)
            result = Markup.escape(buf.getvalue().strip())
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
