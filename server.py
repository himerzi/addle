import web
import requests

urls = (
	'/(.*)', 'index'
)

render = web.template.render('templates/')

class index:
	def GET(self, user_id):
		return user_id

		user_id = 'bob'

		#list users followeds from api
		followeds = ['mdetmold','tomchambers','joeroot','dclough','jordnb']
		followeds_r = {
			'mdetmold',['tomchambers','joeroot','johnnynobody','foghorn'],
			'tomchambers',['mdetmold','joeroot','jordnb'],
			'joeroot',['outofnetwork','beastboy','tomchambers','mdetmold','jordnb']
		}

		for a in followeds:
			#list each followed's followeds from the api
			followeds = followeds_r[a]
			for b in followeds_r:
				#perform check to see how many connections they have with the first level
				#assign them a ranking

		#weak_link = follower with lowest value

		return weak_link

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()