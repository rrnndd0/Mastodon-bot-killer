# Mastodon-bot-killer

Requires mastodon.py (https://github.com/halcy/Mastodon.py) installed in order to function

Once installed you will need to navigate to Mastodon's preferences -> Development -> New Application.
You can name your application anything you like but it's important to grant the permissions 'read', 'write' and 'write:blocks'.
Once your application is created, copy the client key, client secret and access token and add it to the botkiller.py file. Be sure to enter your own instance URL too.

To run, just type:

python botkiller.py

OR

python3 botkiller.py

Remember to double check your block lists after running this operation! 
