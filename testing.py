from server import twitter

screen_name = 'melior_cj'
t = twitter()

links = {}

def check_connections(user, user_friends):
	upper_user = user.upper()
	print "NOW CHECKING "+upper_user

	connections = 0
	for a in friends_friends:
		#print "another loop"
		connection = friends_friends[a]
		#print connection

		#print connection
		for b in connection:
			#print b
			if user == b:
				connections = connections + 1
				#print user+" is followed by "+a+". They now have "+str(connections)+" connections"

	links[user] = connections			
	return connections

#list users followeds from api
#user_friends = ['mdetmold','tomchambers','joeroot','dclough','jordnb']

user_friends = t.get_friends(screen_name)

"""friends_friends = {
	'mdetmold': ['tomchambers','joeroot','johnnynobody','foghorn'],
	'tomchambers': ['mdetmold','joeroot','jordnb'],
	'joeroot': ['outofnetwork','beastboy','tomchambers','mdetmold','jordnb'],
	'dclough': ['economics','businessguy','jordnb','mdetmold'],
	'jordnb': ['mdetmold','tomchambers']
}"""

friends_friends = {}

for a in user_friends:
	friends_friends[a] = t.get_friends(a)

	connection = friends_friends[a]

	for b in connection:
		check_connections(b, user_friends)

links = sorted(links.items())

print links
