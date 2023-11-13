# YOUR SONG LIST

#### Video Demo: <https://www.youtube.com/watch?v=VMjNmGGOpMY>

#### Description: My final project is a website made with Python, Flask, sqlite3, HTML, CSS and JavaScript, titled "Your Songs". It is a platform where users can nominate songs they deem greatest from various countries, adding them to the database. They can also edit the data about songs, vote for songs, and make comments about songs. The ultimate goal is that after users nominate lots of songs from many different countries, based on their votes, we can determine greatest songs globally, as well as greatest songs from each country.

## Overview

The motivation behind the website lies in the fact that while there are many lists of greatest songs ever, almost all of them focus only on songs in English, so there is a lack of such a list that would also take into consideration songs from other countries, sung in different languages.

Besides nominating songs, voting for them, editing and commenting them, users also have their own profiles. For registration, all that is required is a username, a password, and an e-mail. However, users are free to give more information about themselves on their profile, including their country, favorite music, their website, and there is also "about me" section. Just like users can comment the songs, they can also leave comments on each other's profiles.

Besides regular user accounts, there is also the admin account. The admin has some additional rights, for example, they can delete all the comments, both on user profiles, and on songs. This allows the admin the power to remove abusive comments and spam made by other users. Regular users, on the other hand, can only delete the comments they made themselves.

The admin can also lock the editing of a song, preventing other users from making changes to the song. The editing of songs is allowed, because users sometimes can, when nominating the song, enter incomplete, imprecise, or plain wrong information. Other users, when they see such mistakes or incomplete information, are free to edit the information about songs. However, this, of course can be abused, and users can also change the correct information about songs, and enter incorrect information. To prevent this, once the admin is sure that the information entered about a certain song is correct and complete, they can lock the editing of the song, to prevent any further changes made by other users.

There is also a page that displays a log of the 50 most recent changes made to the website, such as nomination of songs, editing songs, voting for them, commenting songs, commenting profiles and deleting comments. This page shows the most recent changes in a table, showing for each change, the following information: the type of change, who made the change, which (if any) song is affected, which (if any) user profile is affected and when the change was made.

## Functionalities of the website

### Layout

The layout consists of all the visual elements in the website that all the pages have in common.

The layout consists of the div element with the class main-container that contains the entire layout of the website. It is a grid with 2 columns, 4fr and 1 fr. The width of the container is set to 80% of the body element.

The layout starts with a large logo, which takes both columns. By clicking the logo the user is redirected to the root route, which displays the master list of all songs.

Below the logo, there is a nav element which is the main navigation of the website. It also takes both columns. When users aren't logged in the only 2 links displayed in the navbar are "Register" and "Log in". When they are logged in, from the main navigation they can access: "My Profile", "Edit profile", "Log out", "Song list", "Nominate a Song", "Search song", "Countries" and "Users".

Below the navigation, there are 2 sections, main and aside. Main contains actual content of each page, and aside is the sidebar, each taking 1 column of the grid: main 4fr and aside 1fr. Sidebar contains links to 3 similar websites, together with their logos. By clicking on their logos, it's possible to go to those websites.

At the bottom of the page there is a footer. The footer takes both columns and contains the basic information about the website, and link to "Change Log" page, where you can see the latest changes to the website.

#### Responsive design

When the website is viewed in cellphones, certain changes in design occur. First, the links of the navbar are displayed vertically, instead of horizontally. Second, the sidebar is displayed below the main content and not next to it. Third, main-cointainer that contains the whole layout of the website is now at 100% width instead of 80%. This is all achieved with a media query. Besides, in a phone version of the website font sizes are smaller and certain table columns are not shown. For example, desktop version of the master song list contains the following columns: ID, Song, Artist, Country, Language, Votes, Year, Upvote and Downvote. Cellphone version does not show Language, Upvote and Downvote columns. Voting is still possible on cellphones, but only from the individual song pages.

### Displaying information

#### Homepage / Master song list

On the homepage, there is a short intro about the website, after which the master list of all songs is shown, organized in a table. Songs can be sorted by ID, song name, aritst, country, langauge, number of votes and year. The default sorting is by ID, descending, so that the most recently nominated songs appear at the top of the table. Users can vote for each song directly from this table.

#### Individual pages about songs

Users can also click on each song name, and that leads them to individual pages for each song, on the route /song?id=songid . Individual pages about songs contain information about the song displayed in a table, after which there are buttons for upvoting and downvoting the song, as well as for editing. If the website is viewed while logged in as an admin there are also buttons for locking and unlocking editing of the song.
Finally there is a text area and button for adding comments, after which comments are displayed, with the most recent ones on top.

#### Countries

There is also a route /countries. It shows, in a table all the countries from which some songs are nominated so far. Countries can be sorted by name, number of songs, and number of votes. Default sorting is by name.

#### Individual pages about each country

