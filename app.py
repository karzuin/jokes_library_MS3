import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_jokes")
def get_jokes():
    jokes = list(mongo.db.jokes.find())
    if "user" in session:
        users_bookmark = list(mongo.db.users.find_one(
            {"username": session["user"]})["users_bookmark"])
        return render_template(
            "jokes.html", jokes=jokes, users_bookmark=users_bookmark)
    return render_template("jokes.html", jokes=jokes)


@app.route("/coll_bookmarks/<username>", methods=["GET", "POST"])
def coll_bookmarks(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    users_bookmark = mongo.db.users.find_one(
            {"username": session["user"]})["users_bookmark"]

    bookmark_jokes = []
    for bookmark in users_bookmark:
        joke = mongo.db.jokes.find_one({'_id': ObjectId(bookmark)})
        bookmark_jokes.append(joke)
    return render_template(
        "coll_bookmarks.html", username=username.title(),
        users_bookmark=users_bookmark, bookmark_jokes=bookmark_jokes,
        joke=joke)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    jokes = list(mongo.db.jokes.find({"$text": {"$search": query}}))
    return render_template("jokes.html", jokes=jokes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
    # to check if username already exists in Mongo DB
        existing_user = mongo.db.users.find_one(
        {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "users_bookmark": []
        }
        mongo.db.users.insert_one(register)

        # put the user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                         "coll_bookmarks", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist. indentation is inline with existing user
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_joke", methods=["GET", "POST"])
def add_joke():
    if request.method == "POST":
        joke = {
            "category_name": request.form.get("category_name"),
            "joke_description": request.form.get("joke_description"),
            "created_by": request.form.get("created_by"),
            "like": "",
            "dislike": ""
        }
        mongo.db.jokes.insert_one(joke)
        flash("Joke Successfully Added")
        return redirect(url_for("get_jokes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_joke.html", categories=categories)


@app.route("/edit_joke/<joke_id>", methods=["GET", "POST"])
def edit_joke(joke_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "joke_description": request.form.get("joke_description"),
            "created_by": request.form.get("created_by"),
        }
        mongo.db.jokes.update({"_id": ObjectId(joke_id)}, submit)
        flash("Joke Successfully Updated")

    joke = mongo.db.jokes.find_one({"_id": ObjectId(joke_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_joke.html", joke=joke, categories=categories)


@app.route("/delete_joke/<joke_id>")
def delete_joke(joke_id):
    mongo.db.jokes.remove({"_id": ObjectId(joke_id)})
    flash("Joke Successfully Deleted")
    return redirect(url_for("get_jokes"))


@app.route("/add_bookmark/<joke_id>", methods=["GET", "POST"])
def add_bookmark(joke_id):
    mongo.db.users.find_one_and_update(
        {"username": session["user"].lower()},
        {"$push": {"users_bookmark": ObjectId(joke_id)}})
    flash("Bookmark is Saved!")
    return redirect(url_for("get_jokes"))


@app.route("/remove_bookmark/<joke_id>", methods=["GET", "POST"])
def remove_bookmark(joke_id):
    mongo.db.users.find_one_and_update(
        {"username": session["user"].lower()},
        {"$pull": {"users_bookmark": ObjectId(joke_id)}})
    flash("Bookmark is Removed!")
    return redirect(url_for("get_jokes"))


@app.route("/like/<joke_id>", methods=["GET", "POST"])
def like(joke_id):
    joke = mongo.db.jokes.find_one_and_update(
        {"_id": ObjectId(joke_id)}, {"$inc": {"like": 1}})
    return redirect(url_for("get_jokes", joke=joke))


@app.route("/dislike/<joke_id>", methods=["GET", "POST"])
def dislike(joke_id):
    joke = mongo.db.jokes.find_one_and_update(
        {"_id": ObjectId(joke_id)}, {"$inc": {"dislike": 1}})
    return redirect(url_for("get_jokes", joke=joke))


@app.route("/family_jokes")
def family_jokes():
    jokes = list(mongo.db.jokes.find({"category_name": "Family Jokes"}))
    return render_template(
        "family_jokes.html", jokes=jokes)


@app.route("/food_jokes")
def food_jokes():
    jokes = list(mongo.db.jokes.find({"category_name": "Food Jokes"}))
    return render_template(
        "food_jokes.html", jokes=jokes)


@app.route("/insult_jokes")
def insult_jokes():
    jokes = list(mongo.db.jokes.find({"category_name": "Insult Jokes"}))
    return render_template(
        "insult_jokes.html", jokes=jokes)


@app.route("/word_jokes")
def word_jokes():
    jokes = list(mongo.db.jokes.find({"category_name": "Word Play Jokes"}))
    return render_template(
        "word_jokes.html", jokes=jokes)


@app.route("/relationship_jokes")
def relationship_jokes():
    jokes = list(mongo.db.jokes.find({"category_name": "Relationship Jokes"}))
    return render_template(
        "relationship_jokes.html", jokes=jokes)


@app.route("/yo_jokes")
def yo_jokes():
    jokes = list(mongo.db.jokes.find({"category_name": "Yo Momma Jokes"}))
    return render_template(
        "yo_jokes.html", jokes=jokes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
