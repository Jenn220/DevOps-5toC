from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>API de Operaciones con Flask 🚀</h1>"

@app.route('/suma/<int:a>/<int:b>')
def suma(a, b):
    resultado = a + b
    return jsonify({"operacion": "suma", "a": a, "b": b, "resultado": resultado})

@app.route('/resta/<int:a>/<int:b>')
def resta(a, b):
    resultado = a - b
    return jsonify({"operacion": "resta", "a": a, "b": b, "resultado": resultado})

@app.route('/multiplicar/<int:a>/<int:b>')
def multiplicar(a, b):
    resultado = a * b
    return jsonify({"operacion": "multiplicacion", "a": a, "b": b, "resultado": resultado})

@app.route('/dividir/<int:a>/<int:b>')
def dividir(a, b):
    if b == 0:
        return jsonify({"error": "No se puede dividir para cero"}), 400
    resultado = a / b
    return jsonify({"operacion": "division", "a": a, "b": b, "resultado": resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
