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

    def loadUser(self, data):
        if data['status'] != 'ok':
            return self.STATUS_FAILED
        try:
            user = data['logged_in_user']
            self.username = user['username']
            self.profile_picture = user['profile_pic_url']
            self.fullname = user['full_name']
            self.fbuid = user['fbuid']
            self.private = user['is_private']
            self.logged_in = True
            return self.STATUS_OK
        except KeyError:
            print data
            return self.STATUS_FAILED

    def login(self):
        """
        Logs in and verifies the users supplied credentials when creating
                an instance of Insta.
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

        req = json.loads(
            self.post("accounts/login/", {
                "signed_body": self.signMessage(data) + "." + data,
                "ig_sig_key_version": 6
            }).text
        )

        if self.loadUser(req) == Insta.STATUS_FAILED:
            print "Failed to login...\nStatus: %s\nMessage: %s" % (
                req['status'], req['message']
            )
            return self.STATUS_FAILED
        else:
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
