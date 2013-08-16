import web
import requests
import httplib, base64
urls = (
    '/(.*)', 'index'
)

render = web.template.render('templates/')

class index:
    def GET(self, user_id):
        pass

class twitter:
    def __init__(self):
        self.bearer = self.__get_bearer()
    #@staticmethod
    def __get_bearer(self):

        encode_string = "{!s}:{!s}".format("2nTaA2Uny9mZIOWrtNnO9Q","dqzpWUxiFjfNvrI2hNSNlKnPMSG8cMVU0e2yw9SDAM")
        encoded_string = base64.b64encode(encode_string)
        headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Authorization": "Basic {!s}".format(encoded_string)}
        body = "grant_type=client_credentials"

        r = requests.post("https://api.twitter.com/oauth2/token", data=body, headers=headers,verify=False)
        return r.json()['access_token']

    def get_friends(self, screen_name):
        """
        Returns: A list of ids that are this person's friends
        include an Authorization header with the value of Bearer <base64 bearer token value from step 2>
        """
        headers = {"Authorization": "Bearer {!s}".format(self.bearer)}
        parameters = {"screen_name": screen_name}
        r = requests.get("https://api.twitter.com/1.1/friends/ids.json", params=parameters,headers=headers,verify=False)
        if r.status_code != requests.codes.ok:
            raise 'Error in API call. Twitter returned:' + r.text
        return r.json()['ids']

if __name__ == "__main__":
    #app = web.application(urls, globals())
    #app.run()
    twit = twitter()
    print twit.get_friends('himerzi')
