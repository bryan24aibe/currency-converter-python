from flask import Flask, render_template, request

app = Flask(__name__)

# Tasas de cambio predefinidas (USD como moneda base)
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
    "JPY": 110.0,
    "AUD": 1.35,
    "CAD": 1.25,
    "MXN": 20.0
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        amount = float(request.form["amount"])
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]
        
        # Realizamos la conversión usando las tasas predefinidas
        converted_amount = amount * exchange_rates[to_currency] / exchange_rates[from_currency]
        return render_template("index.html", exchange_rates=exchange_rates, converted_amount=converted_amount, 
                               amount=amount, from_currency=from_currency, to_currency=to_currency)
    
    return render_template("index.html", exchange_rates=exchange_rates)

if __name__ == "__main__":
    app.run(debug=True)