Users can click on each country, which leads them to route /country?c=countryname . On this route the individual pages for each country are displayed. On those pages, there is a list of songs, shown in table, similar to the master table of all songs, but only from that country. From this table, users can also vote for songs and access individual pages for each song.

#### Users

There is also a route /users, where you can access a list of all registered users, displayed in the table with columns: ID, Username, Country, Nominations (the number of songs they nominated), Upvotes, Downvotes, Comments (the number of comments they left on songs), Profile comments (the number of comments they left on users profiles) and website. The users can also be sorted by any of those columns. From this list, it's also possible to access user profile pages.

#### Profile pages of users

At the route /profile?u=username there are individual profile pages for each user. They contain the information about the user displayed in a table. Besides all the infomation that is available in the Users table, individual profile pages also contains "About me" and "Favorite music" sections. Below that information, there is an option to add a comment to the profile, and below that, there are all the old comments displayed in reverse chronological order, with newest comments at the top.

#### Change log

At the route /changes the last 50 changes to the website are displayed in a table. It contains information about who made the change, the type of change, the affected song (if any), the affected user profile (if any) and when the change occured. From this table, it's possible to directly access the profiles of users who made the change, as well as the pages of affected songs and profiles of affected users. Change log can be accessed by clicking on "Change log" link which is inside the footer.

### Functionalities that change data

#### User registration

New users can register by accessing route /register from the main navigation. They must enter username, email, password and password confirmation. If any of those are not entered, or if username they are trying to register is already taken, or if the password and the confirmation do not match, the website return an apology and the registration can't proceed. Apology function is taken from helpers.py file of the Finance PSET.

Once the registration is successful, the user is automatically logged in and the message Registered! is flashed. They are also redirected to the root route.

#### Editing user profiles

Each user can edit their own profile by accessing /editprofile route, which is accessible from main navigation. There they can add or change information about their country, website, favorite music, and there's also "About me" section that they can edit. Username and password can't be changed. The information about the user that's already in the database is displayed as a placeholder in input elements. Changes can be saved by clicking "Save changes" button. This also redirects users back to their profile.

#### Voting for songs

Voting can be accessed from the main song list, from lists of songs of specific countries and from individual song pages. After voting, user is redirected to the same page from which they voted. Each user can give just one positive or one negative vote for each song. For example, if they have already given a positive vote to a song, they can't give another positive vote. But they can change their opinion, and give a negative vote to a song they gave a positive vote in the past (and vice versa). When they change their opinion, their old vote is deleted and only their new vote counts. Voting changes the number of votes a song has, and it also changes the number of upvotes (or downvotes) the user has. If the user tries to double vote, the message "You've already cast your vote" is flashed. If the voting is successful the message "Thanks for voting" is flashed.

#### Nominating songs

Nominating songs can be reached via route /nominate, which is accessible from the main navigation. Required fields users must fill when nominating a song are song name and country. If they don't fill those fields, the site gives them apology stating that this information is missing. Also, if the user enters a country that doesn't exist, they will receive apology "Invalid country". Other fields they can fill are: artist, year and language of the song. When song is entered into database it also automatically gets an ID, which is autoincremented. Also, when a song is nominated, the count of nominated songs for that particular user is increased by one.

#### Editing songs

Editing functionality is accessible via individual pages dedicated to each song. On that page, below the information about the song there is a button "Edit song / Correct mistakes", which leads to a form which allows the users to change the information about the song. The form allows users to change the title, country, artist, language and year of the song. Before each text input there is a label. Inside text inputs old values are shown as placeholders. This form is only reachable if the editing isn't locked. If the editing is locked, upon clicking on the button "Edit song / Correct mistakes" the message "Editing locked" is flashed to the user.

#### Locking and unlocking editing of songs

These are functionalities only avaliable to the admin. If the users is logged in from the admin account, on the individual pages of each song, below buttons for voting and editing the song, two additional buttons are visible: lock editing and unlock editing. By clicking "lock editing" the admin can lock editing of the song, preventing other users from making changes. Likewise, they can unlock the editing of the song by clicking on "Unlock editing" button. Upon locking / unlocking the song, they will also receive a flashed message "Editing locked" or "Editing unlocked". If they click "lock editing" on a song that was already locked, they'll receive the message "Song was already locked". Likewise, if they try to unlock the song that was already unlocked they will receive the message "Song was already unlocked".

#### Commenting on songs

Each user can leave comments on each song. To comment they must visit the individual pages of songs. On those pages there is a text input in which they can enter their comment and then click on the button below "Add comment". When the comment is added the message "Comment added" is flashed, and the comment appears in the comment section of the page dedicated to that particular song. The user is redirected to that same page. Also when they add a comment the comment count of that user is increased by one.

#### Deleting song comments

Each user can delete their own comments they left on songs, by clicking the "Delete" button that is visible inside the comment itself. The admin can also delete other user's comments.

