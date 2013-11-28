from selenium import webdriver
import unittest
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait


TEST_USER = 'admin'
TEST_PASSWORD = 'admin'
TEST_DATA = {'name': 'John', 'surname': 'Smith', 'bithdate': '07-02-1987',
             'bio': 'I was born on 7 July 1987', 'email': 'john@mail.com', 'skype': 'john.smith',
             'jabber': 'johnsmith', 'other_contacts': 'Phone: 1234567'}


def ajax_complete(driver):
    try:
        return 0 == driver.execute_script("return jQuery.active")
    except WebDriverException:
        pass


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

    def authorize(self):
        self.browser.get('http://localhost:8000/logout/')

        self.browser.get('http://localhost:8000/edit_home/')

        self.browser.find_element_by_id('id_username').send_keys(TEST_USER)
        self.browser.find_element_by_id('id_password').send_keys(TEST_PASSWORD)
        self.browser.find_element_by_xpath("//*[@type='submit']").click()

    def test_authorization(self):

        self.authorize()
        self.assertEqual(self.browser.current_url, 'http://localhost:8000/edit_home/')

    def test_edit_main_page(self):

        self.authorize()

        for key, value in TEST_DATA.iteritems():
            element = self.browser.find_element_by_id('id_%s' % key)
            element.clear()
            element.send_keys(value)

        self.browser.find_element_by_xpath("//*[@type='submit']").click()

        WebDriverWait(self.browser, 10).until(ajax_complete)

        output = self.browser.find_element_by_class_name('output').text
        self.assertIn("Form saved successful.", output)

        self.browser.get('http://localhost:8000')

        left = self.browser.find_element_by_class_name('left').text

        self.assertIn(TEST_DATA['name'], left)
        self.assertIn(TEST_DATA['surname'], left)
        self.assertIn('July 2, 1987', left)
        self.assertIn(TEST_DATA['bio'], left)

        right = self.browser.find_element_by_class_name('right').text

        self.assertIn(TEST_DATA['email'], right)
        self.assertIn(TEST_DATA['skype'], right)
        self.assertIn(TEST_DATA['jabber'], right)
        self.assertIn(TEST_DATA['other_contacts'], right)


if __name__ == '__main__':
    unittest.main()