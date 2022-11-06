import unittest
import heritage

class TestDisplays(unittest.TestCase):
    def test_user(self):
        utilisateur = heritage.User("User1", "password")
        self.assertEqual(utilisateur.display(),"User1")

    #def test_

if __name__ == '__main__':
    unittest.main()