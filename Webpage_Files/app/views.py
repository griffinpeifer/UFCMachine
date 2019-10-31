from app import app
from flask import render_template, request, redirect, jsonify, make_response
from machine_learning import predict, loaded_model
import sqlite3
import pandas as pd


@app.route("/")
def index():
    return redirect("/login")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# Here you are passing python objects into and html page.
@app.route("/jinja")
def jinja():
    age = 18
    name = "eddie"
    list = ["Da", "Py", "God"]
    dict = {"name": "eddie", "age": 25}
    return render_template("jinja.html", name=name, list=list, dict=dict, age=age)


experiment = {}


# Here you are capturing input data and then manipulating it in the function definition
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":

        req = request.form
        username = str(req["username"])
        password = str(req["password"])

        missing = list()
df.to_csv(index=False)z
        for k, v in req.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("sign_up.html", feedback=feedback)

        # for k, v in req.items():
        #     if v != "":
        #
        # experiment.update(
        #     {req['username']: {"name": req["name"], "email": req["email"], "password": req["password"]}}
        # )

        if not missing:
            conn = sqlite3.connect("login_credentials")
            c = conn.cursor()
            c.execute("""INSERT INTO login_creds(username, password) VALUES (?, ?)""",
                      (username, password))
            conn.commit()
            c.close()
            conn.close()
            # c.execute('SELECT * FROM login_creds')
            # for row in c.fetchall():
            #     print(row)

            print(experiment)

            access_granted = f"Hey there {username} you have successfully been signed up! Go ahead and log in."

            # return redirect(request.url, access_granted=access_granted)
            return render_template("sign_in.html", access_granted=access_granted)

    return render_template("sign_up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        conn = sqlite3.connect("login_credentials")
        c = conn.cursor()
        c.execute('SELECT * FROM login_creds')

        req = request.form

        username = str(req["username"])
        password = str(req["password"])
        data = c.fetchall()

        if (username, password) in data:
            c.close()
            conn.close()
            return redirect("/main_page")

        elif (username, password) not in data:
            feedback = f"Incorrect email or password please try again"
            return render_template("sign_in.html", feedback=feedback)

    return render_template("sign_in.html")


@app.route("/main_page", methods=["GET", "POST"])
def main_page():
    if request.method == "POST":
        req = request.form
        fighter1 = str(req["fighter1"])
        fighter2 = str(req["fighter2"])

        red = fighter1
        blue = fighter2

        prediction = predict(loaded_model, red, blue)
        prediction2 = predict(loaded_model, blue, red)

        fighter1_avg = (prediction + (1 - prediction2)) / 2
        fighter2_avg = (prediction2 + (1 - prediction)) / 2

        prediction_f1 = int(round(fighter1_avg[0][0] * 100))
        prediction_f2 = int(round(fighter2_avg[0][0] * 100))

        tale_df = pd.read_csv("tale_df.csv")
        df_q_red = tale_df.query(f'Name == "{fighter1}"')
        r_weight_class = df_q_red["Weight Class"].values[0]
        r_weight = df_q_red["Weight:"].values[0]
        r_height = df_q_red["Height:"].values[0]
        r_reach = df_q_red["Reach:"].values[0]
        r_age = df_q_red["Age"].values[0]
        r_wins = df_q_red["Wins"].values[0]
        r_losses = df_q_red["Losses"].values[0]
        r_draws = df_q_red["Draws"].values[0]

        df_q_blue = tale_df.query(f'Name == "{fighter2}"')
        b_weight_class = df_q_blue["Weight Class"].values[0]
        b_weight = df_q_blue["Weight:"].values[0]
        b_height = df_q_blue["Height:"].values[0]
        b_reach = df_q_blue["Reach:"].values[0]
        b_age = df_q_blue["Age"].values[0]
        b_wins = df_q_blue["Wins"].values[0]
        b_losses = df_q_blue["Losses"].values[0]
        b_draws = df_q_blue["Draws"].values[0]


        return render_template("main_page.html", red=prediction_f1, blue=prediction_f2,
                               red_name=fighter1, blue_name=fighter2,

                               r_weight_class=r_weight_class, r_age=r_age, r_height=r_height,
                               r_weight=r_weight, r_reach=r_reach, r_wins=r_wins, r_losses=r_losses, r_draws=r_draws,

                               b_weight_class=b_weight_class, b_age=b_age, b_height=b_height,
                               b_weight=b_weight, b_reach=b_reach, b_wins=b_wins, b_losses=b_losses, b_draws=b_draws)

    return render_template("main_page.html")


# @app.route("/profile/<username>")
# def profile(username):
#     user = users[username]
#     return render_template("profile.html", username=username, user=user)


@app.route("/json", methods=["POST"])
def json():
    if request.is_json:

        req = request.get_json()

        print(req)

        response = {"message": "JSON Recieved!",
                    "name": req.get("name")}

        res = make_response(jsonify(response), 200)

        return res

    else:
        return "JSON not recieved!", 400


# @app.route("/guestbook")
# def guestbook():
# Receive JSON, returning a response object asynchronously.
@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():
    req = request.get_json()

    print(req)

    res = make_response(jsonify({"message": "OK"}), 200)

    return res
