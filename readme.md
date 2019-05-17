# Keyword Reddit

Get the reddit post sent to your email based on the keywords you want for each subreddit.

## Getting Started

Below is the instructions you need to get the program running.

### Prerequisites

Make sure you have python3 and pip installed. 
You will also need to have a reddit account in order to use PRAW and a gmail account in order to send email to yourself.

### Installing

Would highly recommend using virtual environment to run this program to guarantee the right version for each package. In my case, I was using python's standard library [venv](https://docs.python.org/3/library/venv.html).

After you clone the project, cd into the project directory.

Create a virtual environment in kw_reddit directory.
```
$ python -m venv virtuaEnvNameYouWant
```

To activate the virtual environment in kw_reddit directory.
```
$ venvnameyouwant\Scripts\activate.bat
```
When you see (virtuaEnvNameYouWant) show up to the left of each command line, you know you are in the virtual environment now.

Then you can install the packages specified in the requirements.txt file

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

## Running the program
Edit the subreddits.txt to specify the keywords you want to see in the title or selfpost.

Formatted as below.

subreddit1,kw1,kw2

subreddit2,kw1,kw2

Ex:

```

```


https://www.reddit.com/prefs/apps

https://myaccount.google.com/security

