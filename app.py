from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <form action="/predict">
        <input name="text">
        <button type="submit">Analyze</button>
    </form>
    '''

@app.route("/predict")
def predict():
    text = request.args.get("text")

    if "good" in text:
        result = "Positive"
    else:
        result = "Negative"

    return result

app.run()