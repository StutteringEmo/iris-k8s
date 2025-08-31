from flask import Flask, render_template, request
import numpy as np, pickle

app = Flask(__name__)
model = pickle.load(open("file_iris.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html", predict=None, form_vals={})

@app.route("/predict", methods=["POST"])
def predict():
    vals = {
        "Sepal_Length": float(request.form["Sepal_Length"]),
        "Sepal_Width":  float(request.form["Sepal_Width"]),
        "Petal_Length": float(request.form["Petal_Length"]),
        "Petal_Width":  float(request.form["Petal_Width"]),
    }
    pred = model.predict(np.array([[vals["Sepal_Length"], vals["Sepal_Width"],
                                    vals["Petal_Length"], vals["Petal_Width"]]]))[0]
    return render_template("index.html", predict=str(pred), form_vals=vals)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
