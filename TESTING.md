# <p align="center">Testing [Laugh Out Loud!](https://jokes-library.herokuapp.com/)</p>

### [Back to repository](https://github.com/karzuin/jokes_library_MS3)

### Table of Contents<hr>

* [Validators](#validators)
* [Testing User Stories](#testing-user-stories)
* [Responsiveness On Different Devices](#responsiveness-on-different-devices)
* [Browser Compatibility](#browser-compatibility)
* [Bugs During Testing](#bugs-during-testing)
* [Bugs To Be Fixed](#bugs-to-be-fixed)

### Validators<hr>

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

### Testing User Stories<hr>

### All Users

- As a user, I want the website to be easy to understand and navigate.
    - As the user can see from the homepage everything is clearly described and labelled. 
    - The fixed navbar on the top shows the tabs to the Home, Register and Log In pages.
    - On the welcome message just below the hero image and above the searchbox, the user can click on the text and instructions 
    appear on how to use this website they can scroll up and down to read it.
    - When finished the user can scroll up and click on the 'x' on the top right corner to close the window.

- As a user, I want the website to be clean and simple looking.
    - The user can see that the layout is very simple, clean and spacious looking.

- As a user, I want to be able to read jokes on the homepage.
    - The user can scroll down and immediately see the joke cards displayed.

- As a user, I want to be able to access different categories of jokes easily from the homepage.
    - The user can easily access the different categories available on the right side of the joke cards.

- As a user, I want to be able to search for jokes.
    - The user can use the searchbox on all pages except the register, login, and submit a joke pages.
    - The user can use any keywords for jokes eg. fart, coconut, dad etc. and even usernames to find their submitted jokes.
    - The user can click the Reset button to clear the input field. 
    - It's the quickest way to finding what the user wants.
    - The search result appears on the home page and if no results are found a message appears to let the user know.

- As a user, I want to be able to like and dislike each joke and see the number count.
    - The user can click on either the laughing face icon to like or the frowning face icon to dislike to increase the number count 
    as many times as they want. 
    - It's a small fun interaction for the user.

- As a user, I want to be able to register easily and have that confirmed.
    - The user can click on the register tab on the fixed navbar wherever they are on the page. 
    - The register page opens and the form is in the centre of the page where the user is told to type a username between 5 - 15 letters
    or numbers, any other characters will not be accepted and the user will see the line goes red indicating invalid entry. 
    - If the user clicks the submit button at this point an alert message appears 'Please match the format requested'. This also 
    applies with the password input field.
    - When the fields have been inputted correctly the lines go green, the submit button is clicked then the user is redirected to the 
    home page opens with a message confirming 'Registration Succesful!'

[Back to top](#table-of-contents)

### Registered Users

- As a user, I want to be able to log in easily and have that confirmed.
    - The user clicks on the Log In tab on the fixed navbar and the Log In page opens and the form is in the center of the page where the 
    the user is told to type a username and password. 
    - If the username or password does not match an already existing account, an alert message appears 'Incorrect Username and/or Password'.
    - When both the username and password entered match and the user clicks the log in button the page is redirected to the homepage with 
    a personalised message 'Welcome username!'

- As a user, I want to be able to submit my own jokes easily and have that confirmed.
    - Once logged in the user will be able to see the Submit A Joke tab on the fixed navbar by clicking on it they will be directed 
    to the Submit A Joke page where there are two input fields to be filled in. 
    - Firstly, the joke category menu to select the category the joke belongs to, clicking in the area of the input field the menu 
    list will appear with the choices and the user can scroll up and down and click on their preferred choice. 
    - If nothing has been selected and the user clicks the submit button an alert message appears 'Please select an item from the list'.
    - Secondly, the joke description input field where the user types in the joke, if the input field is left blank then the line goes 
    red and an alert message appears 'Please fill in this field'.
    - When the submit button is clicked the user is redirected to the homepage and a confirmation message appears 'Joke Successfully Added'.

- As a user, I want to be able to edit my jokes and have that confirmed.
    - The user can find the joke they want to edit on the homepage, the the category page it is in or via the searchbox.
    - Once the joke is found click on the edit button and the Edit Joke page opens where there are two buttons: a cancel and edit joke 
    button and two input fields to be filled in.
    - The user can choose to click on the cancel button at any time and will be redirected to the homepage.
    - Firstly, the joke category menu in order to select the category the joke belongs to, clicking in the area of the input field 
    the menu list will appear with the choices and the user can scroll up and down and click on their preferred choice.
    - At this point there is always a selected category and they cannot leave it blank.
    - Secondly, the joke description input field where the user types in the joke, if the input field is left blank then the line goes 
    red and an alert message appears 'Please fill in this field'.
    - With both input fields filled when the user clicks on the edit joke button they stay on the same page with a message
    confirming 'Joke Successfully Updated' and see the edited changes in the input fields.
    - If they are happy with the changes the user can click on cancel or the homepage tab to leave the page.
    - If they are not happy with the changes the user can continue to edit.
    
- As a user, I want to be able to bookmark jokes from other users I like and have that confirmed.
    - The user will see on every joke card a bookmark button, when they hover over it a message appears 'Click to Bookmark!'.
    - The user can bookmark on the homepage and any of the category pages.
    - The user is redirected to the homepage and will see the button has been changed to 'Added'.
    

- As a user, I want to be able to un-bookmark jokes on the collections page, home page and category page and have that confirmed.
    - The user can all the jokes they have bookmarked changed to the Added button, when the user hovers over the button a message 
    appears 'Click to Un-Bookmark!'
    - The user can un-bookmark jokes on the homepage, any of the category pages they have bookmarked jokes and their collection page,
    by clicking on the Added button and they will be redirected to the homepage.

- As a user, I want to be able to see the bookmarked jokes in my collections.
    - The user can click on the Collection tab on the fixed navbar and the page opens up with the message 'Username's Collection'.
    - The user will see all the jokes they have bookmarked displayed.
    - Here they can un-bookmark any of the jokes and be redirected to the homepage.


[Back to top](#table-of-contents)

### Responsiveness On Different Screen Sizes<hr>

### [Laugh Out Loud!](https://jokes-library.herokuapp.com/)

The website was manually tested via Chrome Devtools in desktop, laptop, tablet and mobile screens. 
The website images, text and content are well proportioned, undistorted and evenly spaced.
No errors or problems occured with the function of the app.

[Back to top](#table-of-contents)

### Browser Compatibility<hr>

The website was manually tested on the following browsers and do not occur any errors or problems.

[Google Chrome](https://google.com) all the testing information has been tested on Chrome browser using DevTools.

[Mozilla Firefox](https://www.mozilla.org/en-GB/firefox/new/)
- When filling in forms they had security messages indicating the connection is not secure.

[Safari](https://www.apple.com/uk/safari/) 

[Back to top](#table-of-contents)

### Bugs During Testing<hr>

- **Bug**: User can save link to submit a joke and log out and then paste the submit a joke link and add a joke.
- **Debugged**: Added a check if statement in add_joke view and edit_joke view to ensure user is logged in or they will be redirected 
to the log in page.

- **Bug**: How to display the logged in username as the author to a joke they just added rather than allowing them to type anything.
- **Debugged**: Used find_one method in add joke function by defining a variable and used that as a value in the dict.

- **Bug**: When a user registered and went to other pages this error appeared: UnboundLocalError: local variable ‘joke’ referenced before assignment and in the terminal HTTP/1.1" 500 error.
- **Debugged**: Had to assign the joke variable with a value in all the functions that needed it.

- **Bug**: When the user creates a joke, then bookmarks it and then deletes it, it would leave an empty card panel with the bookmark button on the collections page.
- **Debugged**: Update the delete function by adding part of the unbookmark function to it. To remove the bookmark and delete the joke.


### Bugs to be fixed<hr>

- Currently none but many features to be added to make the user experience better are listed in Features Left to Implement in the 
[README](https://github.com/karzuin/jokes_library_MS3/blob/master/README.md)

[Back to top](#table-of-contents)

### [Back to repository](https://github.com/karzuin/jokes_library_MS3)