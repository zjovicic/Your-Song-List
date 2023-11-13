import os
import csv
from datetime import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

countries = []
with open("countries.csv") as file:
	file_reader = csv.reader(file)
	for row in file_reader:
		countries.append(row[0])

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///songs.db")

def adjustcountryname(countryname):
    if countryname in ["PRC", "People's Republic of China"]:
        countryname = "China"
    if countryname in ["UK", "Great Britain", "United Kingdom of Great Britain and Northern Ireland"]:
        countryname = "United Kingdom"
    if countryname in ["US", "USA", "United States of America"]:
        countryname = "United States"
    if countryname in ["Antigua & Deps", "Antigua & Barbuda"]:
        countryname = "Antigua and Barbuda"
    if countryname in ["Korea, North", "DRK", "Democratic Republic of Korea", "Korea, Democratic Republic of"]:
        countryname = "North Korea"
    if countryname in ["Korea, South", "Republic of Korea", "ROK", "Korea, Republic of"]:
        countryname = "South Korea"
    if countryname == "Kosovo":
        countryname = "Serbia"
    if countryname == "Russian Federation":
        countryname = "Russia"
    if countryname == "Guinea Bissau":
        countryname = "Guinea-Bissau"
    if countryname in ["Bosnia", "BiH"]:
        countryname = "Bosnia and Herzegovina"
    if countryname == "CAR":
        countryname = "Central African Republic"
    if countryname in ["Congo", "Republic of Congo", "Congo, Republic of the", "Congo, Republic of"]:
        countryname = "Republic of the Congo"
    if countryname in ["DRC", "Democratic Republic of Congo", "Congo, Democratic Republic of", "Congo, Democratic Republic of the"]:
        countryname = "Democratic Republic of the Congo"
    if countryname == "Czech Republic":
        countryname = "Czechia"
    if countryname == "Republic of Ireland":
        countryname = "Ireland"
    if countryname == "Macedonia":
        countryname = "North Macedonia"
    if countryname in ["St Kitts & Nevis", "St Kitts and Nevis", "Saint Kitts & Nevis"]:
        countryname = "Saint Kitts and Nevis"
    if countryname == "St Lucia":
        countryname = "Saint Lucia"
    if countryname in ["Saint Vincent & the Grenadines", "Saint Vincent and Grenadines", "Saint Vincent & Grenadines", "St Vincent & the Grenadines", "St Vincent and Grenadines", "St Vincent & Grenadines"]:
        countryname = "Saint Vincent and the Grenadines"
    if countryname == "Sao Tome & Principe":
        countryname = "Sao Tome and Principe"
    if countryname == "Trinidad & Tobago":
        countryname = "Trinidad and Tobago"
    if countryname == "UAE":
        countryname = "United Arab Emirates"
    if countryname == "Vatican":
        countryname = "Vatican City"
    return countryname

@app.after_request

# The purpose of this function is to make sure caching of responses is disabled. This is the same function that was also used in Finance PSET.
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "nno-cache"
    return response

@app.route("/", methods=["GET", "POST"])

# This function handles displaying the list of all songs on the homepage of the website and renders the file index.html.
def index():
    #user_id = session["user_id"]
    if request.method == "POST":
        method = request.form.get("method")
        if method == "votes":
            rows = db.execute("SELECT * FROM songs ORDER BY votes DESC;")
        elif method == "artist":
            rows = db.execute("SELECT * FROM songs ORDER BY artist ASC;")
        elif method == "id":
            rows = db.execute("SELECT * FROM songs ORDER BY id ASC;")
        elif method == "country":
            rows = db.execute("SELECT * FROM songs ORDER BY country ASC;")
        elif method == "name":
            rows = db.execute("SELECT * FROM songs ORDER BY name ASC;")
        elif method == "year":
            rows = db.execute("SELECT * FROM songs ORDER BY year ASC;")
        elif method == "language":
            rows = db.execute("SELECT * FROM songs ORDER BY language ASC;")
        return render_template("index.html", rows=rows)
    rows = db.execute("SELECT * FROM songs ORDER BY id DESC;")
    return render_template("index.html", rows=rows)

@app.route("/login", methods=["GET", "POST"])

# This function handles logging it to the website.
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")

# This function handles logging out of the website.
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])