#### Commenting on user profiles

Each user can leave comments on profiles of other users, as well as on their own profile. To comment they must visit profile pages of users. On those pages there is a text input in which they can enter their comment and then click on the button below "Add comment". When the comment is added the message "Comment added" is flashed, and the comment appears in the "The Wall" of the profile page of the user whose profile is being commented. The user is redirected to that same page. Also when they add a profile comment, the profile comment count of the user who is making the comment is increased by one.

#### Deleting profile comments

Each user can delete their own comments they left on profiles of users, by clicking the "Delete" button that is visible inside the comment itself. The admin can also delete other user's comments.

### Other functionalities

#### Searching for songs

Users can search for songs by clicking on "Search songs" in the main navigation. This leads them to /searching route, where they can search for a song by song name and by artist, by entering text in one of the 2 appropriately labeled input boxes. As they enter the text, automatically the list appears below with all the songs that contain the searched text in its title, or in artist's name, depending on which input box the user used. The list appears as the text is being entered, the users don't need to press any buttons. This is implemented with JavaScript.

#### Logging in and logging out

If they aren't already logged in, the existing users can log in by clicking "Log In" in main navigation. This leads them to log in page. Also, if they aren't logged in and they try to perform an action that requires being logged in, such as voting for a song, they will be automatically redirected to the "Log in" page. On the "Log in" page, they are required to enter their username and password. If they don't enter the username, or the password, or the password they entered is incorrect, the website will give them appropriate apology message. Users who are already logged in, can log out by clicking on "Log out" in the main navigation.

## Files and Implementation Details

### app.py

This is the main python file that contains the application itself and most of the functionalities of the website are implemented in this file. After importation of necessary libraries and configuration of the application, the session, and the database, this files consists of the series of functions, associated with certain routes, through which various functionalities of the website are implemented. Another thing that is done at the very start of the file is filling the list countries with the content of the file countries.csv. That file contains the list of all countries in the world. The purpose of that file is to make sure that users can only enter valid country names when nominating or editing songs. There is more than one entry for some countries, for example both US, USA, United States and United States of America are entered as valid country names. The functions used in this file are the following:

#### adjustcountryname(countryname)

This function makes sure that country names are uniformely entered in the database, so that you don't count the same countries multiple times. For example, if the user entered a country name "UK" or "Great Britain", the function will adjust the name to the most common form, which is "United Kingdom".

#### after_request(response)

The purpose of this function is to make sure caching of responses is disabled. This is the same function that was also used in Finance PSET.

#### index()

This function handles displaying the list of all songs on the homepage of the website and renders the file index.html.

This function is defined at the route "/", and uses methods "GET" and "POST". When the route is reached via GET method, this function accesses the database songs.db and saves the information about all the songs from the database inside the variable rows (and, by default, orders them by song id, in descending order, so that the songs that are last added to the database, which have the highest id, are displayed first), and then renders the file index.html and sends this variable rows to that file, so that it can be used as a placeholder to display the information about the songs in a table.

When the route is reached via POST method, the function does the same thing, but first saves inside the variable "method" the information that it received from index.html about sorting method that should be used when displaying songs. Then, depending on which method the user selected, it creates the variable "rows" by selecting all songs from the database and then sorting them according to the chosen method. Then, just like before it renders the file index.html and sends the variable "rows" to it, to be used as a placeholder.

#### login()

This function handles logging it to the website.

This function is implemented in a very similar way as login() function in the finance PSET. It is defined at the route "/login". If the route is reached via GET method, the function simply renders the file login.html.

If the function is reached via POST method, it first clears the session, to make sure no one is logged in anymore. Then, it checks if the user entered the information in the form inside the file login.html, about their username and password. If the user didn't enter some of the information, it sends them appropriate apology. If the user entered all the fields, then the function accesses the database to find the information about the user. If there are no users registered under that name, or if there are multiple users registered under that name, or if the password does not match its hash that is saved in the database, the function returns the appropriate apology. To check the password against saved hash, the function check_password_hash() from the library werkzeug.security is used.

If the username is valid and the password is correct, then the function logs in the user, by setting session's fields "user_id", to that user's id, and the "username" to that user's username. Finally it redirects the user (after logging them in) back to the homepage, (that is to the route "/").

#### logout()

This function handles logging out of the website.

This function can be reached via route /logout, and all it does is clear the session (that is delete the information about which user is logged in), and then redirect the user to homepage (i.e. to "/" route).

#### register()

This function handles the registration of new users.

This function can be reached via /register route. If it's reached via GET method, it simply renders the file register.html. If it's reached via the POST method, it first check the information that user entered in the form inside the register.html file. It checks whether the user entered the username, email, password and confirmation of password. If any of the fields aren't entered it return appropriate apology. Then it also makes sure that password and the confirmation are the same. (If not, again, it returns an apology). Finally it checks if the username has already been taken, if that is the case, it returns apology.

