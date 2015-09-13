from Insta import Insta

def main():
	insta = Insta("username", "password")
	if insta.login() == 0:
		print insta.username
	
if __name__ == "__main__":
	main()