# This function handles the registration of new users.
def register():
    """Register user"""
    if request.method == "POST":
        # Make sure user provided username
        if not request.form.get("username"):
            return apology("must provide username", 403)
        elif not request.form.get("email"):
            return apology("must provide email", 403)
        # Make sure user provided password
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        # Make sure user confirmed password
        elif not request.form.get("confirmation"):
            return apology("must provide password confirmation", 403)
        # Make sure password and confirmation match
        elif not request.form.get("password") == request.form.get("confirmation"):
            return apology("password and confirmation do not match", 403)
        # Make sure username hasn't already been taken
        elif db.execute("SELECT * FROM users WHERE username = ?;", request.form.get("username")):
            return apology("Username already taken", 403)
        # Hash the password
        hash = generate_password_hash(request.form.get("password"))
        # Insert user into database
        db.execute("INSERT INTO users (username, email, hash) VALUES (?, ?, ?);", request.form.get("username"), request.form.get("email"), hash)
        # Log in the user and redirect them to the homepage
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]
        time = datetime.now()
        db.execute("INSERT INTO changes (change_type, done_by, affecting_user, time) VALUES (?, ?, ?, ?)", "User registration", rows[0]["id"], rows[0]["id"], time)
        flash("Registered!")
        return redirect("/")
    return render_template("register.html")

@app.route("/nominate", methods=["GET", "POST"])
@login_required

# This function handles the nomination of new songs.
def nominate():
    if request.method == "POST":
        #Code goes here
        if not request.form.get("name"):
            return apology("Missing song name")
        elif not request.form.get("country"):
            return apology("Missing country")
        elif not request.form.get("country") in countries:
            return apology("Invalid country")
        name = request.form.get("name")
        country = adjustcountryname(request.form.get("country"))
        db.execute("INSERT INTO songs (name, country) VALUES (?, ?)", name, country)
        song_id = db.execute("SELECT MAX(id) FROM songs")[0]["MAX(id)"]
        if not request.form.get("artist") == "":
            db.execute("UPDATE songs SET artist = ? WHERE id = ?", request.form.get("artist"), song_id)
        if not request.form.get("year") == "":
            db.execute("UPDATE songs SET year = ? WHERE id = ?", request.form.get("year"), song_id)
        if not request.form.get("language") == "":
            db.execute("UPDATE songs SET language = ? WHERE id = ?", request.form.get("language"), song_id)
        user_id = session["user_id"]
        nominations = db.execute("SELECT nominations FROM users WHERE id = ?", user_id)[0]["nominations"]
        nominations += 1
        db.execute("UPDATE users SET nominations = ? WHERE id = ?", nominations, user_id);
        time = datetime.now()
        db.execute("INSERT INTO changes (change_type, done_by, affecting_song, time) VALUES (?, ?, ?, ?)", "Song nomination", user_id, song_id, time)
        flash ("Song Nominated!")
        return redirect("/")
    return render_template("nominate.html")

@app.route("/vote", methods=["POST"])
@login_required

