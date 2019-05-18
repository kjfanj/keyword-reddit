# Keyword Reddit

Get the reddit post sent to your email based on the keywords you want for each subreddit.

## Getting Started

### Prerequisites

Make sure you have python3 and pip installed. 
You will also need to have a reddit account in order to use PRAW and a gmail account in order to send email to yourself.

### Installing

Would highly recommend using virtual environment to run this program to guarantee the right version for each package. In my case, I was using python's standard library [venv](https://docs.python.org/3/library/venv.html).

After you clone the project, cd into the project directory.

Create a virtual environment in directory.
```
$ python -m venv virtualEnvNameYouWant
```

To activate the virtual environment in directory.
```
$ venvnameyouwant\Scripts\activate.bat
```
When you see (virtualEnvNameYouWant) show up to the left of each command line, you know you are in the virtual environment now.

Then you can install the packages specified in the requirements.txt file into the virtual environment.

```
$ pip install -r requirements.txt 
```

### Authentications

You will need a reddit account for PRAW and a gmail account for sending emails to yourself for this program.

create a .env file in the kw_reddit directory.

copy the .env.sample to the .env file and fill out the required informations.

```
CLIENT_ID=XXXXX-XXXXXXXX (You need to register for an app after signing in on reddit)
CLIENT_SECRET=XXXXXXXXXXXXXXXXXX-XX (You need to register for an app after signing in on reddit)
USER_AGENT=PRAW recommended format: <platform>:<app ID>:<version string> (by /u/<Reddit username>), ex: android:com.example.myredditapp:v1.2.3 (by /u/kemitche)
MY_GMAIL=XXXXXXXXX@gmail.com (the gmail account you used to create the APP_PW)
APP_PW=XXXXXXXXXXXXXXXX (You get this from Google's App passwords after turning on 2-step verification)
```

You can go to the reddit developer console [here](https://www.reddit.com/prefs/apps) after logging in to create an app.

For sending email you will need to go to the [security tab](https://myaccount.google.com/security) in your account setting after logging in, and you will first allow 2-step verification, then create an app password, which is what you will put in the .env file.

More specifics in the images folder.

## Running the program
Edit the subreddits.txt to specify the keywords you want to see in the title or selfpost.

Formatted as below.

subreddit1,kw1,kw2

subreddit2,kw1,kw2

Ex: subreddits.txt

```
space,nasa,telescope
pics,moment
doesnotexistthissubreddit,keyword1
askreddit,fun,funny
```

then run

```
$ python scheduler.py
```

### Demo

![example](/images/example.png)

and also send the post to your gmail

![result](/images/result.png)


The default is making a call every 5 seconds, but you can try to tweak it in scheduler.py based on schedule library.

