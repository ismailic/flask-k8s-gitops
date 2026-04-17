from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevOps Team 🚀 please welcome the New engineers  Yassine Jaml abou dalal, Marouan Jaram 3achiq El gharam, AZIZ AID HAMOU sadiq Imade abou Maed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
