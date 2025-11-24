from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, soy Mateo Guerrón y este es mi pipeline CI/CD"

def multiplicar(a, b):
    return a * b

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
