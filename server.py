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
    def get_screen_name(self, user_id):
        headers = {"Authorization": "Bearer {!s}".format(self.bearer)}
        parameters = {"user_id": user_id, "include_entities": False}
        r = requests.get("https://api.twitter.com/1.1/users/show.json", params=parameters,headers=headers,verify=False)
        if r.status_code != requests.codes.ok:
            raise Exception('Error in API call. Twitter returned:' + r.text)
        return str(r.json()['screen_name'])
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

    def __get__factory(self, url, parameters):

        def f():
            headers = {"Authorization": "Bearer {!s}".format(self.bearer)}
            r = requests.get(url, params=parameters,headers=headers,verify=False)
            if r.status_code != requests.codes.ok:
                raise Exception('Error in API call. Twitter returned:' + r.text)
            return r.json()

if __name__ == "__main__":
    #app = web.application(urls, globals())
    #app.run()
    #twit = twitter()
    #print twit.get_screen_name('12')
