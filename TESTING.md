# <p align="center">Testing [Laugh Out Loud!](https://jokes-library.herokuapp.com/)</p>

### [Back to repository](https://github.com/karzuin/jokes_library_MS3)

## Table of Contents<hr>

* [Validators](#validators)
* [Testing User Stories](#testing-user-stories)
* [Responsiveness On Different Devices](#responsiveness-on-different-devices)
* [Browser Compatibility](#browser-compatibility)
* [Bugs During Testing](#bugs-during-testing)
* [Bugs To Be Fixed](#bugs-to-be-fixed)

## Validators<hr>

Used [W3C HTML validator](https://validator.w3.org/#validate_by_input) website via the direct input path. 

1. Index.html validator results. Due to the jinja templating it throws errors for the majority of the code.

<p align="center"><img width="350" height="300" src="readme-images/html_valid.png"></p>

Used [Jigsaw](https://jigsaw.w3.org/css-validator/#validate_by_input) website via the direct input path. 

2. Style.css validator results.

<p align="center"><img width="350" height="300" src="readme-images/css_valid.png"></p>

Used[JShint](https://jshint.com/) website.
3. main.js validator results.

<p align="center"><img width="350" height="300" src="readme-images/jshint_valid.png"></p>

Used [PEP8](http://pep8online.com/).
4. app.py validator results.

<p align="center"><img width="350" height="300" src="readme-images/pep8_valid.png"></p>

[Back to top](#table-of-contents)

## Testing User Stories<hr>

#### All Users

- As a user, I want the website to be easy to understand and navigate.
    - As the user can see from the homepage everything is clearly described and labelled. 
    - The fixed navbar on the top shows the tabs to the Home, Register and Log In pages.

- As a user, I want the website to be clean and simple looking.
    - The user can see that the layout is very simple, clean and spacious looking.

- As a user, I want to be able to read jokes on the homepage.
    - The user can scroll down and immediately see the joke cards displayed.

- As a user, I want to be able to access different categories of jokes easily from the homepage.
    - The user can easily access the different categories available on the right side of the joke cards.

- As a user, I want to be able to search for jokes.
    - The user can use the searchbox on all pages except the register, login, and submit a joke pages.
    - The user can use any keywords for jokes eg. fart, coconut, dad etc. and even usernames to find their submitted jokes. 
    - It's the quickest way to finding what the user wants.
    - The search result appears on the home page and if no results are found a message appears to let the user know.

- As a user, I want to be able to like and dislike each joke and see the number count.
    - The user can click on either like or dislike to increase the number count as many times as they want. 
    It's a small fun interaction for the user.

- As a user, I want to be able to register easily and have that confirmed.
    - The user can click on the register tab on the fixed navbar wherever they are on the page. 
    - The register page opens and the form is in the centre of the page where the user is told to type a username between 5 - 15 letters
    or numbers, any other characters will not be accepted and the user will see the line goes red indicating invalid entry. If the user
    tries to submit at this point an alert message 'Please match the format requested'. This also applies with the password input field.
    - When the fields have been inputted correctly the lines go green and home page opens with a message confirming 'Registration Succesful!'

#### Registered Users

- As a user, I want to be able to log in easily and have that confirmed.
- As a user, I want to be able to submit my own jokes easily and have that confirmed.
    - 
- As a user, I want to be able to edit my jokes and have that confirmed.
- As a user, I want to be able to bookmark jokes from other users I like and have that confirmed.
- As a user, I want to be able to un-bookmark jokes on the collections page, home page and category page and have that confirmed.
- As a user, I want to be able to see the bookmarked jokes in my collections.


[Back to top](#table-of-contents)

## Responsiveness On Different Devices<hr>

### [](https://jokes-library.herokuapp.com/)

In desktop mode, 

In iPad mode, 

In mobile phone mode, 


[Back to top](#table-of-contents)

# Browser Compatibility<hr>

[Google Chrome](https://google.com) all the testing information has been tested on Chrome browser using DevTools.

[Mozilla Firefox](https://www.mozilla.org/en-GB/firefox/new/)
- **Bug**: 

[Internet Explorer](https://www.microsoft.com/en-gb/download/internet-explorer.aspx) 
- **Bug**: 

[Safari](https://www.apple.com/uk/safari/) 

[Back to top](#table-of-contents)



## Bugs During Testing<hr>

- **Bug**: User can save link to submit a joke and log out and then paste the submit a joke link and add a joke.
- **Debugged**: Added a check if statement in add_joke view and edit_joke view to ensure user is logged in or they will be redirected 
to the log in page.

- **Bug**: How to display the logged in username as the author to a joke they just added rather than allowing them to type anything.
- **Debugged**: Used find_one method in add joke function by defining a variable and used that as a value in the dict.

- **Bug**: When a user registered and went to other pages this error appeared: UnboundLocalError: local variable ‘joke’ referenced before assignment and in the terminal HTTP/1.1" 500 error.
- **Debugged**: Had to assign the joke variable with a value in all the functions that needed it.

- **Bug**: When the user creates a joke, then bookmarks it and then deletes it, it would leave an empty card panel with the bookmark button on the collections page.
- **Debugged**: Update the delete function by adding part of the unbookmark function to it. To remove the bookmark and delete the joke.


## Bugs to be fixed<hr>

- **Bug**: 
- **Bug**: 

[Back to top](#table-of-contents)

### [Back to repository](https://github.com/karzuin/jokes_library_MS3)