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

    def test_requests_showing(self):

        for i in range(10, 0, -1):
            self.browser.get('http://localhost:8000/test%d' % i)

        self.browser.get('http://localhost:8000/requests/')

        table = self.browser.find_element_by_class_name('requests_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn('/requests/', rows[1].text)
        self.assertEqual(len(rows), 11)


if __name__ == '__main__':
    unittest.main()