# Followers

A simple tool to do some simple and basic analyses on followers for twitter users.

Written in python3 (used version 3.10.6), language is Dutch

(I can translate easily in English upon request.)

All credits for analyse.py script go to @r0zetta, I originally found this on:
https://blog.f-secure.com/how-to-get-twitter-follower-data-using-python-and-tweepy/

Install dependencies by:

`pip install -r requirements.txt`

You will need twitter api auth. See: https://medium.com/analytics-vidhya/accessing-the-twitter-api-with-tweepy-8421329afc5c

Create a file in the same dir where these python files reside,  name it .login and paste your credentials in below order
* api key
* api secret
* acces token
* acces secret

Execute:

`python followers.py`

and fill desired fields upon asking.

The analyse.py script will fetch latest 5000 followers with help of the twitter api, and store this in a json file. It will also show the age of these followers accounts in 10 two weeks bins. Alternatively the script will use the stored data, this is optional.

The check.py script will do a quick scan on these accounts, it will check if the user is following users themselves, and if they ever tweeted or not.

(If the python command is not working on Ubuntu distro's,  alternatively, use python3 command instead of python)
