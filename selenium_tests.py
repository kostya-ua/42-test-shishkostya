from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_loading_mail_page(self):

        self.browser.get('http://localhost:8000')

        name = self.browser.find_element_by_id('name').text
        self.assertEqual(name, 'Kostyantyn')

        surname = self.browser.find_element_by_id('surname').text
        self.assertEqual(surname, 'Shish')

        bith_date = self.browser.find_element_by_id('bith_date').text
        self.assertEqual(bith_date, 'May 13, 1989')

        email = self.browser.find_element_by_id('email').text
        self.assertEqual(email, 'Email: shish.kostya@gmail.com')

        jabber = self.browser.find_element_by_id('jabber').text
        self.assertEqual(jabber, 'Jabber: shishkostya@jabber.at')

        skype = self.browser.find_element_by_id('skype').text
        self.assertEqual(skype, 'Skype: kotya___')


if __name__ == '__main__':
    unittest.main()