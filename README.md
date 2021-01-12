# <p align="center">[Laugh Out Loud!](https://jokes-library.herokuapp.com/)</p>

A website that has a collection of jokes to make people laugh and lighten their mood in these challenging times! 
The web pages are easy to navigate with a simple layout and light, fresh colours. 
Jokes are all displayed on the homepage but are also categorised for easy access. All users can read and vote to like or dislike jokes.
Users can also register to gain access to options of submitting, editing and deleting their jokes, bookmarking and collecting jokes of 
other users.

Reasons users may be want to use this site:
- They like reading or collecting jokes. 
- To pass the time. 
- To laugh out loud, giggle or improve their mood. 
- Aspiring comedians looking for inspiration.

## Table of Contents

* [UX](#ux)
  * [User Stories](#user-stories)
  * [Design](#design)
  * [Wireframes](#wireframes)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## UX<hr>

## User stories:<hr>

#### All Users

- As a user, I want the website to be easy to understand and navigate.
- As a user, I want the website to be clean and simple looking.
- As a user, I want to be able to read jokes on the homepage.
- As a user, I want to be able to access different categories of jokes easily from the homepage.
- As a user, I want to be able to search for jokes.
- As a user, I want to be able to like and dislike each joke and see the number count.
- As a user, I want to be able to register easily and have that confirmed.

#### Registered Users

- As a user, I want to be able to log in easily and have that confirmed.
- As a user, I want to be able to submit my own jokes easily and have that confirmed.
- As a user, I want to be able to edit my jokes and have that confirmed.
- As a user, I want to be able to bookmark jokes from other users I like and have that confirmed.
- As a user, I want to be able to un-bookmark jokes on the collections page, home page and category page and have that confirmed.
- As a user, I want to be able to see the bookmarked jokes in my collections.

## Design<hr>

I wanted a simple layout, easy to intuitively navigate, and light, fresh colours of white, yellow and teal to positively influence the 
mood of the user. The buttons were bold colours of green, red, yellow and a muted grey colour for the cancel button.

I used face emoji icons from ICONS8 as they were colourful for the like and dislike function.

Mali font family was used throughout the website as it gives a playful, humorous, light looking feel.

## Wireframes<hr>
I used [Pencil](https://pencil.evolus.vn/) to create [wireframes](https://github.com/karzuin/jokes_library_MS3/tree/master/wireframes) 
in desktop, tablet and phone view.

# Features<hr>
## Accessible to all users

- The homepage consists of the main heading, navbar with links to the homepage, register page and log in page.
- There is a welcome message where you can click to get more information on how to use the website.
- The search box allows the user to search for jokes with keywords, they also have the option to reset the input field or search.
- The Joke Bank displays all the jokes in the database with the option to like or dislike them. 
- On the left of the joke bank are the jokes in their categories, so the user may want to read particular type of jokes.
- In the footer are social links that open up to their respective homepages.

## Accessible to registered users

- Once logged in, the user is directed to the homepage with a welcome message. 
- The jokes now show options of bookmarking them. 
- All bookmarked jokes are displayed on their collections page. 
- The user can submit jokes into the database. 
- Once jokes are submitted the option to edit or delete them will appear on the joke card.
- They can still like and dislike jokes on any of the joke pages.

# Features Left to Implement

- Pagination

# Technologies Used<hr>

- [Gitpod](https://gitpod.io/) IDE (Integrated Development Environment).
- [GitHub](github.com/) The remote storing of code platform. 
- [HTML 5](https://en.wikipedia.org/wiki/HTML5) for markup language.
- [CSS 3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) cascading style language.
- [JQuery](https://code.jquery.com/) javascript library.
- [Materialize](https://materializecss.com/) css framework for design. 
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) python framework.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) templating with flask. 
- [Werkzeug](https://palletsprojects.com/p/werkzeug/) autentication and authorisation. 
- [Heroku](https://www.heroku.com/) hosting cloud platform to deploy live version of project. 
- [Python](https://www.python.org/) backend programming language.
- [PyMongo](https://pymongo.readthedocs.io/en/stable/) Python API for MongoDB.
- [MongoDB Atlas](https://www.mongodb.com/1) store, index and query data.
- [dnspython](https://www.dnspython.org/) DNS toolkit for Python. 
- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) To see visually the elements of what each code produced, what happens if code is changed, and responsiveness of different device sizes.
- [Autoprefixer](https://autoprefixer.github.io/) To check CSS browser compatibility.
- [Jigsaw](https://jigsaw.w3.org/css-validator) To check for any errors in CSS code.
- [W3C Markup Validator](https://validator.w3.org/) To check for any errors in HTML code.
- [Pep8 Online](http://pep8online.com/) check for any errors in python code.
- [Google Fonts](https://fonts.google.com/) This is where I found the Mali font family.
- [Favicon](https://favicon.io) To include a ?? icon on the web browser tab.

# Testing<hr>
Testing information is found on a separate file [TESTING.md](TESTING.md)

# Deployment<hr>
  
## How to deploy the application to Heroku:

- First I created some files that Heroku needs to run the app with. The first file tells Heroku which applications and dependencies are required
to run the app.

- In the terminal of my IDE gitpod, type: `pip3 freeze --local > requirements.txt`

- Next the Procfile is what Heroku looks for to know which file runs the app and how to run it.

- In the terminal of my IDE gitpod, type: `echo web: python app.py > Procfile`

- Check the requirements.txt has a list of dependencies that are needed for Flask.
- The Procfile may add a blank line at the bottom, sometimes this can cause problems when running apps on Heroku, so delete that line and 
add, commit and push these files.

- Go to the Heroku website and create an account, on the dashboard click 'Create a new app', give an app name using lowercase and use '-' 
instead of spaces.

- Select a region and click 'Create app'.

- To deploy the app, go to the 'Deploy' tab, go to the 'Deployment section' and click on the 'Github' button.

- Make sure my Github profile is displayed, then search for the repository name, click 'Connect' button to connect to the app from Github.

There are different ways to connect a project to Heroku and Heroku has full documentation on how to do that via the 'Deploy' tab.

- Since I've hid the environment variables in the env.py file Heroku won't be able to read them. Click 'Settings' tab. Click 'Reveal Config Vars'.

- Type in the following variables:
```
IP = 0.0.0.0
MONGO_DBNAME = [Name of MongoDB] <br>
MONGO_URI = mongodb+srv://:@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority
PORT = 5000
SECRET_KEY = [Secret key]
```
- Click 'Hide Config Vars'. 

- You can find your MongoDB URI link go to MongoDB Atlas account and click 'Clusters', click ‘Connect Cluster’ button, click 'Connect your 
application' button. Select 'Python' as driver and version 3.6 or later.

- Click 'Deploy' tab, click 'Enable Automatic Deployment', click 'Deploy Branch'. Heroku now receives the code from Github and starts to
build the app. When it has finished a message 'Your app was successfully deployed', click 'View' to launch the new app.

### How to run the app locally:

For more information on [Cloning a Repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

- Scroll to the top of this page and click on green button 'code'.
- Click on the icon that looks like a clipboard on the right side of the URL (this copies URL link)
- Open repo or create new repo.
- Open a new Terminal window in your IDE.
- Type `git clone` and paste URL link and press enter.
- Now create a Database to use for this project with MongoDB.
- Return to the Terminal
- To install all required dependencies type:
```
pip3 install -r requirements.txt
```
- Create an env.py file with the following content, replacing the 'username','password', 'cluster_name' and 'database_name' with your MongoDB database values:
```
import os

os.environ["MONGO_URI"] = "mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority" 
```
- Add your env.py file to .gitignore to make sure your database information is not viewable to others

- App is ready to run locally by typing `python3 app.py`

# Credits<hr>

### Content

#### Text for the jokes.html:

- Is written by me.

### Media

#### Images for base.html:

- Hero image from [The Alternative UK](https://www.thealternative.org.uk/dailyalternative/2019/2/22/laughter-and-politics)

- Icon of laughing with tears face emoji for the like link [ICONS8](https://icons8.com/icons/set/laughing-emoji)

- Icon of the frowning face emoji for the dislike link [ICONS8](https://icons8.com/icons/set/frowning-emoji)

#### Image for web browser tab:

- [ICONS8](https://icons8.com/icons/set/lego)

### Code

- 

# Acknowledgements

Also thank you to the [Code Institute](https://codeinstitute.net/) slack channel, [CI](https://codeinstitute.net/) tutors and mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/).
