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


'''
This function gets all the jokes from the database and
renders them onto the homepage.
If the user is signed in then their bookmarked jokes will
also appear on the homepage
'''


@app.route("/")
@app.route("/get_jokes")
def get_jokes():
    jokes = list(mongo.db.jokes.find())
    # credit the following code to CI Tutor Tim
    if "user" in session:  # checks if user is in session
        # finding the logged-in user and only getting their users_bookmark key
        users_bookmark = list(mongo.db.users.find_one(
            {"username": session["user"]})["users_bookmark"])
        # renders the template with the bookmarked jokes if user is logged in
        return render_template(
            "jokes.html", jokes=jokes, users_bookmark=users_bookmark)
        # otherwise renders the template with just jokes
    return render_template("jokes.html", jokes=jokes)


'''
The coll_bookmarks function finds all the users bookmarked
jokes to display on the collections page.
'''


@app.route("/coll_bookmarks/<username>", methods=["GET", "POST"])
def coll_bookmarks(username):
    # credit the following code to CI Tutor Johann
    # gets user and users bookmark list from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    users_bookmark = mongo.db.users.find_one(
            {"username": session["user"]})["users_bookmark"]
    #  loop through that list to find joke id in the users bookmark key
    #  and push to bookmark jokes collection.
    bookmark_jokes = []
    for bookmark in users_bookmark:
        joke = mongo.db.jokes.find_one({'_id': ObjectId(bookmark)})
        bookmark_jokes.append(joke)
    #  The bookmarked jokes are then rendered onto the template
    return render_template(
        "coll_bookmarks.html", username=username.title(),
        users_bookmark=users_bookmark, bookmark_jokes=bookmark_jokes,
        joke=joke)


'''
The search function searches through the jokes database matching
the query keyword and renders the joke(s) onto the homepage.
'''


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    jokes = list(mongo.db.jokes.find({"$text": {"$search": query}}))
    return render_template("jokes.html", jokes=jokes)


'''
The like function finds and updates the joke id and adds one
count each click.
'''


@app.route("/like/<joke_id>", methods=["GET", "POST"])
def like(joke_id):
    joke = mongo.db.jokes.find_one_and_update(
        {"_id": ObjectId(joke_id)}, {"$inc": {"like": 1}})
    return redirect(url_for("get_jokes", joke=joke))


'''
The dislike function finds and updates the joke id and adds one
count each click.
'''


@app.route("/dislike/<joke_id>", methods=["GET", "POST"])
def dislike(joke_id):
    joke = mongo.db.jokes.find_one_and_update(
        {"_id": ObjectId(joke_id)}, {"$inc": {"dislike": 1}})
    return redirect(url_for("get_jokes", joke=joke))


'''
The register function checks if the user already exists, if no,
creates a new user for the database.
'''


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
        return redirect(url_for("get_jokes", username=session["user"]))
    return render_template("register.html")


