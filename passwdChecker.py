class PasswordChecker:
	def check_password_length(self, passwd):
		if len(passwd) >= 8:
			return True
		else:
			return False

if __name__ == '__main__':
	passwdChecker = PasswordChecker()
	print('Does password meet the rules? ' + str(passwdChecker.check_password_length('asgard-is-real')))