# This function handles voting for songs.
def vote():
    user_id = int(session["user_id"])
    song_id = int(request.form.get("song_id"))
    upvotes = int(db.execute("SELECT upvotes FROM users WHERE id = ?", user_id)[0]["upvotes"])
    downvotes = int(db.execute("SELECT downvotes FROM users WHERE id = ?", user_id)[0]["downvotes"])
    oldscore = int(request.form.get("score"))
    try:
        oldvotes = int(db.execute("SELECT votes FROM votes WHERE song_id = ? and user_id = ?", song_id, user_id)[0]["votes"])
    except IndexError:
        oldvotes = 0;
    newvote = int(request.form.get("vote"))
    # Updating tables votes, songs and users
    if newvote == 1:
        if oldvotes == -1:
            # Voting FOR song, that has already been voted AGAINST in the past
            print("Case A")
            db.execute("UPDATE votes SET votes = 1 WHERE user_id = ? AND song_id = ?", user_id, song_id)
            db.execute("UPDATE songs SET votes = ? WHERE id = ?", oldscore + 2, song_id)
            db.execute("UPDATE users SET upvotes = ? WHERE id = ?", upvotes + 1, user_id)
            db.execute("UPDATE users SET downvotes = ? WHERE id = ?", downvotes - 1, user_id)
        elif oldvotes == 0:
            print("Case B")
            # Vorting FOR song, the first time
            db.execute("INSERT INTO votes (song_id, user_id, votes) VALUES (?, ?, ?)", song_id, user_id, 1)
            db.execute("UPDATE songs SET votes = ? WHERE id = ?", oldscore + 1, song_id)
            db.execute("UPDATE users SET upvotes = ? WHERE id = ?", upvotes + 1, user_id)
        elif oldvotes == 1:
            print("Case C")
            # Trying to vote FOR song AGAIN
            flash ("You've already cast your vote")
            return redirect(request.referrer)
    elif newvote == -1:
        if oldvotes == -1:
            print("Case D")
            # Trying to vote AGAINST song AGAIN
            flash ("You've already cast your vote")
            return redirect(request.referrer)
        elif oldvotes == 0:
            print("Case E")
            # Voting AGAINST song, the first time
            db.execute("INSERT INTO votes (song_id, user_id, votes) VALUES (?, ?, ?)", song_id, user_id, -1)
            db.execute("UPDATE songs SET votes = ? WHERE id = ?", oldscore - 1, song_id)
            db.execute("UPDATE users SET downvotes = ? WHERE id = ?", downvotes + 1, user_id)
        elif oldvotes == 1:
            print("Case F")
            # Voting AGAINST song, that has previously been voted FOR
            db.execute("UPDATE votes SET votes = -1 WHERE user_id = ? AND song_id = ?", user_id, song_id)
            db.execute("UPDATE songs SET votes = ? WHERE id = ?", oldscore - 2, song_id)
            db.execute("UPDATE users SET upvotes = ? WHERE id = ?", upvotes - 1, user_id)
            db.execute("UPDATE users SET downvotes = ? WHERE id = ?", downvotes + 1, user_id)
    time = datetime.now()
    db.execute("INSERT INTO changes (change_type, done_by, affecting_song, time) VALUES (?, ?, ?, ?)", "Voting for a song", user_id, song_id, time)
    flash ("Thanks for voting!")
    return redirect(request.referrer)

@app.route("/countries", methods=["GET", "POST"])

# This function displays the list of countries from which there are songs in the database.
def states():
    if request.method == "POST":
        method = request.form.get("method")
        if method == "country":
            rows = db.execute("SELECT country, COUNT(*), SUM(votes) FROM songs GROUP BY country ORDER BY country ASC;")
        elif method == "songs":
            rows = db.execute("SELECT country, COUNT(*), SUM(votes) FROM songs GROUP BY country ORDER BY COUNT(*) DESC;")
        elif method == "votes":
            rows = db.execute("SELECT country, COUNT(*), SUM(votes) FROM songs GROUP BY country ORDER BY SUM(votes) DESC;")
        return render_template("countries.html", rows=rows)
    rows = db.execute("SELECT country, COUNT(*), SUM(votes) FROM songs GROUP BY country;")
    return render_template("countries.html", rows=rows)

@app.route("/country", methods=["GET", "POST"])

# This function handles displaying lists of songs from just one country.
def country():
    country = request.args.get("c")
    if request.method == "POST":
        method = request.form.get("method")
        if method == "votes":
            rows = db.execute("SELECT * FROM songs WHERE country = ? ORDER BY votes DESC;", country)
        elif method == "artist":
            rows = db.execute("SELECT * FROM songs WHERE country = ? ORDER BY artist ASC;", country)
        elif method == "id":
            rows = db.execute("SELECT * FROM songs WHERE country = ? ORDER BY id ASC;", country)
        elif method == "country":
            rows = db.execute("SELECT * FROM songs WHERE country = ? ORDER BY country ASC;", country)
        elif method == "name":
            rows = db.execute("SELECT * FROM songs WHERE country = ? ORDER BY name ASC;", country)
        elif method == "year":
            rows = db.execute("SELECT * FROM songs WHERE country = ? ORDER BY year ASC;", country)
        elif method == "language":
            rows = db.execute("SELECT * FROM songs WHERE country = ? ORDER BY language ASC;", country)
        return render_template("country.html", country=country, rows=rows)
    rows = db.execute("SELECT * FROM songs WHERE country = ? ORDER BY id DESC;", country)
    return render_template("country.html", country=country, rows=rows)

@app.route("/users", methods=["GET", "POST"])