If all the fields are entered, the password and confirmation match, and the username has not been taken, then it first hashes the password the user provided and saves the hash in the variable "hash". Then it inserts a new row in the table users of the database, filling the columns username and email with the information obtained from the user, and the hash with newly created hash.

Once the user is inserted in the database, the function logs them in by setting session's fields "user_id", to that user's id, and the "username" to that user's username.

Then it also inserts a new row in the table "changes" of the database, entering information about the action of user registration itself (the type of change, who did it, which user is affected, and when it occured). The information about timing of the registration is obtained by using the function datetime.now() from the library datetime.

Finally the function flashes the message "Registered!" (using the function flash()) and redirects (now registered and logged in) user to the homepage.

#### nominate()

This function handles the nomination of new songs.

This function can be reached via route "/nominate". If accessed via GET method, it simply renders the file nominate.html. If reached via "POST" method it accesses the information the user entered in the form inside the file nominate.html. First it makes sure that the user entered the required fields, which are song name and country. If any of these fields are left blank, or the country is not among those countries listed in flie countries.csv, the user receives an appropriate apology. If both song name and country are provided and the country name is valid, the new row is inserted in the table songs inside the database.

Since there are other fields that user might have entered which aren't obligatory, now we need to save those fields into our database too. But to do that, we need to know which song from the database to update.
To do that, we save, inside the variable "song_id", the id of the song with maximum id from the entire table songs. This is because the song that we just entered will have the highest id, due to autoincrementing of IDs. So the song we just entered and that we want to update, will be the one with max id.

Once this is saved we check for each of the other fields (artist, year and language) in the form if the user left them blank. If they didn't then we update the table songs so that this information is entered, each time updating the song whose id is equal to our variable song_id.

Finally we make sure we have the information necessary for updating the table changes, that deals with changes we made. We get info about the user who is logged in by accessing session["user_id"]. We get the info about the time by using datetime.now().

First we update the table users in such a way that we increase the number of nominatios for user with id session["user_id"] by one (that is for currently logged in user who made the nomination).

Then we also insert the new row in table changes, with the information about the type of change, the user that did it, which song is affected, and when it occured.

Finally the function flashes message ("Song nominated!") and redirects the user to home route ("/").

#### vote()

This function handles voting for songs.

It can be reached via route /vote and only uses POST method.

This function needs to update the table songs, so that the score of a song is increased or decreased according to the vote. It also needs to update the table users, so that the number of their upvotes and/or downvotes is increased or decreased according to the vote. It also needs to update the table votes, to keep track who voted for/against which songs.

To be able to make those changes, first it saves the information about the user who is voting in variable user_id, about the song that is being voted for (or against) in the variable song_id, about the number of upvotes and downvotes the user has in the variables upvotes and downvotes, respectively, and about the old score of the song before voting in the variable old_score and about the number of votes (positive or negative) the particular user gave to a particular song in the variable oldvotes.

The function gets information about the current vote from the form that's used in all the pages that access this function: index.html, country.html or song.html. This information is saved in the variable newvote.

Then the function deals with 6 different cases, and in each case updates the tables appropriately. The cases are:

1. user voting for a song they already voted against in the past,

2. user voting for a song, the first time,

3. user trying to vote for a song again,

4. trying to vote against a song again

5. voting against the song for the first time

6. voting against the song they previously voted for

The function makes sure the user can't double vote on a song. They can change their vote, but if they have, for example, already voted for, they can't give another vote for.

The function also makes sure the tables are appropriately updated. For example if the user votes for a song they previously voted against, the function makes the following changhes: the number of upvotes in the table users is increased by 1 for that user, the number of downvotes in table users is decresead by one for that user, the score of the song is increased by 2 (because a downvote is replaced by an upvote), and the number of votes in table votes is set to 1 for that user/song pair.

Finally, after the voting itself is handled, the function updates the table changes by inserting a new row with the information about the type of change, who did it, which song is affected, and when the change occured.

Then the function flashes message ("Thanks for voting") and redirects the user back to the page from which they voted.

In case user tried to give a double vote to the song, the function doesn't make any changes to the database, but just flashes the message "You've already cast your vote" and redirects the user back to the page from which they voted.

#### states()

This function displays the list of countries from which there are songs in the database. It should have been called countries but that name was already taken by the variable that contains the list of countries, for this reason this function is called states()

It can be reached via route "/countries" and 2 methods GET and POST. If it's reached via get route it accesses the database and from the table songs, gets information about countries, the number of votes the songs from each country received, and the number of songs from each countrie. This is achieved by using COUNT(\*), SUM(votes) and GROUP BY(country) on the songs table. By default, countries are ordered by country name. It saves it in variable rows, which it sends to the file countries.html while rendering it.

