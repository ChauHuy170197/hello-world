from flask import flask
app = flask(_name_)
@app.route("/")
def index():
    return "Chào mọi người"
@app.route("/)
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3) 
        return str(fahrenheit)
    except ValueError:
        return "invalid input"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True
