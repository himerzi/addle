from server import twitter

screen_name = 'tomchambers3'
t = twitter()

links = {}

def check_connections(user, user_friends):
	print "NOW CHECKING "+str(user)

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
				print str(user)+" is followed by "+str(a)+". They now have "+str(connections)+" connections"

	links[user] = connections			
	return connections

#list users followeds from api
#user_friends = ['mdetmold','tomchambers','joeroot','dclough','jordnb']

user_friends = t.get_friends(screen_name)

friends_friends = {}

for i,a in enumerate(user_friends):
	if i > 1:
		break
	friends_friends[a] = t.get_friends(user_id=a)
	print "API calls: "+str(i)

	connection = friends_friends[a]

	for b in connection:
		check_connections(b, user_friends)

links = sorted(links.items())

print links

sorted_list = sorted(data, key=lambda tup: tup[1])
print sorted_list[0][0]