# This function deals with displaying the list of users.
def users():
    if request.method == "POST":
        method = request.form.get("method")
        if method == "username":
            rows = db.execute("SELECT * FROM users ORDER BY username ASC;")
        elif method == "country":
            rows = db.execute("SELECT * FROM users ORDER BY country ASC;")
        elif method == "id":
            rows = db.execute("SELECT * FROM users ORDER BY id ASC;")
        elif method == "website":
            rows = db.execute("SELECT * FROM users ORDER BY website ASC;")
        elif method == "upvotes":
            rows = db.execute("SELECT * FROM users ORDER BY upvotes DESC;")
        elif method == "downvotes":
            rows = db.execute("SELECT * FROM users ORDER BY downvotes DESC;")
        elif method == "nominations":
            rows = db.execute("SELECT * FROM users ORDER BY nominations DESC;")
        elif method == "comments":
            rows = db.execute("SELECT * FROM users ORDER BY comments DESC;")
        elif method == "profilecomments":
            rows = db.execute("SELECT * FROM users ORDER BY profilecomments DESC;")
        return render_template("users.html", rows=rows)
    rows = db.execute("SELECT * FROM users")
    return render_template("users.html", rows=rows)

@app.route("/profile")
@login_required
# This function deals with displaying user profiles.
def profile():
    username = request.args.get("u")
    user_id = int(session["user_id"])
    isadmin = db.execute("SELECT isadmin FROM users WHERE id = ?", user_id)[0]["isadmin"]
    loggedin = session["username"]
    rows = db.execute("SELECT * FROM users WHERE username LIKE ?;", username)
    id = rows[0]["id"]
    comments = db.execute("SELECT time, username, comment, users.id AS commenterid, profilecomments.id AS commentid FROM profilecomments JOIN users ON profilecomments.user_id = users.id WHERE profile_id = ? ORDER BY time DESC", id)
    return render_template("profile.html", user=username, rows=rows, loggedin=loggedin, id=id, comments=comments, isadmin=isadmin, user_id=user_id)

@app.route("/myprofile")
@login_required
# This function deals with displaying the profile of the person who is currently logged in.
def myprofile():
    username = session["username"]
    user_id = int(session["user_id"])
    isadmin = db.execute("SELECT isadmin FROM users WHERE id = ?", user_id)[0]["isadmin"]
    rows = db.execute("SELECT * FROM users WHERE username LIKE ?;", username)
    id = rows[0]["id"]
    comments = db.execute("SELECT time, username, comment, users.id AS commenterid, profilecomments.id AS commentid FROM profilecomments JOIN users ON profilecomments.user_id = users.id WHERE profile_id = ? ORDER BY time DESC", id)
    return render_template("profile.html", user=username, rows=rows, id=id, comments=comments, isadmin=isadmin, user_id=user_id)

@app.route("/editprofile", methods=["GET", "POST"])
@login_required

# This function allows users to edit their profiles.
def editprofile():
    username = session["username"]
    user_id = session["user_id"]
    if request.method == "POST":
        if not request.form.get("country") == "":
            db.execute("UPDATE users SET country = ? WHERE username = ?;", request.form.get("country"), username)
        if not request.form.get("aboutme") == "":
            db.execute("UPDATE users SET about_me = ? WHERE username = ?;", request.form.get("aboutme"), username)
        if not request.form.get("favoritemusic") == "":
            db.execute("UPDATE users SET favorite_music = ? WHERE username = ?;", request.form.get("favoritemusic"), username)
        if not request.form.get("website") == "":
            db.execute("UPDATE users SET website = ? WHERE username = ?;", request.form.get("website"), username)
        time = datetime.now()
        db.execute("INSERT INTO changes (change_type, done_by, affecting_user, time) VALUES (?, ?, ?, ?)", "Editing user profile", user_id, user_id, time)
        flash("Profile updated!")
        return redirect("/myprofile")
    rows = db.execute("SELECT * FROM users WHERE username LIKE ?;", username)
    return render_template("editprofile.html", rows=rows)

@app.route("/song")
@login_required

# This function handles displaying pages about individual songs.
def song():
    user_id = int(session["user_id"])
    isadmin = db.execute("SELECT isadmin FROM users WHERE id = ?", user_id)[0]["isadmin"]
    songid = request.args.get("id")
    name = db.execute("SELECT name FROM songs WHERE id = ?;", songid)[0]["name"]
    rows = db.execute("SELECT * FROM songs WHERE id = ?;", songid)
    comments = db.execute("SELECT users.id AS commenterid, time, username, comment, comments.id AS commentid FROM comments JOIN users ON comments.user_id = users.id WHERE song_id = ? ORDER BY time DESC", songid)
    return render_template("song.html", user_id=user_id, name=name, rows=rows, id=songid, comments=comments, isadmin=isadmin)

