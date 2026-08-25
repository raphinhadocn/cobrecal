from flask import Flask, render_template, request, send_from_directory
from calculadora import (
    metros_para_kg,
    kg_para_metros,
    calcular_btus
)

app = Flask(__name__)


# =========================================
# ROTAS PWA (Manifest, Service Worker e Ícones)
# =========================================

@app.route("/manifest.json")
def manifest():
    return send_from_directory("static", "manifest.json")


@app.route("/sw.js")
def service_worker():
    return send_from_directory("static", "sw.js")


@app.route("/icons/<path:filename>")
def custom_icons(filename):
    return send_from_directory("static/icons", filename)


# =========================================
# ROTA PRINCIPAL DO APLICATIVO
# =========================================

@app.route("/", methods=["GET", "POST"])
def inicio():

    resultado_cobre = None
    resultado_btus = None

    if request.method == "POST":

        tipo = request.form.get("tipo")

        # =========================
        # CALCULADORA DE COBRE
        # =========================

        if tipo == "cobre":

            operacao = request.form.get("operacao")
            bitola = request.form.get("bitola")

            if operacao == "metros_kg":

                metros = float(request.form.get("valor"))

                resultado_cobre = metros_para_kg(
                    bitola,
                    metros
                )

                resultado_cobre["operacao"] = "metros_kg"

            elif operacao == "kg_metros":

                kg = float(request.form.get("valor"))

                resultado_cobre = kg_para_metros(
                    bitola,
                    kg
                )

                resultado_cobre["operacao"] = "kg_metros"

        # =========================
        # CALCULADORA DE BTUS
        # =========================

        elif tipo == "btus":

            area = float(request.form.get("area"))
            pessoas = int(request.form.get("pessoas"))
            sol = request.form.get("sol") == "sim"

            resultado_btus = calcular_btus(
                area,
                pessoas,
                sol
            )

    return render_template(
        "index.html",
        resultado_cobre=resultado_cobre,
        resultado_btus=resultado_btus
    )


if __name__ == "__main__":
    app.run(debug=True)