from flask import Flask, render_template_string, request
import pickle
import pandas as pd

app = Flask(__name__)

with open("trained_model.pkl", "rb") as file:
    model = pickle.load(file)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Performance Predictor</title>
    <style>
        body {
            font-family: Arial;
            background: #eef2f7;
            text-align: center;
            padding: 30px;
        }
        .container {
            background: white;
            max-width: 450px;
            margin: auto;
            padding: 25px;
            border-radius: 12px;
        }
        input {
            width: 90%;
            padding: 10px;
            margin: 8px;
        }
        button {
            background: #1f4e79;
            color: white;
            padding: 12px 25px;
            border: none;
            cursor: pointer;
        }
        h1 { color: #1f4e79; }
        .result { color: green; font-size: 22px; }
    </style>
</head>
<body>
<div class="container">
    <h1>Student Performance Prediction</h1>
    <p>Enter student academic details</p>

    <form method="POST">
        <input type="number" name="age" placeholder="Age (15-22)" min="15" max="22" required>
        <input type="number" name="studytime" placeholder="Study Time (1-4)" min="1" max="4" required>
        <input type="number" name="failures" placeholder="Past Failures (0-4)" min="0" max="4" required>
        <input type="number" name="absences" placeholder="Absences" min="0" max="100" required>
        <input type="number" name="G1" placeholder="First Period Grade (0-20)" min="0" max="20" required>
        <input type="number" name="G2" placeholder="Second Period Grade (0-20)" min="0" max="20" required>
        <br><br>
        <button type="submit">Predict Final Grade</button>
    </form>

    {% if prediction is not none %}
        <h2 class="result">Predicted Grade: {{ prediction }}/20</h2>
        <h3>{{ status }}</h3>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    status = ""

    if request.method == "POST":
        values = [[
            int(request.form["age"]),
            int(request.form["studytime"]),
            int(request.form["failures"]),
            int(request.form["absences"]),
            int(request.form["G1"]),
            int(request.form["G2"])
        ]]

        data = pd.DataFrame(values, columns=[
            "age", "studytime", "failures", "absences", "G1", "G2"
        ])

        prediction = round(float(model.predict(data)[0]), 2)
        status = "Likely to Pass" if prediction >= 10 else "May Need Improvement"

    return render_template_string(HTML, prediction=prediction, status=status)

if __name__ == "__main__":
    app.run(debug=True)