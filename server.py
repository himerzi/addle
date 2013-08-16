import web
import requests
import httplib, base64
urls = (
    '/',  'index',
    '/(.*)', 'found'
)

render = web.template.render('templates/')

class index:
    def GET(self):
        render.index()

class found:
    def GET(self, screen_name):
        g = get_user()
        found_user = g.found_user()
        render.index(found_user)

class get_user:
    t = twitter()

    links = {}

    def check_connections(user, user_friends):
        connections = 0
        for a in friends_friends:
            connection = friends_friends[a]

            for b in connection:
                if user == b:
                    connections = connections + 1
        links[user] = connections           
        return connections

    def found_user():
        user_friends = t.get_friends(screen_name)

        friends_friends = {}

        for i,a in enumerate(user_friends):
            #take this out
            if i > 1:
                break

            connection = friends_friends[a]

            for b in connection:
                check_connections(b, user_friends)

        links = sorted(links.items())

        sorted_list = sorted(data, key=lambda tup: tup[1])
        found_id = sorted_list[0][0]
        return t.get_screen_name(found_id)

class twitter:
    def __init__(self):
        self.bearer = self.__get_bearer()
        print 'great! our bearer token is', self.bearer
    #@staticmethod
    def __get_bearer(self):

        encode_string = "{!s}:{!s}".format("2nTaA2Uny9mZIOWrtNnO9Q","dqzpWUxiFjfNvrI2hNSNlKnPMSG8cMVU0e2yw9SDAM")
        encoded_string = base64.b64encode(encode_string)
        headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Authorization": "Basic {!s}".format(encoded_string)}
        body = "grant_type=client_credentials"

        r = requests.post("https://api.twitter.com/oauth2/token", data=body, headers=headers,verify=False)
        return r.json()['access_token']

    def get_friends(self, screen_name='', user_id=None):
        """
        Returns: A list of ids that are this person's friends
        include an Authorization header with the value of Bearer <base64 bearer token value from step 2>
        """
        headers = {"Authorization": "Bearer {!s}".format(self.bearer)}
        parameters = {"screen_name": screen_name} if not user_id else {"user_id": user_id}
        r = requests.get("https://api.twitter.com/1.1/friends/ids.json", params=parameters,headers=headers,verify=False)
        if r.status_code != requests.codes.ok:
            raise Exception('Error in API call. Twitter returned:' + r.text)
        return r.json()['ids']

    def get_friends_rate_limit(self):
        """
        Returns: A string representing your rate limits
        """

        headers = {"Authorization": "Bearer {!s}".format(self.bearer)}
        parameters = {"resources": "friends"}
        r = requests.get("https://api.twitter.com/1.1/application/rate_limit_status.json", params=parameters,headers=headers,verify=False)
        if r.status_code != requests.codes.ok:
            raise Exception('Error in API call. Twitter returned:' + r.text)
        return str(r.json()['resources'])

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
    #twit = twitter()
    #print twit.get_friends_rate_limit()