If it's reached via POST route, it does the same thing, the only difference it first gets the sorting method from the file countries.html, and then when accessing the database, sorts the countries according to the criteria selected by user (country name, sum of votes or number of songs in each country)

#### country()

This function handles displaying lists of songs from just one country.

It's defined on route /country, it uses methods GET and POST. It works in the same way as index function, the only difference is that instead of displaying all the songs, now only the songs from a specified country are displayed. Again, if it's reached via GET mode it orders the songs by song ID in descending order which is default, and if it's reached via POST method the users can select by which method to order the songs. To display the songs it renders the file country.html.

#### users()

This function deals with displaying the list of users.

It is defined at the route /users, and can be accessed with GET and POST methods. In any case it renders the file users.html while sending it the information from the database about the users saved in the variable rows. If it's reached via GET route it displays users sorted according to their ID (default sorting). If it's reached via POST mode, it first gets the sorting method from the file users.html, and then orders the users according to the criteria selected by the user.

#### profile()

This function deals with displaying user profiles.

It is defined at route /profile. It uses only GET method. From the URL it gets the infromation about whose profile to display, and it saves it in the username variable. From session it gets the info about which user is currently logged in, and saves their ID in variable user_id, and their username in the variable loggedin. Then it checks whether the user who is logged in is an admin, and saves this information in the variable isadmin.

Then it saves the info about the user who's profile is to be displayed in the rows variable. It also obtains their id from the database and saves it in the id variable.
It also saves the information about all the comments made to that users profile in the comments variable.

Finally it renders the profile.html file, while sending it variables username, rows, loggedin, id, comments, isadmin and user_id. All those variables are necessary for the file profiles.html to properly function.
This is because this file not only displays the info about the user in the table, but also has a title where the username is displayed, and also has comments section, as well as the functionality to add your own comment. Also it makes it possible for users to delete their own comments and for admins to delete each users comments.

#### myprofile()

This function deals with displaying the profile of the person who is currently logged in.

It's just a modified version of profile() function. The main difference being that it doesn't get the info from URL about whose profile to display, but instead it gets that information from session.

#### editprofile()

This function allows users to edit their profiles.

It is defined at the route /editprofile and it uses methods GET and POST. First it takes the information about username and id of the user currently logged in from the session and saves it in variables username and user_id. If it's reached via GET method it saves in a variable rows the information about the user that is currently logged in and sends it to the file editprofile.html while rendering that file.

If it's reached via POST method it checks which fields in the form user entered and which they left blank and then for all the fields in which the user entered the information, it updates the corresponding columns in the table users. Then it obtains the information about the current time by using datetime.now() function, and finally it inserts the new row in the table changes with the information about what changes have been made (in this case it's "Editing user profile"), who made them, which user is affected, and when the change occured. Once this is done the function flashes the message "Profile updated" and redirects the user to their profile (the route /myprofile).

#### song()

This function handles displaying pages about individual songs.

It is defined at /song route and only uses the GET method. In a similar way as functions profile() and myprofile() it obtains the information about the id of the user currently logged in, whether they are admin or not, the id of the song being displayed (from the URL) and the name of the song being displayed (from its ID). Then it accesses the database and saves the information about the song being displayed in the rows variable, and the information about the comments in comments variable. Finally it renders the file song.html, and provides it with all this information. As in case of profile(), the information is necessary for displaying not just the information about the song, but also it's title and the comments, and for deciding who can delete comments. Again, users can only delete their own comments, while admins can delete everyone's comments.

#### deletesongcomment()

This function handles deleting comments users left on songs.

It's defined at /deletesongcomment route and it only uses POST method. It needs to delete the comment from the comments table and to update users table so that the comment count of the user making the comment is decreased by 1. To achieve this, it needs to obtain the information of which user is deleting the comment - from the session it gets the info about user logged in and saves it in variable performer. From the form it gets the id of comment being deleted and saves it in comment_id variable. It also gets the information about who made the comment that is being deleted, and to which song this comment was posted. It saves those information in variables user_id and song_id.

Then it updates the users table so that their comments number is decreased by one. It also deletes the comment from the database. Finally it inserts a new row in the changes table with the information about the type of change ("Deleting song comment"), who did it, which song is affected, and when it occured (which is obtained via datetime.now()).

Eventually it flashes "Comment deleted" and redirects the users to the page they were on, using redirect(request.referrer) method.

#### deleteprofilecomment()

This function handles deleting comments users left on profiles of other users (or on their own profile).

It's defined at /deleteprofilecomment and uses only POST method. It works in a similar way as deletesongcomment() function. The main difference is that it deals with the table profilecomments instead of comments, and in users table it changes the column profilecomments instead of comments.

#### lock()

This function allows the admin to lock editing of the song so to prevent other users from making changes to songs they are sure have all the information entered correctly.

