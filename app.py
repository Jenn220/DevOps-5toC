from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola Mundo desde Flask con Traefik! 🚀"

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=5000)
=======
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 824ec1edf6e18806712186d0d1bcbb4cc57c0a4a
