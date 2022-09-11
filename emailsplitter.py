def emailsplit():
	emails = input("Input Email: ")
	if "@" in emails:
		usernames = emails.split("@")[0]
		domains = emails.split("@")[-1]
		print(usernames)
		print(domains)
	else:
		print(emails + " is not a valid email")

emailsplit()