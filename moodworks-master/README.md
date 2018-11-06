# Moodworks :: The repository for the IBM Hack Challenge :coffee:
# Authors: Sebin Sabu and Nora Elizabeth Joby (Team K15)
Created: 05 September 2018
Last updated: 07 October 2018

# Solution Manual:

1. What is Moodworks?

Moodworks is a system that tracks your mood according to your tweet data and feedback response and dynamically helps you deal with it by providing multiple options to help recover from negative emotions, or celebrate the positive emotions!

2. How to use MoodWorks?

MoodWorks is hosted at BlueMix Service of IBM so that its accessible from anywhere on internet.

For tuning moodworks on your profile input your Name and twitter Id in the url like this.:
http://getstartedpython-impressive-bear.eu-gb.mybluemix.net/hello/your_twitter_Id/your_name>

Example:: http://getstartedpython-impressive-bear.eu-gb.mybluemix.net/hello/ndtv/Akhil

If you do not have a Twitter ID, add "nil" as twitter id in the url.like this:

Example:: http://getstartedpython-impressive-bear.eu-gb.mybluemix.net/hello/nil/Sebin

MoodWorks will greet you according to the time of the day and prompt you with a question about your day. Reply to it with whatever you feel, even with an emoticon. Once you press "Send", it will come back to you with a curated response by understanding about your emotional state from twitter account and your response.

MoodWorks can also be installed and used on localhost by running python hello.py in terminal.

3. How MoodWorks Works?

MoodWorks use Twitter API and IBM NLP API for the computation. It works on Flask Micro Web Framework of Python.

MoodWorks fetches last five tweets of the user and user response about his feelings, both are scrubbed using data-filtration algorithm for improved sentimental analysis. IBM NLP services is used to process the tweets and user response to create a sentiment matrix of the user. A default weightage of 1:1 is assigned for sentiment matrix derived from tweets and user response (This is for the ease of demo of different moods).
The weightage and number of tweets fetched can be optimised according to performance and user behavioral trend.

4. How MoodWorks can help?

MoodWorks can be used as a friendly tool for keeping a track of people's sentiment and also allowing them to get a more diverse and customised  experience. Continuous monitoring of an user using MoodWorks can be used for identifying traits of depression in user behaviours. Growing self awareness of negative sentiments in one person is the best method to help him on avoiding them.
Tracking of users and associated functionalities is currently removed, since MoodWorks is now released for Public Access.

5. What is special about Moodworks?
Our Unique Value points (Key Value Propositions) are:
* Input from Social Media as well as direct response from the user, and combining both information
* Data scrubbing algorithm to process and deal with both the above inputs
* Dynamically responding user interface according to time of the day, your mood etc.
* Randomised response system gives you a new list of suggestions each time
* A list of choices to choose from , for each mood detected
* Ready to deploy (User can deploy anytime he/she wants to)
* Easy to use and simple User Interface
* Robustness to work even without twitter ID/account


# Documentation

The idea:

https://docs.google.com/document/d/1uWrIDC5otDsZ_2aolNyIwRJXxM5byvcslAFCT--KhHs/edit?usp=sharing

Powerpoint presentation:

https://docs.google.com/presentation/d/1KlYtX9OWuvmy0UiCsRMvjP-Bvvc5eISQLGUox4tN_BE/edit?usp=sharing

Video link:

https://drive.google.com/open?id=1ler-1Q-8YoxdEqXTxvYMqnM1vlUbBwbd

Code:

https://github.com/norajoby/moodworks/tree/master/get-started-python
