# Gamebook

Welcome to Gamebook! The site where gaming enthusiasts can share thoughts, tips, tricks and more about games!
This site is designed to be a social media platform aimed specifically at gamers. It is a place where the community can come together and share a huge amount of knowledge on any game. The platform would also appeal to gaming companies and content creators as a way to advatise and monitor the popularity of certain games. This makes it stand out from the huge crowd of different social media platforms that exist today, and this is only the begining! I truely believe thise site could be added apon significantly to make it even better with some extra features that would help it to excel in a real world senerio.

![Finished website on different devices](/docs/screenshots/finishedsushi.jpg)

### Link to deployed site: https://pp5api.herokuapp.com/

---

## Project Board

### Link: https://github.com/users/MadeleineWalder/projects/5

Here you can see:
- The Wireframe
- User Stories
- Design Features
- Structural Features
- Future Features
- Bugs

## The Wireframe

MAKE


## User Stories

Navigation & Authentication:

- Navigation: As a user I can view a navbar from every page so that I can navigate easily between pages
- Routing: As a user I can navigate through pages quickly so that I can view content seamlessly without page refresh
- Authentication - Sign up: As a user I can create a new account so that I can access all the features for signed up users
- Authentication - Sign in: As a user I can sign in to the app so that I can access functionality for logged in users
- Authentication - Logged in Status: As a user I can tell if I am logged in or not so that I can log in if I need to
- Authentication - Refreshing access tokens: As a user I can maintain my logged-in status until I choose to log out so that my user experience is not compromised
- Navigation: Conditional rendering - As a logged out user I can see sign in and sign up options so that I can sign in/sign up
- Avatar: As a user I can view user's avatars so that I can easily identify users of the application

Adding & Liking Posts:

- Create posts: As a logged in user I can create posts so that I can share my thoughts on gaming/a game by adding an image, a title, a rating and text
- View a post: As a user I can view the details of a single post so that I can learn more about it
- Like a post: As a logged in user I can like a post so that I can show my support for the posts that interest me

The Posts Page:

- View most recent posts: As a user I can view all the most recent posts, ordered by most recently created first so that I am up to date with the newest content
- As a user, I can search for posts with keywords, so that I can find the posts and user profiles I am most interested in.
- View liked posts: As a logged in user I can view the posts I liked so that I can find the posts I enjoy the most
- View posts of followed users: As a logged in user I can view content filtered by users I follow so that I can keep up to date with what they are posting about
- Infinite scroll: As a user I can keep scrolling through the images on the site, that are loaded for me automatically so that I don't have to click on "next page" etc

The Post Page:

- Post page: As a user I can view the posts page so that I can read the comments about the post
- Edit post: As a post owner I can edit my post title and description so that I can make corrections or update my post after it was created
- Create a comment: As a logged in user I can add comments to a post so that I can share my thoughts about the post
- Comment date: As a user I can see how long ago a comment was made so that I know how old a comment is
- View comments: As a user I can read comments on posts so that I can read what other users think about the posts
- Delete comments: As an owner of a comment I can delete my comment so that I can control removal of my comment from the application
- Edit a comment: As an owner of a comment I can edit my comment so that I can fix or update my existing comment

The Profile Page:

- Profile page: As a user I can view other users profiles so that I can see their posts and learn more about them
- Most followed profiles: As a user I can see a list of the most followed profiles so that I can see which profiles are popular
- User profile - user stats: As a user I can view statistics about a specific user: bio, number of posts, follows and users followed so that I can learn more about them
- Follow/Unfollow a user: As a logged in user I can follow and unfollow other users so that I can see and remove posts by specific users in my posts feed
- View all posts by a specific user: As a user I can view all the posts by a specific user so that I can catch up on their latest posts, or decide I want to follow them
- Edit profile: As a logged in user I can edit my profile so that I can change my profile picture and bio
- Update username and password: As a logged in user I can update my username and password so that I can change my display name and keep my profile secure

---

## Design Features

- **Color Scheme:**

- **Font:**

## Structural Features

### The Navbar

- **Logo:**

- **Add Post:**  

- **Navigation Links:** 

### Home Page:


### Post Page:


### Profile Page:


### Sign-up Page


### Sign-in Page


## Future Features:


---

## Structural Features



---

## Future Features



---

## Bugs

- 


---

## Technologies:

- This site was created using these languages: Python, JavaScript, React, Bootstrap, HTML and CSS.
- Frameworks/Libraries: Django and Bootstrap.
- Allauth was used to create the log-in/out and sign-up forms.
- Github and Gitpod are the platforms where I created this website. Github (and Gihub pages) for creating and storing my repositories and project board/issues, and Gitpod for writing the code.
- Heroku for deployment.
- Unicorn Revealer is an extension for Chrome which I used to help me see the different elements of my site clearly.
- [Google Fonts](https://fonts.google.com/) is where I imported my fonts from.
- [Fontawesome](https://fontawesome.com/) is the website where I sourced my social media icons.
- [Pexels](https://www.pexels.com/) is the website I used to source the hero image.
- I used the website [amiresponsive.co.uk](https://amiresponsive.co.uk/) to show my finished site on different devices at the top of this page.

---

## Testing: 

### Supported Screens and Browsers:

- The site was viewed and tested on the Google Chrome browser
- Different screen sizes were tested using a simulator that is part of Google Chrome's dev tools
- As a result all screenshots of different screen sizes are also taken from this simulator
- Tested/ supported devices: Galaxy Fold, Moto G4, iPhone 4, 6, 7, 8, X, XR and 12 Pro, Pixel 5, Samsung Galaxy S8+, S20 Ultra and A51/71, iPad, iPad Air, Mini and Pro, Surface Pro 7, Surface Duo, Nest Hub and Nest Hub Max.

### Test Cases:

Upon opening the site the user should first see the home page:

This includes the navbar, hero image, main buttons and footer.

Home page on desktop:

![homepage on desktop](/docs/screenshots/hpdesktop.jpg)

Home page on tablet:

![homepage on tablet](/docs/screenshots/hptablet.jpg)

Home page on mobile:

![homepage on mobile](/docs/screenshots/hpmobile.jpg)

Outcome: tests passed

Clicking on 'Menu' in the navigation bar OR the 'Menu' button should take the user to the menu page:

Menu page on desktop:

![menu on desktop](/docs/screenshots/mdesktop.jpg)

Menu page on tablet:

![menu on tablet](/docs/screenshots/mtablet.jpg)

Menu page on mobile:

![menu on mobile](/docs/screenshots/mmobile.jpg)

Outcome: tests passed

Clicking on 'Sign-up' in the navigation bar should take the user to the sign up page:

Sign up page on desktop:

![sign up on desktop](/docs/screenshots/signupdesktop.jpg)

Sign up page on tablet:

![sign up on tablet](/docs/screenshots/signuptablet.jpg)

Sign up page on mobile:

![sign up on mobile](/docs/screenshots/signupmobile.jpg)

The Sign-up form requires the user to fill out all fields except the optional email field:

![username required](/docs/screenshots/unrequired.jpg)

![password required](/docs/screenshots/pwrequired.jpg)

![same password required](/docs/screenshots/pw2required.jpg)

Password fields must be the same and the password cannot be too simple:

![password too common](/docs/screenshots/pwc.jpg)

The email must be in email format:

![email in valid format required](/docs/screenshots/email.jpg)

Outcome: tests passed

Clicking on 'Sign-in' in the navigation bar should take them to the sign in page:

Sign in page on desktop:

![sign in on desktop](/docs/screenshots/signindesktop.jpg)

Sign in page on tablet:

![sign in on tablet](/docs/screenshots/signintablet.jpg)

Sign in page on mobile:

![sign in on mobile](/docs/screenshots/signinmobile.jpg)

The Sign-in form requires the users username and password:

![users username](/docs/screenshots/username.jpg)

![users password](/docs/screenshots/password.jpg)

Outcome: tests passed

Clicking on 'Sign-out' in the navigation bar should take them to the sign out page:

Sign out page on desktop:

![sign out on desktop](/docs/screenshots/signoutdesktop.jpg)

Sign out page on tablet:

![sign out on tablet](/docs/screenshots/signouttablet.jpg)

Sign out page on mobile:

![sign out on mobile](/docs/screenshots/signoutmobile.jpg)

Outcome: tests passed

When the user signs in or out an alert should pop up to notify them:

Alert on desktop:

![Alert on desktop](/docs/screenshots/alertd1.jpg)

![Alert on desktop](/docs/screenshots/alertd.jpg)

Alert on tablet:

![Alert on tablet](/docs/screenshots/alertt1.jpg)

![Alert on tablet](/docs/screenshots/alertt.jpg)

Alert on mobile:

![Alert on mobile](/docs/screenshots/alertm1.jpg)

![Alert on mobilep](/docs/screenshots/alertm.jpg)

Outcome: tests passed

Clicking on 'Bookings' in the navigation bar OR the 'Book' button should take them to the bookings page:

Booking page on desktop:

![Booking page on desktop](/docs/screenshots/bdesktop.jpg)

Booking page on tablet:

![Booking page on tablet](/docs/screenshots/btablet.jpg)

Booking page on mobile:

![Booking page on mobile](/docs/screenshots/bmobile.jpg)

Outcome: tests passed

However if the user is not signed in yet they will be required to sign in first:

Require sign in to book on desktop:

![Booking page on desktop](/docs/screenshots/sidesktop.jpg)

Require sign in to book on tablet:

![Booking page on tablet](/docs/screenshots/sitablet.jpg)

Require sign in to book on mobile:

![Booking page on mobile](/docs/screenshots/simobile.jpg)

Outcome: tests passed

Clicking on the 'Add Booking' button should take them to the add booking page:

Add booking page on desktop:

![add booking page on desktop](/docs/screenshots/adesktop.jpg)

Add booking page on tablet:

![add booking page on tablet](/docs/screenshots/atablet.jpg)

Add booking page on mobile:

![add booking page on mobile](/docs/screenshots/amobile.jpg)

When the user clicks on the date field they will see this calendar to help them pick a date:

![add booking date picker](/docs/screenshots/date.jpg)

The time field also has a similar function:

![add booking time picker](/docs/screenshots/time.jpg)

None of the form fields can be left blank:

![the name field is required](/docs/screenshots/fname.jpg)

![the date field is required](/docs/screenshots/fdate.jpg)

![the time field is required](/docs/screenshots/ftime.jpg)

![the number of people field is required](/docs/screenshots/fpeople.jpg)

If the user inputs a date in the past, they will be notified that they must enter a date in the future.

![the date error message](/docs/screenshots/datepicker2.jpg)

The same thing will happen if they try to edit a booking date to a date that is older than the current date.

Likewise if they edit or create bookings on the same date they will notified and the booking form refreshed:

![the double booking error message](/docs/screenshots/doublebooking.jpg)

Outcome: tests passed

Clicking on the 'Edit' button on a booking should take them to the edit booking page:

It is the same form as for adding a new booking and has all the same funtionality.

Edit booking page on desktop:

![Edit booking page on desktop](/docs/screenshots/edesktop.jpg)

Edit booking page on tablet:

![Edit booking page on tablet](/docs/screenshots/etablet.jpg)

Edit booking page on mobile:

![Edit booking page on mobile](/docs/screenshots/emobile.jpg)
Outcome: tests passed

Clicking on the 'Delete' button should trigger the delete modal on the bookings:

Delete booking page on desktop:

![Delete booking page on desktop](/docs/screenshots/ddesktop.jpg)

Delete booking page on tablet:

![Delete booking page on tablet](/docs/screenshots/dtablet.jpg)

Delete booking page on mobile:

![Delete booking page on mobile](/docs/screenshots/dmobile.jpg)

Outcome: tests passed

My site also has a custom 404 page. If the user were to enter a url that doesn't exist it should be displayed:
If the user clicks the button they should return to the homepage.

The 404 page on desktop:

![custom 404 page desktop](/docs/screenshots/404.jpg)

The 404 page on tablet:

![custom 404 page tablet](/docs/screenshots/404t.jpg)

The 404 page on mobile:

![custom 404 page mobile](/docs/screenshots/404m.jpg)

Outcome: tests passed

---

### Validator Testing

- I used the [W3C HTML Validator](https://validator.w3.org/#validate_by_input) to test my html.

The home page:
The results showed an error in two places where an anchor tag is wrapping the buttons. I did some research and I couldn't find out **why** this is bad practise. I even found one website which gave an example of some html where the button was wrapped in anchor tags. The website actually offers coding courses which I almost enrolled in myself. A link to the page is here: https://www.shecodes.io/athena/17038-how-to-add-a-link-to-my-button-in-html

The only other solution I could find was to remove the button tags and use divs instead, but style them like buttons. Unfortunately I dont think I will have time to implement this as I'm worried about the implications this will cause to the layout of my site so close to my deadline.

![The W3C Validator showing my HTML](/docs/screenshots/hpvalid1.jpg)

The menu page:
Here there were no errors.

![The W3C Validator showing my HTML](/docs/screenshots/bvalid.jpg)

The booking page:
I made sure to add a booking here before copying the source code so that could be tested too. I'm not sure what is going on with these errors. I have been looking over my code and all the errors say I have unclosed elements but all of mine are closed properly.
As an example the final error says that the main tag is unclosed, but you can clearly see that it is:

![The W3C Validator showing my HTML](/docs/screenshots/vbvalid.jpg)

![The W3C Validator showing my HTML](/docs/screenshots/main.jpg)

The Sign-up page:
No errors.

![The W3C Validator showing my HTML](/docs/screenshots/suvalid.jpg)

The Sign-in:

![The W3C Validator showing my HTML](/docs/screenshots/sivalid.jpg)

The Sign-out page:

![The W3C Validator showing my HTML](/docs/screenshots/sovalid.jpg)

- I used the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) to test my CSS. There were no errors:

![The W3C Validator showing my CSS](/docs/screenshots/cssvalid.jpg)

- I used the [CI Python Validator](https://pep8ci.herokuapp.com/) to test my python:

My models.py file had no errors:

![python validator testing my code](/docs/screenshots/models.jpg)

My forms.py file had no errors:

![python validator testing my code](/docs/screenshots/forms.jpg)

My views.py file had no errors:

![python validator testing my code](/docs/screenshots/views.jpg)

My urls.py files had no errors except one path which made the line too long:

![python validator testing my code](/docs/screenshots/urls1.jpg)

![python validator testing my code](/docs/screenshots/urls2.jpg)

I did not want to change this as I was worried it would effect the path.

My widgets.py file had no errors:

![python validator testing my code](/docs/screenshots/widgets.jpg)

My manage.py file had no errors:

![python validator testing my code](/docs/screenshots/manage.jpg)

My admin.py file had no errors:

![python validator testing my code](/docs/screenshots/admin.jpg)

My wsgi.py file had no errors:

![python validator testing my code](/docs/screenshots/wsgi.jpg)

My settings.py file had a few ling too long errors:

![python validator testing my code](/docs/screenshots/settings.jpg)

I could not fix these errors and code is still functioning as intended so I left them alone.
As you can see in this screenshot above, line 124, 127, 130 and 133 cannot be made shorter, at least to my knowledge.

- I used [JSHint](https://jshint.com/) to test my JavaScript:

![JSHint validator testing my code](/docs/screenshots/js.jpg)

As you can see the only errors were missing semi-colons so I added these.

![JSHint validator testing my code](/docs/screenshots/js1.jpg)

- I have tested my site using the devtools Lighthouse feature.

![The lighthouse report](/docs/screenshots/lhreport.jpg)

---

## Deployment:

### Gitpod

- Typing 'python3 manage.py runserver' into the Gitpod terminal allows you to view a preview of the site in a browser.
- Dragging open the second terminal, type 'cd frontend' to ensure you in the frontend directory. Then type 'npm start' and click open preview to view the app.
- Every time a secton of code is added the browser can be refreshed to see the change, sometimes you need to press ctrl + shift + R for changes to be updated.
- To save and commit progress, type 'git add .' into the terminal to add all your changes followed by 'git commit -m' and then your message describing what you did in double quotes.
- Typing 'git push' will then push your code, and this should be done at the end of every coding session or whenever you want an already deployed site to be updated.


### ElephantSQL

- I used ElephantSQL to install and manage the database. I had already set up an account so I could log in and begin.
- I clicked on the green 'Create New Instance' button in the top right.
- I added details such as name, region and the type of plan I wanted which was the free 'Tiny Turtle' plan.
- My database url was then provided for me to copy and paste into my config vars on Heroku.


### Heroku

- For this project I deployed to Heroku at the begining of the project. Deploying early can save you a lot of time later on.
- To do this I created a new Heroku app which I also named sushicat.
- In the app settings I made sure to add all of the config vars I would need: the secret key, the port and my database url which I got from ElephantSQL.
- I made sure to comment out the old database 'db.sqlite3' in the settings.py file and added in my new database url.
- I also added my Heroku Hostname to the allowed hosts list.
- Back in Heroku I went to the deployment tab for my app and selected Github. Then I searched for and selected my repository.
- At the bottom of the page I ticked the box to enable automatic deploys, and then clicked deploy.

Link to deployed site: https://sushicat.herokuapp.com/

---