It is defined at /lock route and only uses POST method.

It works by setting the value of the column "islocked" in the songs table of the song being locked to 1. First it checks if the song is already locked in which case it makes no changes to the database and just flashes the message "Song was already locked" and redirects the user back to the page from which they arrived.

If the song wasn't locked it lockes the song, enters the new row in changes table (the type of change being "Locking song editing"), flashes the message "Editing locked" and redirects the user back to the page from which they arrived.

#### unlock()

This function allows the admin to unlock editing of songs.

It works in the same way as lock() function, the only difference is that it sets the value of the column "islocked" in the songs table of the song being unlocked to 0.

#### editsong()

This function deals with rendering the form in the editsong.html, which users can use to edit information about the song.
It's defined at /editsong route and only uses GET method.
It gets the information about which song to edit from URL and saves it in the variable id.

It makes sure not to render the form if the editing is locked - in that case it just flashes "Editing locked" and redirects the user back to the page from which they arrived.

If the editing isn't locked it renders the editsong.html which contains the form for editing the song, providing it with the rows variable, which contains the information about the song being edited that was obtained from the database.

#### edit()

This function updates the database when the user submits the form on editsong.html.

It's defined at /edit route and only uses POST method.

It checks which fields the user entered in the form and updates the corresponding columns in the songs table for the song being edited. From the form it also gets the information about the id of the song, so that it can update the information only about the song that's being edited.

Finally it updates the changes table, providing it with the information about the type of change ("Editing song"), who did it (obtained from session), which song is affected and when the change occured. Then it flashes "Song updated!" and redirects the user to the page of the song that was edited.

#### comment()

This function handles commenting on songs. It's defined at /comment route and only uses POST method.

It inserts the information in comments table about the comment being made, updates the users table so that the comment count of the user who made the comment is increased by one, and finally inserts a new row in the changes table documenting the change being made "Commenting a song", who did it, which song is affected, and when the change occured.

Lastly it flashes "Comment added!" and redirects the user to the page of the song being commented on.

#### profilecomment()

This function handles commenting on user profiles. It's defined at /profilecomment route and only uses POST method.

It works in a similar way as comment() function, the only difference being that it deals with profilecomments table and profilecomments column in the users table (instead of comments table and comments column).

#### search()

This function returns the search results, when users search for songs. It's defined at /search route and only uses GET method.
This function is called by asynchrounous JavaScript function within search.html. It gets the URL from the JavaScript (in form of '/search?song=' + songinput.value OR '/search?artist=' + artistinput.value), which it can use to search for the songs in the database.

It saves the user input in variables song and artist, and then depending on which field in the form the user entered, it selects all the songs in which the song name or the aritst is similar to what the user entered, limiting the output to 50 results.

Eventually it renders the page results.html, sending it the output of the database query in the placeholder songs. Results.html consists of just li elements representing all the songs that are search result, and this html file isn't used on its own, but within search.html.

#### searching()

This function simply renders the page search.html which contains the form for searching the songs, and in which the search results will also be displayed as a result of asynchronous JavaScript function.

It is defined at the route /searching and only uses GET method.

#### changes()

This function handles displaying the list of most recent changes to the database of the website. It renders the file changes.html.

It's defined at route /changes and only uses GET method.

It saves the 50 most recent changes in the rows variable which it sends to the file changes.html. Before sending the results of the query, it transforms the raw database output, so that, if a song is affected by a change a field affecting_songname is added to the rows dictionary, and if a user is affected by the change, the field affecting_username is added to rows dictionary. This is done to allow the file changes.html to display usernames and song names of users and songs affected by changes, instead of just displaying their ids.

### helpers.py

This is a reduced version of the file helpers.py from the Finance PSET, retaining only those functions that are still needed. After importing necessary libraries, it contains just two functions defined within:

#### apology(message, code=400)

This function handles displaying of apology messages in case that user has made some errors when entering the data in some of the forms used on the website. It takes 2 arguments, message, which is a string to be displayed as apology, and code, which is server response code to be displayed with the apology message. By default it's set to 400.

#### login_required()

This function defines a decorator to be used for all the functions for which login is required. If the user who is not logged in tries to access a function which requires login, it redirects them to the /login route, so that they can log in.

### countries.csv

This is a list of countries that's used as a CSV file within the file app.py. Its purpose is that people can only enter the valid country names when they're entering the information about the songs. The file countains multiple entries for certain countries, to accommodate different ways in which users might enter countriy names: for example, all of the following country names are listed: US, USA, United States and United States of America.

### requirements.txt

This is the list of required libraries that are necessary for running the app.

### README.md

This is the file you're currently reading, and contains the detailed information about the functionality of the application and its implementation.

### songs.db

