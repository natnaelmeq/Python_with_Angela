from flask import Flask,render_template
import random
import datetime
import requests
app = Flask(__name__)




@app.route("/")
def home():
    random_num = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("test.html", rannum=random_num,yyyy=current_year)

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io/?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url= f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age= age_data["age"]
    return render_template("guess.html",age=age, name=name, gender = gender)

if __name__ == "__main__":
    app.run(debug=True)