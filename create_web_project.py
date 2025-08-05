import os

project_root = os.path.join(os.getcwd(), "webapp")
templates_dir = os.path.join(project_root, "templates")

files = {
    os.path.join(project_root, "requirements.txt"): "Flask\n",
    os.path.join(project_root, "app.py"): '''from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
''',
    os.path.join(templates_dir, "index.html"): '''<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Flask WebApp</title>
</head>
<body>
    <h1>Hello, Flask!</h1>
    <p>This is your starter web project.</p>
</body>
</html>
'''
}

def main():
    os.makedirs(templates_dir, exist_ok=True)
    for path, content in files.items():
        with open(path, "w") as f:
            f.write(content)
    print("Web project scaffold created in ./webapp")
    print("To run your app:")
    print("  cd webapp")
    print("  pip install -r requirements.txt")
    print("  python3 app.py")
    print("To open in your browser (after running):")
    print('  $BROWSER http://localhost:5000/')

if __name__ == "__main__":
    main()