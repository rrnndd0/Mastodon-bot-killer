from mastodon import Mastodon

#Client key
key = ""

#Client Secret
secret = ""

#Access Token
token = ""

#Instance
instance = 'https://mastodon.social'


############################


lstBots = []

mastodon = Mastodon(key,secret,token, api_base_url = instance)

tl = mastodon.timeline_local(max_id=None, since_id=None, limit=40)
for loop in range (0,5):
	if len(tl) > 0:
		for x in range (0,len(tl)):
			if tl[x].account.bot == True and lstBots.count(tl[x].account.username) == 0:
				lstBots.append(tl[x].account.username)
				mastodon.account_block(tl[x].account.id)
	tl = mastodon.fetch_next(tl[len(tl) - 1]._pagination_next)
				
print ("From the last 200 toots I've blocked " + str(len(lstBots)) + " bots!")
			

	