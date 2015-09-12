import requests
import hmac
import json
import hashlib
import uuid

STATUS_FAILED = -1
STATUS_OK = 0

class Insta(object):
		
	def __init__(self,user,pw):
		self.user = user
		self.pw = pw
		self.genGuid()
		self.genDeviceId()
		
	def genDeviceId(self):
		self.device_id = "android-%s" % self.guid.replace("-","")[0:16]
		pass
		
	def genGuid(self):
		self.guid = str(uuid.uuid1())
		pass
	
	def getUserAgent(self):
		return "Instagram 6.21.2 Android (19/4.4.2; 480dpi; 1152x1920; Meizu; MX4; mx4; mt6595; en_US)"
	
	def loadUser(self,data):
		if data['status'] != 'ok':
			return STATUS_FAILED
		try:
			user = data['logged_in_user']
			self.username = user['username']
			self.profile_picture = user['profile_pic_url']
			self.fullname = user['full_name']
			self.fbuid = user['fbuid']
			self.private = user['is_private']
			return STATUS_OK
		except KeyError:
			print data
			return STATUS_FAILED
		
	
	def login(self):
		data = {
			"device_id":self.device_id,
			"guid":self.guid,
			"username":self.user,
			"password":self.pw,
			"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
		}
		data = json.dumps(data)
		signedData = self.signMessage(data) + "." + data
		
		req = json.loads(self.post("accounts/login/", {
			"signed_body":signedData,
			"ig_sig_key_version":6
		}).text)
		
		if self.loadUser(req) == STATUS_FAILED:
			print "Failed to login...\nStatus: %s\nMessage: %s" % (req['status'], req['message'])
			return STATUS_FAILED	
		else:
			return STATUS_OK
		
		
	def post(self,url,contents):
		headers = {
			"user-agent":self.getUserAgent()
		}
		
		req = requests.post("https://instagram.com/api/v1/" + url,data=contents,headers=headers)
		return req
		
	def signMessage(self,data):
		return hmac.new("25eace5393646842f0d0c3fb2ac7d3cfa15c052436ee86b5406a8433f54d24a5", data, hashlib.sha256).hexdigest()