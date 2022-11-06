import unittest
import heritage

class TestDisplays(unittest.TestCase):
    def test_display_user(self):
        utilisateur = heritage.User("User1", "password")
        self.assertEqual(utilisateur.display(),"User1")

    def test_display_post(self):
        user = heritage.User("userTest","password123")
        post = heritage.Post("Ceci est un test",user, "today")
        self.assertEqual(   "-"*60 + "\n" + "Ceci est un test \n Published by : userTest on today",\
                            post.display())

if __name__ == '__main__':
    unittest.main()