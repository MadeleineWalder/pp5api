# Gamebook

Welcome to Gamebook! The site where gaming enthusiasts can share thoughts, tips, tricks and more about games!
This site is designed to be a social media platform aimed specifically at gamers. It is a place where the community can come together and share a huge amount of knowledge on any game. The platform would also appeal to gaming companies and content creators as a way to advatise and monitor the popularity of certain games. This makes it stand out from the huge crowd of different social media platforms that exist today, and this is only the begining! I truely believe thise site could be added apon significantly to make it even better with some extra features that would help it to excel in a real world senerio.

![Finished website on different devices](/docs/screenshots/.jpg)

### Link to deployed site: 

---

## Project Board

### Link: 

Here you can see:
- The Wireframe
- User Stories
- Design Features
- Structural Features
- Future Features
- Bugs

#### Note all of these are also included below.

## The Wireframe

- The wireframe for the home page:

![wireframe home page](/docs/wireframes/wfhome.jpg)

- The wrieframe for the post page. This is the page a user will see if they click on a post to view it individually:

![wireframe post page](/docs/wireframes//wfpost.jpg)

- The wireframe for the profile page: something I forgot to consider here at the time of planning was that if a user is signed in, and is viewing another users profile, they will also see the follow/ unfollow button for that profile.

![wireframe profile page](/docs/wireframes//wfprofile.jpg)


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

The colour scheme for this site is red, white and a super dark blue thats almost black. When I started the project my first thought was: 'What colours do I think of when I think about gaming?' and red was immediately my first response. The colour red is used so much in the gaming industry because of its vibrant, exciting appearance to make games amoung other products look as fun and exciting as possible. My next choice was black as black and red is used a lot in games, gaming equipment is commonly black. However when I tried to use black I didn't like the outcome. If I used it as a background colour it made the site look very dark, and a lot of the images I was uploading just didn't stand out so well on a black background. The more I lightened the black colour to more of a gray the less clear the red text became. I ended up using white instead as it looked a lot more friendly and welcoming which is something I wanted for my social media platform to encourage people to use it. However when I was experimenting with different shades of black I found this very nice black/blue which I decided to use as a highlight for things like the navbar icons when hovered or active. It stands out very well and contrasts nicely from the other colours which is perfect for this role.

- **Font:** 

My font which I chose for this site is called Roboto Mono and I really like how it is clear and easy to read it is. It also looks like a font from a video game; it reminds me of a font from a retro game but with a modern twist. I ended up using this font for the whole site as I thought it worked so well with the theme and kept the site consistent in style.

## Structural Features

### The Navbar

- This contains the logo, nav-links. If the user is signed in there will also be a link to their profile and their avatar will be displayed.

- The logo can be clicked to naigate the user back to the home page.

- The nav-links have a darker colour when hovered or active.

![navbar signed out](/docs/screenshots/navbar1.jpg)

![navbar signed in](/docs/screenshots/navbar2.jpg)

### Home Page:

- The home page contains the search bar at the top to allow users to search posts.

![search bar](/docs/screenshots/searchbar1.jpg)

- The most popular profiles are displayed on the right. If signed in the user will be able to follow/unfollow them here. 

Signed in:

![popular profiles signed in](/docs/screenshots/poppros1.jpg)

Signed out:

![popular profiles signed out](/docs/screenshots/poppros2.jpg)

- The home page allows the user to scroll inifinitely through posts without having to navigate to other pages.

![loading more posts](/docs/screenshots/scroll1.jpg)


### Sign-up Page

- The sign-up page includes the navbar, an image and a form with a username field and two password fields as well as a sign up button to submit.

![the sign-up page](/docs/screenshots/signup1.jpg)

### Sign-in Page

- The sign-in page is basically the same but the form only has one password field.

![the sign-in page](/docs/screenshots/signin1.jpg)

### Feed and Liked pages:

- When signed in the user can navigate to the 'Feed' and 'Liked' pages through the navbar. The feed shows the user posts made by accounts they are following.

![the feed](/docs/screenshots/feed1.jpg)

- Whilst the liked page is of course for posts the user has liked:

![the liked page](/docs/screenshots/liked1.jpg)

### Profile Page:

- Clicking on an avatar allows the user to view that profile and its stats. This includes the number of posts, following and people they are folling.

![the profile page](/docs/screenshots/profile1.jpg)

- If the user is signed in and viewing their own profile they will also see this dropdown menu allowing them to edit their profile, username or password. 

![profile dropdown menu](/docs/screenshots/profile2.jpg)

- If the user clicks edit profile they can use this form to change their avatar and bio.

![profile edit form](/docs/screenshots/editprofile.jpg)

- The change username or password options take the user to a form to change their username or password respectively.

![username edit form](/docs/screenshots/changeusername.jpg)
![password edit form](/docs/screenshots/changepassword.jpg)

### Post Create Form:

- Clicking on the add post link with take the user to the post create form.

![post create form](/docs/screenshots/postcreate.jpg)

- The post consists of: The owners username and avatar, the date the post was created, the image, the title, the optional rating, the main text, the like counter and button and the comment counter and button. For the owner of the post the three dots for the dropdown menu will also be visible.

![post structure](/docs/screenshots/post.jpg)

### Post Page:

- Once a user has created a post, they can click it to view it separately. Here the owner of the post can see the dropdown menu.

![post dropdown menu](/docs/screenshots/postmenu.jpg)

- From that dropdown menu on the post page the owner can click the edit button to be take to the post edit form. This contains all the same fields as the post create form.

![post edit form](/docs/screenshots/postedit.jpg)

- Deleting a post is as simple as clicking the delete button.

- The like button can be clicked to like posts, however the user must be logged in to like and they cannot like their own post.

![like and comment buttons](/docs/screenshots/buttons.jpg)

- The owner and other users can also view its comments or make comments using the comment form if logged in.

![comments](/docs/screenshots/comment1.jpg)

---

## Future Features

In the future I would love to include the following aspects to make the site compete with other big social media platforms:

- Private messaging -to allow direct communication between users

- Pin comments -to allow only the owner of a post to pin a comment to the top of the list. It could be one they thought was most useful like an answer to a question, or one they thought was simply the most funny. This would improve user experience as other people looking for an answer wouldn't have to scroll through all comments to find it.

- Reply to comments -being able to reply to a specific comment would make communication between users easier as the reply would be under the original comment and not above in order from newest to oldest. It would be easier to tell who was talking to who or responding to which comment.

- Like comments -being able to like comments is similar to being able to pin them, except its not just the owner of the post who can like its comments. Allowing all suers to like comments (provided that they are logged in) provides more overall user interaction for the community.

- Email authentication / password recovery -to allow users to reset their password if they forgot it would be ideal for real world use. Everyone forgets their password sometimes! It would encorage users to continue using the site instead of giving up or having to make a new account.

- Emojis for desktop -emojis are a huge part of how people express themselves online and would not only improve user experince but also just make posting and communiting with each other more fun!

- Notifications -recieving notifications when someone likes of comments on your post would also encorage users to return to the site often and boost user activity.

- Able to view followers/following -being able to see a list of followers or people you are following would make it easier to follow/unfollow speific people so the user doesn't have to scroll through the feed to try to find someone.

---

## Bugs

- Bug: The user could not see the stats on their profile/ another users profile such as number of posts, followers and following.

- Solution: In my serializers.py file inside the profiles directory I had forgotten to add 'posts_count', 'followers_count', 'following_count', to the fields lists in the meta class for the profile model.

![bug example 1](/docs/screenshots/fix1.jpg)


- Bug: The user could not view individual posts or comment on posts. They would just be taken to a blank white screen.

- Solution: Correct the import in PostPage.js. I was importing from "react-router" when it should have been "react-router-dom".

![bug example 2](/docs/screenshots/fix2.jpg)

---

## Technologies:

- This site was created using these languages: Python, JavaScript, React, HTML and CSS.
- Frameworks/Libraries: Django and Bootstrap.
- Github and Gitpod are the platforms where I created this website. Github (and Gihub pages) for creating and storing my repositories and project board/issues, and Gitpod for writing the code.
- Heroku was connected to my github repository for site deployment.
- [Google Fonts](https://fonts.google.com/) is where I imported my font from.
- [Fontawesome](https://fontawesome.com/) is where I sourced my icons.
- [Pexels](https://www.pexels.com/) is the website I used to source any images that I didn't take myself.
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

This includes the navbar, search bar, recent posts, and popular profiles.

Home page on desktop:

![Home page on desktop](/docs/screenshots/hdesktop.jpg)

Home page on tablet:

![Home page on tablet](/docs/screenshots/htablet.jpg)

Home page on mobile:

![Home page on mobile](/docs/screenshots/hmobile.jpg)

Outcome: tests passed

The navbar should show the logo, Home, Sign-in and Sign-up links when a user is logged out:

Navbar logged out on desktop:

![Navbar logged out on desktop](/docs/screenshots/navbard.jpg)

Navbar logged out on tablet:

![navbar logged out on tablet](/docs/screenshots/navbart.jpg)

On moblie the navbar will become a dropdown menu which can be toggled by the user:

Navbar logged out on mobile:

![Navbar logged out on mobile](/docs/screenshots/navbarm1.jpg)

![with dropdown menu active](/docs/screenshots/navbarm2.jpg)

Outcome: tests passed

The navbar should show the profile, feed, liked and sign-out links when a user is logged in:

Navbar logged in on desktop:

![Navbar logged in on desktop](/docs/screenshots/navbardin.jpg)

Navbar logged in on tablet:

![navbar on tablet](/docs/screenshots/navbartin.jpg)

Navbar logged in on mobile:

![Navbar logged in on mobile](/docs/screenshots/navbarmin1.jpg)

![Navbar logged in on mobile](/docs/screenshots/navbarmin2.jpg)

Outcome: tests passed

Clicking on 'Sign-up' in the navigation bar should take the user to the sign up page:

Sign up page on desktop:

![Sign up page on desktop](/docs/screenshots/signupd.jpg)

Sign up page on tablet:

![Sign up page on tablet](/docs/screenshots/signupt.jpg)

Sign up page on mobile:

![Sign up page on mobile](/docs/screenshots/signupm.jpg)

The Sign-up form requires the user to fill out all fields. Password fields cannot be too simple or too short:

Sign up form on desktop:

![Password verification](/docs/screenshots/password1d.jpg)

Sign up form on tablet:

![Sign up form on tablet](/docs/screenshots/password1t.jpg)

Sign up form on mobile:

![Sign up form on mobile](/docs/screenshots/password1m.jpg)

Password fields must also be the same:

![password too common](/docs/screenshots/passwordsame.jpg)

Outcome: tests passed

Clicking on 'Sign-in' in the navigation bar should take them to the sign in page:

Sign in page on desktop:

![sign in on desktop](/docs/screenshots/signind.jpg)

Sign in page on tablet:

![sign in on tablet](/docs/screenshots/signint.jpg)

Sign in page on mobile:

![sign in on mobile](/docs/screenshots/signinm.jpg)

The Sign-in form requires the users correct username and password:

Username required:

![users username](/docs/screenshots/usernamerequired.jpg)

Password required: 

![users password](/docs/screenshots/passwordrequired.jpg)

Incorrect username or password:

![incorrect info](/docs/screenshots/incorrect.jpg)

Outcome: tests passed

Clicking on 'Sign-out' in the navigation bar should sign the user out, redirecting them to the home page if they aren't there already:

Signed in before sign out button clicked:

![before sign out](/docs/screenshots/signout1.jpg)

Signed out after button clicked:

![before sign out](/docs/screenshots/signout2.jpg)

Outcome: tests passed

Typing into the search bar on the home page should allow users to search for posts by title or user:

Searching on desktop:

![Searching on desktop](/docs/screenshots/searchd.jpg)

Searching page on tablet:

![Searching on tablet](/docs/screenshots/searcht.jpg)

Searching page on mobile:

![Searching on mobile](/docs/screenshots/searchm.jpg)

Outcome: tests passed

Popular profiles should be displayed to the user:

Popular profile on desktop:

![Popular profiles on desktop](/docs/screenshots/popprod.jpg)

Popular profile on tablet:

![Popular profiles on tablet](/docs/screenshots/popprot.jpg)

Popular profile on mobile:

![Popular profiles on mobile](/docs/screenshots/popprom.jpg)

Outcome: tests passed

Clicking on a popular profile avatar should take the user to that profile page:

Before clicking on a popular profile:

![Profile on desktop](/docs/screenshots/popprobeforeclicked.jpg)

After clicking on a popular profile:

![Profile on desktop](/docs/screenshots/popproclicked.jpg)

Outcome: tests passed

If logged in the user should be able to see and use the follow/unfollow buttons on the popular profiles:

Follow buttons on desktop:

![follow buttons desktop](/docs/screenshots/followd.jpg)

Follow buttons on tablet:

![follow buttons tablet](/docs/screenshots/followt.jpg)

However on mobile it would take up too much screen space, so they are not present here on mobile screens. Instead users will have to click the profile, then follow it from there.

Follow buttons on mobile:

![follow buttons mobile](/docs/screenshots/followm.jpg)

Outcome: tests passed

If the user clicks 'Feed' in the navbar (logged in), they should see the feed page where post from people they are following are displayed:

Feed page on desktop:

![Feed page desktop](/docs/screenshots/feedd.jpg)

Feed page on tablet:

![Feed page tablet](/docs/screenshots/feedt.jpg)

Feed page on mobile:

![Feed page mobile](/docs/screenshots/feedm.jpg)

For example if I were to unfollow 'Yumi_Plays' and refresh the page I would no longer see their posts on the feed:

![Unfollowed post](/docs/screenshots/feedunfollow.jpg)

Outcome: tests passed

If the user clicks 'Liked' in the navbar (logged in), they should see the Liked page where posts they have liked are displayed:

Liked page on desktop:

![Liked page desktop](/docs/screenshots/likedd.jpg)

Liked page on tablet:

![Liked page tablet](/docs/screenshots/likedt.jpg)

Liked page on mobile:

![Liked page mobile](/docs/screenshots/likedm.jpg)

For example if I were to unlike the fist post and refresh the page I would no longer see that post on the feed:

![Unliked post](/docs/screenshots/unliked.jpg)

Outcome: tests passed

The user should be able to scroll infinitely to continuously view posts:

A loading circle will signify that more posts are loading to allow inifinite scrolling:

![infinite scrolling](/docs/screenshots/scroll.jpg)

Outcome: tests passed

The user should be able to click on a post to view it in more detail:

Post on desktop:

![Post on desktop](/docs/screenshots/postd.jpg)

Post on tablet:

![Post on tablet](/docs/screenshots/postt.jpg)

Post on mobile:

![Post on mobile](/docs/screenshots/postm.jpg)

Outcome: tests passed

A user can like and comment on a post if logged in:

Like and comment on desktop:

![Like or comment on desktop](/docs/screenshots/commentd.jpg)

Like and comment on tablet:

![Like or comment on tablet](/docs/screenshots/commentt.jpg)

Like and comment on mobile:

![Like or comment on mobile](/docs/screenshots/commentm.jpg)

Outcome: tests passed

The user should not be able to like their own post:

Unable to like on desktop:

![Unable to like on desktop](/docs/screenshots/likeownd.jpg)

Unable to like on tablet:

![Unable to like on tablet](/docs/screenshots/likeownt.jpg)

Unable to like on mobile:

![Unable to like on mobile](/docs/screenshots/likeownm.jpg)

Outcome: tests passed

The user should be able to click 'add post' in the navbar to add a post (logged in):

Add a post on desktop:

![Add a post on desktop](/docs/screenshots/addpostd.jpg)

Add a post on tablet:

![Add a post on tablet](/docs/screenshots/addpostt.jpg)

Add a post on mobile:

![Add a post on mobile](/docs/screenshots/addpostm.jpg)

Outcome: tests passed
<!--
The user should not be able to add an image that is too large:

Add a post on desktop:

![Add a post on desktop](/docs/screenshots/largeimaged.jpg)

Add a poston tablet:

![Add a post on tablet](/docs/screenshots/largeimaget.jpg)

Add a post on mobile:

![Add a post on mobile](/docs/screenshots/largeimagem.jpg)

Outcome: tests passed
-->
The user cannot create a post without an image and a title:

Image required:

![Image required](/docs/screenshots/image.jpg)

Title required:

![Title required](/docs/screenshots/title.jpg)
<!-- 
The image cannot be too large:

![image too large](/docs/screenshots/toolarge.jpg)
-->

Outcome: tests passed

The user should be able to see the dropdown menu on their own post if logged in:

Dropdown menu on desktop:

![Dropdown menu on desktop](/docs/screenshots/dropdownd.jpg)

Dropdown menu on tablet:

![Dropdown menu on tablet](/docs/screenshots/dropdownt.jpg)

Dropdown menu on mobile:

![Dropdown menu on mobile](/docs/screenshots/dropdownm.jpg)

Outcome: tests passed

Clicking on the 'Edit' button should allow the user to edit the post via the edit form:

Edit post on desktop:

![Edit post on desktop](/docs/screenshots/editpostd.jpg)

Edit post on tablet:

![Edit post on tablet](/docs/screenshots/editpostt.jpg)

Edit post on mobile:

![Edit post on mobile](/docs/screenshots/editpostm.jpg)

Outcome: tests passed

Clicking on the 'Delete' button should delete the post. The page resfreshes and it's no longer visable on their profile:

Before deletion:

![post present](/docs/screenshots/predelete.jpg)

After deletion:

![post deleted](/docs/screenshots/postdelete.jpg)

Outcome: tests passed

The user should be able to see the dropdown menu on their profile page if logged in:

Profile dropdown on desktop:

![Profile dropdown on desktop](/docs/screenshots/profilemenud.jpg)

Profile dropdown on tablet:

![Profile dropdown on tablet](/docs/screenshots/profilemenut.jpg)

Profile dropdown on moblie:

![Profile dropdown on mobile](/docs/screenshots/profilemenum.jpg)

Outcome: tests passed

The user should be able to click 'edit' to be taken to the edit profile form:

The edit profile page on desktop:

![Edit profile page desktop](/docs/screenshots/editprofiled.jpg)

The edit profile page on tablet:

![Edit profile page tablet](/docs/screenshots/editprofilet.jpg)

The edit profile page on mobile:

![Edit profile page mobile](/docs/screenshots/editprofilem.jpg)

Outcome: tests passed

The user should be able to edit their username and password if logged in:

The edit username on desktop:

![edit username desktop](/docs/screenshots/editnamed.jpg)

The edit username on tablet:

![edit username tablet](/docs/screenshots/editnamet.jpg)

The edit username on mobile:

![custom username mobile](/docs/screenshots/editnamem.jpg)

Outcome: tests passed

If the user were to enter a url that doesn't exist the custom 404 page should be displayed:

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

DO I ONLY HAVE 1 PAGE??? inspect > download source code > paste into validator

or
- home
- sign-up
- sign-in
- post
- create post
- edit post
- profile
- feed
- liked

![The W3C Validator showing my HTML](/docs/screenshots/hpvalid1.jpg)


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