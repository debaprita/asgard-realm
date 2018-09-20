import unittest
import passwdChecker as PasswordChecker

class Test(unittest.TestCase):
	pChecker = PasswordChecker.PasswordChecker()
	
	def test_check_password_length(self):
		print('Checking passwords for compliance \n')
		passwdList = ['!llNotF@il@11' ,'@her05welcome', 'lost4ever#']
		
		for passwd in passwdList:
			print('Checking password: ' + passwd )
			passInfo = self.pChecker.check_password_length(passwd)
			self.assertTrue(passInfo)


if __name__ == '__main__':
	unittest.main()
			