This is the database of the application. It contains the tables: users - containing the information about users of the website, songs - keeping the information about the songs that users nominated so far, comments - keeping the information about comments the users left about individual songs, profilecomments - keeping the information about comments users left about profiles of other users (or on their own profile), sqlite_sequence - an autogenerated table that's used for autoincrementing id columns of other tables, votes, which keeps track about which user voted for, or against, which song, and changes which keeps track about the changes made to other tables in the database.

The tables users, songs, comments, profilecomments and changes all have id as their autoincremented primary key. The table votes has no primary key.

The tables users and songs don't have foreign keys.

The table comments and votes have foreing keys song_id and user_id, which reference id column in songs and users tables respectively.

The table profilecomments has foreign keys profile_id and user_id which both reference the id column in users table. However profile_id keeps the information about the user on whose profile the comment is made, and user_id keeps the information about the user who made the comment.

There are two indexes made for the table songs, to make it faster for users to search for songs. One is made on the name column, and the other on the artist column, as those are the 2 criteria users can use to search songs.

### Templates folder

This folder contains HTML files used by the website.

#### apology.html

The purpose of this file is to show the apology message when the user doesn't enter enough information or enters incorrect information while filling certain forms.

Like all the html files (except results.html and layout.html itself), it extends layout.html. It is the same apology.html file that was used in Finance PSET.

#### changes.html

This file displays the change log inside the table, by showing data it receives from the changes() function. Two of the columns inside the table have the class "collapsable". Elements with this class are only visible on big screens, but not on cellphones. This was done to make the website more responsive. So on desktop, users can see the columns: ID, Change type, Done by, Affected user, Affected song and Time, while on cell phones the columns Affected user and Affected song are not displayed.

#### countries.html

This file displays in a table all the countries that have songs in the database, by showing data it receives from states() function. It also contains a form with select and option elements, and a submit button, that allows users to select how they want the countries to be sorted. The form gets submitted to the "/countries" route using the post method.

#### country.html

This file displays in a table all the songs in the database from a particular country. It receives the data from the country() function. It also allows choosing the sorting method by using a form with select and option elements and a submit button. The form gets submitted to the country?c={{country}} route using the post method. Again, certain columns inside the table are collapsable, for responsiveness reasons. Finally, next to each song, inside the table, voting buttons are added, to allow the users to upvote or downvote a song. They are implemented using a form with 3 hidden inputs and a submit button. The form gets sent to the /vote route using the post method.

#### editprofile.html

This file displays a form that users can use when they want to edit their profile. The form is submitted to /editprofile route using the post method.

The form consists of a series of labels and input elements and a submit button. Label elements show what data has to be inputed, and inside the input elements old data (received from editprofile() function) is shown as placeholders, to make it easier and more practical for users to edit their profiles. The input elements regarding "About me" and "Favorite music" are implemented using textarea html element, rather than classical input element, because these fields will typically require more text to be enetered.

#### editsong.html

This file displays a form that users can use to edit songs. The form is submitted to /edit route using the post method. Just like in editprofile.html, the form consists of label and input elements and the submit button. Inside the input elements old data (received from the function editsong()) is shown in placeholders.

#### index.html

This is the homepage of the website. This file first give the users a quick intro about the website in several p elements, after which it shows the table containing all the songs in the database. Again certain columns are collapsable for better responsiveness. Again, the users can select which criteria to sort the songs by, which is implemented using a form with select and option elements and submit button. The form gets submitted to "/" route using the post method. Again, inside the table there are upvote and downvote buttons, which allow the user to vote for songs. They are implemented using a form with 3 hidden inputs and a submit button. The form gets sent to the /vote route using the post method.

#### layout.html

This file defines the layout of the website. All the other html files except results.html extend this file. The layout consists of the div main-container that encompasses everyhing inside the body element. This div is used so that the width of the whole content can be reduced to 80% on desktops, for simply esthetic reasons. The main-container is also a grid container, it defines the structure of the website as a grid with 2 columns of 4fr and 1fr.

Inside the main container, first comes the logo of the website (an img element inside the div). Below the logo, there is the main navigation, defined using the nav element with the class main-navigation. This nav element is a flex container. It displays links to various parts of the website as flex items. If the user is on desktop, the flex direction is default, that is row, so the items in the menu are showed in the same line one next to another. If the user is on cellphone, the flex direction is column, so the items are shown vertically, one above the other. Also, which menu items will be shown depends on whether the user is logged in or not. If the user is not logged in, the only two items they see in the menu are "Register" and "Log in", otherwise, they see the full navigation. This is implemented using if and endif in jinja.

Also, inside the main navigation, if the user is logged in, the first item, before all the links is a greeting, which greets them using their username obtained from session["username"].

Below the navigation, the element for displaying flashed messages is defined. It comes right below the nav and before the main content.

Next there comes the "main" element inside which comes the content of all the other html pages.

