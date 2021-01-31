from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Someone has heard about a cool new online to-do app.
        # it goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # It notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # It is invited to ener a to-do item straight away

        # It types "Buy peacock feathers" into a text box 

        # When it hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting it to add another item.
        # It enters "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on the list

        # It wonders wheter the site will remember its list. Then it sees
        # that the site has generated a unique URL for it -- there is some
        # explanatory text to that effect.

        # It visits the URL - the to-do list is still there.

        # Satisfied it goes back to sleep


if __name__ == "__main__":
    unittest.main(warnings='ignore')


