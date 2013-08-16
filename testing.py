user_id = 'bob'

def check_connections(user, first_level):
	upper_user = user.upper()
	print "NOW CHECKING "+upper_user

	connections = 0
	for a in first_level_follows:
		#print "another loop"
		connection = first_level_follows[a]
		#print connection

		#print connection
		for b in connection:
			#print b
			if user == b:
				connections = connections + 1
				print user+" is followed by "+a+". They now have "+str(connections)+" connections"

	return connections

#list users followeds from api
first_level = ['mdetmold','tomchambers','joeroot','dclough','jordnb']
first_level_follows = {
	'mdetmold': ['tomchambers','joeroot','johnnynobody','foghorn'],
	'tomchambers': ['mdetmold','joeroot','jordnb'],
	'joeroot': ['outofnetwork','beastboy','tomchambers','mdetmold','jordnb'],
	'dclough': ['economics','businessguy','jordnb','mdetmold'],
	'jordnb': ['mdetmold','tomchambers']
}

for a in first_level:
	#list each followed's followeds from the api
	connection = first_level_follows[a]

	for b in connection:
		print check_connections(b, first_level)

		#(user, first_level)
		#perform check to see how many connections they have with the first level
		#assign them a ranking
		#print b

#weak_link = follower with lowest value

#return weak_link