Next, there is aside element which defines the sidebar. The sidebar consists of the 3 pictures inside "a" elements which allow the user to visit other similar websites. Each picture is a logo of these other websites, which include https://digitaldreamdoor.com/, https://www.rollingstone.com/, and http://www.acclaimedmusic.net/. In CSS the aside element is defined as a flex container with flex direction set to "column".

In CSS main and aside elements are put in the grid in such a way to be displayed next to each other on desktop. On cellphones, on the other hand, the aside comes below the main.

Finally a footer is defined. Inside the footer, as a part of the text, there is a link to my personal website on github, and a link to CS50x course. Also from the footer, and not from anywhere else, the users can access change log page. The link to change log page is in the footer, because it's of secondary importance for regular users and is more important to admins who want to monitor the changes users made to the website.

#### login.html

This file contains the login form. The form is submitted to /login route using the post method. It just has 2 text inputs for username and password and submit button.

#### nominate.html

This file contains the form for nominating new songs. The form is sumbitted to /nominate route using the post method. Input fields are: name, country, artist, language and year.

#### profile.html

This file displays profile pages of users. First it displays the information about the user in a table, the information is obtained from profile() or myprofile() function. After that there is a form for submitting comments. The form has one hidden input element, that sends the user id to the app, also the text area and the button. The form is submitted to /profilecomment route using the post method. Finally there is "The Wall" inside of which the old comments that people left on the user profile are showed. Comments are implemented as a divs with 2 p elements that show information about the comment and the comment itself, and a button that allows user to delete their own comments, and allow admins to delete everyone's comments. When the user sees the comments of other users, there's no delete button.

#### register.html

This file displays the form for registration of new users. The fields are username, email, password and confirmation. The form is submitted to /register route using post method.

#### results.html

This is the only file that does not extend layout.html. It consists of a jinja FOR loop that results in series of li elements in which the search results of the searching for songs are displayed. This html file is never showed on its own, but instead the asynchronous function in JavaScript, inside search.html request this file from the function search().

#### search.html

This file contains the form for searching for the songs by song name or by artist name. There are just 2 input elements with placeholders, but there's no search button. This is because searching is handled automatically by an event listener tied to input elements. Below inputs there is a "ul" element - unordered list inside of which the file results.html, which consists of a series of li elements will be rendered by search() function.

This functionality is implemented through 2 asynchronous JavaScript functions, one for each input element. They add event listeners to each input element. The triggering event is input, and the asynchrounous functions request from the search() function the search results, specifying the search URL which is '/search?song=' + songinput.value or '/search?artist=' + artistinput.value. The results received from the search() function are then assigned to "ul" element on the same page as innerHTML attribute.

#### song.html

This file displays the information about individual songs. First it displays the information about the song in a table, the information is obtained from song() function. Then there are 3 buttons, for upvote, for downvote and also for editing the song. Voting buttons are implemented in the same way as in other files. The "Edit song / correct mistakes" button is inside "a" element that has href attribute /editsong?id={{id}}, this way it sends the information about the id of the song to editsong() function via get method.

Then just like in profile.html, there is a form for adding comments, and a section for displaying old comments below. They are implemented in a similar way as the analogous sections on profile.html, the only difference is that the forms submit to /comment and /deletesongcomment routes instead.

#### users.html

This file displays a table that contains information about users. It's similar to index.html page. Again there is a form for selecting sorting method. Again, some of the columns are collapsable, that is, only shown when viewed on desktop, for the sake of responsiveness.

### static folder

This folder contains styles.css, favicon.png and pictures folder.

#### styles.css

All the CSS for the website is defined in styles css. There's no bootstrap used. Everything is pure CSS. At the beggining there is a "global reset" which sets all the margins and paddings to zero for all the elements, to make later customization easier. Also box sizing is defined as border-box for everything to allow easier positioning of elements. Font family is defined as "Gill Sans", sans-serif.

The layout of the website is defined as grid, this grid behaves differently on desktops vs. cellphones. This is handled by using media query.

First are defined styles using element selectors, then some additional styles using class selectors. "a" elements are styled using pseudoclasses, that define their behavior in different situations (link, visited, hover, active).

All the necessary adaptation to the layout for viewing on smaller screens are defined inside the media query.

#### favicon.png

This is a small picture / logo of the website that appears in its tab in browsers.

#### pictures folder

This folder contains the following pictures:

acclaimed.png - Logo of the Acclaimed music website, used inside the link in aside that leads to the URL of that website.

ddd.png - Logo of the Digital Dream Door website, used in the same way.

rollingstone.png - Logo of the Rolling Stone website, used in the same way.

delete.png - A small picture used as a button for deleting comments on songs and profiles.

downvote.png - A small picture used as a button for downvoting songs.

upvote.png - A small picture used as a button for upvoting songs.

songslogo.png - A large logo for the website that's displayed at the top of the each page.

#### flask_session folder

An autogenerated folder that contains the information about sessions of logged in users.
