import requests
import hmac
import json
import hashlib
import uuid


class Insta(object):

    STATUS_FAILED = -1
    STATUS_OK = 0

    def __init__(self, user, pw):
        self.user = user
        self.pw = pw
        self.genGuid()
        self.genDeviceId()
        self.logged_in = False
        self.user_info = []
        self.session = requests.Session()

    def genDeviceId(self):
        self.device_id = "android-%s" % self.guid.replace("-", "")[0:16]
        pass

    def genGuid(self):
        self.guid = str(uuid.uuid1())
        pass

    def get(self, url):
        """
        Issues a GET request to a specified endpoint within the Instagram
                private API.

        Arguments:
                url: path of endpoint, domain name removed (already prepended)

        Returns a requests.request object.
        """
        if self.logged_in:
            headers = {
                "user-agent": self.getUserAgent()
            }
            return self.session.get(
                "https://instagram.com/api/v1/" + url,
                headers=headers
            )
        else:
            print "You must be logged in before issuing requests"
            return -1

    def getUserAgent(self):
        return "Instagram 6.21.2 Android (19/4.4.2; 480dpi; \
        1152x1920; Meizu; MX4; mx4; mt6595; en_US)"
        
    def getInfo(self,key):
        """
        Returns the key associated with the user's information
        
        "username" - Username of the user
        "profile_pic_url" - URL of user's profile profile_picture
        "full_name" - Full name of the user
        "fbuid" - Facebook ID of user
        "is_private" - 'true' if user's profile is private, 
            'false' if public
        """
        try:
            return self.user_info[key]
        except KeyError:
            return "null"

    def login(self):
        """
        Logs in and verifies the users supplied credentials when creating
                an instance of Insta.
                
        If login is successful, we will setup a dictionary that
        contain the following keys:
            
        "username" - Username of the user
        "profile_pic_url" - URL of user's profile profile_picture
        "full_name" - Full name of the user
        "fbuid" - Facebook ID of user
        "is_private" - 'true' if user's profile is private, 
            'false' if public
            
        *Additional keys may be contained, but these are the few that are guaranteed
        to exist within the dictionary
        """
        data = json.dumps(
            {
                "device_id": self.device_id,
                "guid": self.guid,
                "username": self.user,
                "password": self.pw,
                "Content-Type": "application/x-www-form-urlencoded;"
                "charset=UTF-8"
            }
        )
        
        responseJson = json.loads(
            self.post("accounts/login/", {
                "signed_body": self.signMessage(data) + "." + data,
                "ig_sig_key_version": 6
            }).text
        )

        if responseJson['status'] != 'ok':
            print "Failed to login...\nStatus: %s\nMessage: %s" % (
                responseJson['status'], responseJson['message']
            )
            return self.STATUS_FAILED
        else:
            self.user_info = responseJson['logged_in_user']
            return self.STATUS_OK

    def post(self, url, contents):
        """
        Issues a POST request to the specified endpoint
                within the Instagram private API.

        Arguments:
                url: path of the specified endpoint, without
                                         domain name (it is already prepended)
                contents: a dictionary containing the POST data

        Returns a requests.request object.
        """
        headers = {
            "user-agent": self.getUserAgent()
        }
        return self.session.post("https://instagram.com/api/v1/" + url,
                                 data=contents,
                                 headers=headers
                                 )

    def signMessage(self, data):
        return hmac.new(
            "25eace5393646842f0d0c3fb2ac7d3cfa15c052436ee86b5406a8433f54d24a5",
            data,
            hashlib.sha256).hexdigest()