@app.route("/deletesongcomment", methods=["POST"])
@login_required

# This function handles deleting comments users left on songs.
def deletesongcomment():
    performer = int(session["user_id"])
    comment_id = request.form.get("comment_id")
    user_id = db.execute("SELECT user_id FROM comments WHERE id = ?", comment_id)[0]["user_id"]
    song_id = db.execute("SELECT song_id FROM comments WHERE id = ?", comment_id)[0]["song_id"]
    comments = db.execute("SELECT comments FROM users WHERE id = ?", user_id)[0]["comments"]
    comments -= 1
    db.execute("DELETE FROM comments WHERE id = ?", comment_id)
    db.execute("UPDATE users SET comments = ? WHERE id = ?", comments, user_id)
    time = datetime.now()
    db.execute("INSERT INTO changes (change_type, done_by, affecting_song, time) VALUES (?, ?, ?, ?)", "Deleting song comment", performer, song_id, time)
    flash("Comment deleted")
    return redirect(request.referrer)

@app.route("/deleteprofilecomment", methods=["POST"])
@login_required

# This function handles deleting comments users left on profiles of other users (or on their own profile).
def deleteprofilecomment():
    performer = int(session["user_id"])
    comment_id = request.form.get("comment_id")
    user_id = db.execute("SELECT user_id FROM profilecomments WHERE id = ?", comment_id)[0]["user_id"]
    profile_id = db.execute("SELECT profile_id FROM profilecomments WHERE id = ?", comment_id)[0]["profile_id"]
    comments = db.execute("SELECT profilecomments FROM users WHERE id = ?", user_id)[0]["profilecomments"]
    comments -= 1
    db.execute("DELETE FROM profilecomments WHERE id = ?", comment_id)
    db.execute("UPDATE users SET profilecomments = ? WHERE id = ?", comments, user_id)
    time = datetime.now()
    db.execute("INSERT INTO changes (change_type, done_by, affecting_user, time) VALUES (?, ?, ?, ?)", "Deleting profile comment", performer, profile_id, time)
    flash("Profile comment deleted!")
    return redirect(request.referrer)

@app.route("/lock", methods=["POST"])
@login_required

# This function allows the admin to lock editing of the song
def lock():
    performer = int(session["user_id"])
    song_id = request.form.get("song_id")
    islocked = db.execute("SELECT islocked FROM songs WHERE id = ?", song_id)[0]["islocked"]
    if islocked == 1:
        flash("Song was already locked!")
        return redirect(request.referrer)
    else:
        db.execute("UPDATE songs SET islocked = 1 WHERE id = ?", song_id)
        time = datetime.now()
        db.execute("INSERT INTO changes (change_type, done_by, affecting_song, time) VALUES (?, ?, ?, ?)", "Locking song editing", performer, song_id, time)
        flash("Editing locked!")
        return redirect(request.referrer)

@app.route("/unlock", methods=["POST"])
@login_required

# This function allows the admin to unlock editing of songs.
def unlock():
    performer = int(session["user_id"])
    song_id = request.form.get("song_id")
    islocked = db.execute("SELECT islocked FROM songs WHERE id = ?", song_id)[0]["islocked"]
    if islocked == 0:
        flash("Song was already unlocked!")
        return redirect(request.referrer)
    else:
        db.execute("UPDATE songs SET islocked = 0 WHERE id = ?", song_id)
        time = datetime.now()
        db.execute("INSERT INTO changes (change_type, done_by, affecting_song, time) VALUES (?, ?, ?, ?)", "Unlocking song editing", performer, song_id, time)
        flash("Editing unlocked!")
        return redirect(request.referrer)

@app.route("/editsong")
@login_required

# This function deals with rendering the form in the editsong.html, which users can use to edit information about the song.
def editsong():
    id = request.args.get("id")
    islocked = db.execute("SELECT islocked FROM songs WHERE id = ?;", id)[0]["islocked"]
    if islocked == 1:
        flash("Editing locked!")
        return redirect(request.referrer)
    rows = db.execute("SELECT * FROM songs WHERE id = ?;", id)
    return render_template("editsong.html", rows=rows)

