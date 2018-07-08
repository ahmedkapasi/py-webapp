from flask import *

app = Flask(__name__)

students = []
students.append({"name": "ahmed", "age": "33", "address": "hyderabad"})
students.append({"name": "mufaddal", "age": "22", "address": "hyderabad"})

@app.route('/', methods=["GET", "POST"])
def start_page():
    try:
        if request.method == "POST":
            name = request.form.get("name", "")
            age = request.form.get("age", "")
            address = request.form.get("address")
            dic = {"name": name, "age": age, "address": address}
            students.append(dic)
            return redirect(url_for("start_page"))
        return render_template("index.html",students=students)
    except KeyError:
        print("some error occured")

app.run(debug=True)
