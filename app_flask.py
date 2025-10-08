from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

## Continue o código aqui.


@app.route("/soma")
def soma():
    valor1 = float(request.args.get('valor1'))
    valor2 = float(request.args.get('valor2'))
    return {"resultado":valor1+valor2}


@app.route("/subtrair")
def subtracao():
    valor1 = float(request.args.get('valor1'))
    valor2 = float(request.args.get('valor2'))
    return {"resultado":valor1-valor2}


@app.route("/multiplicar")
def multiplicacao():
    valor1 = float(request.args.get('valor1'))
    valor2 = float(request.args.get('valor2'))
    return {"resultado":valor1*valor2}


@app.route("/dividir")
def divisao():
    valor1 = float(request.args.get('valor1'))
    valor2 = float(request.args.get('valor2'))
    if valor2 == 0:
        return {"erro": "Divisão por zero não é permitida"}

    return {"resultado":valor1/valor2}


if __name__ == "__main__":
    app.run(debug=True)