@app.route("/edit", methods=["POST"])
@login_required

# This function updates the database when the user submits the form on editsong.html.
def edit():
    performer = int(session["user_id"])
    id = request.form.get("id")
    if not request.form.get("name") == "":
        db.execute("UPDATE songs SET name = ? WHERE id = ?;", request.form.get("name"), id)
    if not request.form.get("country") == "":
        db.execute("UPDATE songs SET country = ? WHERE id = ?;", adjustcountryname(request.form.get("country")), id)
    if not request.form.get("artist") == "":
        db.execute("UPDATE songs SET artist = ? WHERE id = ?;", request.form.get("artist"), id)
    if not request.form.get("language") == "":
        db.execute("UPDATE songs SET language = ? WHERE id = ?;", request.form.get("language"), id)
    if not request.form.get("year") == "":
        db.execute("UPDATE songs SET year = ? WHERE id = ?;", request.form.get("year"), id)
    time = datetime.now()
    db.execute("INSERT INTO changes (change_type, done_by, affecting_song, time) VALUES (?, ?, ?, ?)", "Editing song", performer, id, time)
    flash("Song updated!")
    return redirect("/song?id="+id)

@app.route("/comment", methods=["POST"])
@login_required

# This function handles commenting on songs
def comment():
    time = datetime.now()
    comment = request.form.get("comment")
    songid = request.form.get("song_id")
    userid = session["user_id"]
    db.execute("INSERT INTO comments (song_id, user_id, comment, time) VALUES (?,?,?,?);", songid, userid, comment, time)
    comments = db.execute("SELECT comments FROM users WHERE id = ?;", userid)[0]["comments"]
    db.execute("UPDATE users SET comments = ? WHERE id = ?;", comments + 1, userid)
    db.execute("INSERT INTO changes (change_type, done_by, affecting_song, time) VALUES (?, ?, ?, ?)", "Commenting a song", userid, songid, time)
    flash("Comment added!")
    return redirect("/song?id="+songid)

@app.route("/profilecomment", methods=["POST"])
@login_required

# This function handles commenting on user profiles.
def profilecomment():
    time = datetime.now()
    comment = request.form.get("comment")
    profileid = request.form.get("user_id")
    userid = session["user_id"]
    db.execute("INSERT INTO profilecomments (profile_id, user_id, comment, time) VALUES (?,?,?,?);", profileid, userid, comment, time)
    profilecomments = db.execute("SELECT profilecomments FROM users WHERE id = ?;", userid)[0]["profilecomments"]
    db.execute("UPDATE users SET profilecomments = ? WHERE id = ?;", profilecomments + 1, userid)
    db.execute("INSERT INTO changes (change_type, done_by, affecting_user, time) VALUES (?, ?, ?, ?)", "Commenting a profile", userid, profileid, time)
    flash("Profile comment added!")
    return redirect(request.referrer)

@app.route("/search")

# This function returns the search results, when users search for songs.
def search():
    song = request.args.get("song")
    artist = request.args.get("artist")
    if song:
        songs = db.execute("SELECT * FROM songs WHERE name LIKE ? LIMIT 50", "%" + song + "%")
    elif artist:
        songs = db.execute("SELECT * FROM songs WHERE artist LIKE ? LIMIT 50", "%" + artist + "%")
    else:
        songs = []
    return render_template("results.html", songs=songs)

@app.route("/searching")

# This function simply renders the page search.html which contains the form for searching the songs, and in which the search results will also be displayed as a result of asynchronous JavaScript function.
def searching():
    return render_template("search.html")

@app.route("/changes")

# This function handles displaying the list of most recent changes to the database of the website. It renders the file changes.html.
def changes():
    rows = db.execute("SELECT changes.id AS changeid, username, affecting_user, affecting_song, change_type, time FROM users JOIN changes ON users.id = changes.done_by ORDER BY time DESC LIMIT 50")
    for row in rows:
        if row["affecting_user"]:
            row["affecting_username"] = db.execute("SELECT username FROM users WHERE id = ?", row["affecting_user"])[0]["username"]
        if row["affecting_song"]:
            row["affecting_songname"] = db.execute("SELECT name FROM songs WHERE id = ?", row["affecting_song"])[0]["name"]
    return render_template("changes.html", rows=rows)