'''
The login function checks if username exists and checks password.
'''


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
                flash("Welcome, {}!".format(
                    request.form.get("username").capitalize()))
                return redirect(url_for(
                        "get_jokes", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist. indentation is inline with existing user
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


'''
The logout function removes user from session cookie.
'''


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("get_jokes"))


'''
The add joke function checks if the user is logged in,
if not redirects to log in. If yes, they fill in the form
and submits it to the database which then renders a
new joke onto the homepage.
'''


@app.route("/add_joke", methods=["GET", "POST"])
def add_joke():
    if "user" in session:
        # submits form to database
        if request.method == "POST":
            joke = {
                "category_name": request.form.get("category_name"),
                "joke_description": request.form.get("joke_description"),
                "like": 0,
                "dislike": 0
            }

            mongo.db.jokes.insert_one(joke)
            flash("Joke Successfully Added")
            return redirect(url_for("get_jokes"))
        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("add_joke.html", categories=categories)
    # validate user is logged in
    else:
        flash("Please log in")
        return redirect(url_for("login"))


'''
The edit joke function checks if the user is logged in, if no,
redirects them to the log in page. If yes, user fills in the form
and submits it to the database. The updated data is rendered onto
edit joke page.
'''


@app.route("/edit_joke/<joke_id>", methods=["GET", "POST"])
def edit_joke(joke_id):
    if "user" in session:
        # submits form to database
        if request.method == "POST":
            submit = {
                "category_name": request.form.get("category_name"),
                "joke_description": request.form.get("joke_description"),
                "like": 1,
                "dislike": 0
            }
            mongo.db.jokes.update({"_id": ObjectId(joke_id)}, submit)
            flash("Joke Successfully Updated")

        joke = mongo.db.jokes.find_one({"_id": ObjectId(joke_id)})
        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template(
            "edit_joke.html", joke=joke, categories=categories)

    # validate user is logged in
    else:
        flash("Please log in")
        return redirect(url_for("login"))


'''
The delete joke function removes the joke from the database.
'''


@app.route("/delete_joke/<joke_id>")
def delete_joke(joke_id):
    mongo.db.jokes.remove({"_id": ObjectId(joke_id)})
    flash("Joke Successfully Deleted")
    return redirect(url_for("get_jokes"))


'''
The add bookmark function finds and updates the user and pushes
a new field users bookmark which stores all the jokes the user
has bookmarked.
'''


@app.route("/add_bookmark/<joke_id>", methods=["GET", "POST"])
def add_bookmark(joke_id):
    mongo.db.users.find_one_and_update(
        {"username": session["user"].lower()},
        {"$push": {"users_bookmark": ObjectId(joke_id)}})
    flash("Bookmark is Saved!")
    return redirect(url_for("get_jokes"))


'''
The remove bookmark finds and updates the user and pulls the matching
joke id from the users bookmark array.
'''


@app.route("/remove_bookmark/<joke_id>", methods=["GET", "POST"])
def remove_bookmark(joke_id):
    mongo.db.users.find_one_and_update(
        {"username": session["user"].lower()},
        {"$pull": {"users_bookmark": ObjectId(joke_id)}})
    flash("Bookmark is Removed!")
    return redirect(url_for("get_jokes"))


'''
The family jokes function reads all the jokes from the family category.
Reads the user, user bookmark and finds bookmarked jokes rendering them
on the family jokes page.
'''


@app.route("/family_jokes")
def family_jokes():
    jokes = list(mongo.db.jokes.find({"category_name": "Family Jokes"}))

    if "user" in session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        users_bookmark = mongo.db.users.find_one(
                {"username": session["user"]})["users_bookmark"]

        bookmark_jokes = []
        for bookmark in users_bookmark:
            joke = mongo.db.jokes.find_one({'_id': ObjectId(bookmark)})
            bookmark_jokes.append(joke)
        return render_template(
            "family_jokes.html", username=username.title(),
            users_bookmark=users_bookmark, bookmark_jokes=bookmark_jokes,
            joke=joke, jokes=jokes)

    return render_template("family_jokes.html", jokes=jokes)


'''
The food jokes function reads all the jokes from the family category.
Reads the user, user bookmark and finds bookmarked jokes rendering
them on the food jokes page.
'''


@app.route("/food_jokes")
def food_jokes():
    jokes = list(mongo.db.jokes.find({"category_name": "Food Jokes"}))

    if "user" in session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        users_bookmark = mongo.db.users.find_one(
                {"username": session["user"]})["users_bookmark"]

        bookmark_jokes = []
        for bookmark in users_bookmark:
            joke = mongo.db.jokes.find_one({'_id': ObjectId(bookmark)})
            bookmark_jokes.append(joke)
        return render_template(
            "food_jokes.html", username=username.title(),
            users_bookmark=users_bookmark, bookmark_jokes=bookmark_jokes,
            joke=joke, jokes=jokes)

    return render_template("food_jokes.html", jokes=jokes)


'''
The insult jokes function reads all the jokes from the family category.
Reads the user, user bookmark and finds bookmarked jokes rendering them
on the insult jokes page.
'''


@app.route("/insult_jokes")
def insult_jokes():
    jokes = list(mongo.db.jokes.find({"category_name": "Insult Jokes"}))

    if "user" in session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        users_bookmark = mongo.db.users.find_one(
                {"username": session["user"]})["users_bookmark"]

        bookmark_jokes = []
        for bookmark in users_bookmark:
            joke = mongo.db.jokes.find_one({'_id': ObjectId(bookmark)})
            bookmark_jokes.append(joke)
        return render_template(
            "insult_jokes.html", username=username.title(),
            users_bookmark=users_bookmark, bookmark_jokes=bookmark_jokes,
            joke=joke, jokes=jokes)

    return render_template("insult_jokes.html", jokes=jokes)


'''
The word jokes function reads all the jokes from the family category.
Reads the user, user bookmark and finds bookmarked jokes rendering
them on the word play jokes page.
'''


@app.route("/word_jokes")
def word_jokes():
    jokes = list(mongo.db.jokes.find({"category_name": "Word Play Jokes"}))

    if "user" in session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        users_bookmark = mongo.db.users.find_one(
                {"username": session["user"]})["users_bookmark"]

        bookmark_jokes = []
        for bookmark in users_bookmark:
            joke = mongo.db.jokes.find_one({'_id': ObjectId(bookmark)})
            bookmark_jokes.append(joke)
        return render_template(
            "word_jokes.html", username=username.title(),
            users_bookmark=users_bookmark, bookmark_jokes=bookmark_jokes,
            joke=joke, jokes=jokes)

    return render_template("word_jokes.html", jokes=jokes)


'''
The relationship jokes function reads all the jokes from the family category.
Reads the user, user bookmark and finds bookmarked jokes rendering them on
the relationship jokes page.
'''


@app.route("/relationship_jokes")
def relationship_jokes():
    jokes = list(mongo.db.jokes.find({"category_name": "Relationship Jokes"}))

    if "user" in session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        users_bookmark = mongo.db.users.find_one(
                {"username": session["user"]})["users_bookmark"]

        bookmark_jokes = []
        for bookmark in users_bookmark:
            joke = mongo.db.jokes.find_one({'_id': ObjectId(bookmark)})
            bookmark_jokes.append(joke)
        return render_template(
            "relationship_jokes.html", username=username.title(),
            users_bookmark=users_bookmark, bookmark_jokes=bookmark_jokes,
            joke=joke, jokes=jokes)

    return render_template("relationship_jokes.html", jokes=jokes)


'''
The yo jokes function reads all the jokes from the family category.
Reads the user, user bookmark and finds bookmarked jokes rendering
them on the yo momma jokes page.
'''


@app.route("/yo_jokes")
def yo_jokes():
    jokes = list(mongo.db.jokes.find({"category_name": "Yo Momma Jokes"}))

    if "user" in session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        users_bookmark = mongo.db.users.find_one(
                {"username": session["user"]})["users_bookmark"]

        bookmark_jokes = []
        for bookmark in users_bookmark:
            joke = mongo.db.jokes.find_one({'_id': ObjectId(bookmark)})
            bookmark_jokes.append(joke)
        return render_template(
            "yo_jokes.html", username=username.title(),
            users_bookmark=users_bookmark, bookmark_jokes=bookmark_jokes,
            joke=joke, jokes=jokes)

    return render_template("yo_jokes.html", jokes=jokes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
