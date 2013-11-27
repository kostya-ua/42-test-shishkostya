from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_loading_main_page(self):

        self.browser.get('http://localhost:8000')

        left = self.browser.find_element_by_class_name('left').text

        self.assertIn('Kostyantyn', left)
        self.assertIn('Shish', left)
        self.assertIn('May 13, 1989', left)

        right = self.browser.find_element_by_class_name('right').text

        self.assertIn('Email: shish.kostya@gmail.com', right)
        self.assertIn('Jabber: shishkostya@jabber.at', right)
        self.assertIn('Skype: kotya___', right)


if __name__ == '__main__':
    unittest.main()