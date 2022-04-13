from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        
        # Edith has heard about a cool new online to-do app.She goes
        # to check out it's homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        # She is invited to enter a to-do item straight away
if __name__ == '__main__':
    unittest.main()        
# She types "buy peacock feathers" into a text box (Efith's hobby 
# is tying fly-fishing lures)

# When she hits enter, the page updates, and now another page list
# "1: buy peacock feathers to make a fly" as an item in a to-do list

# There is still a text box inviting het to add another item. She
# enters "Use a peacock feather to make a fly" (Edith is very 
# methodical)

# The page updates again, and now shows both items on her list. 

# Edith wonders whether the site will remember her list. Then she
# sees 
# that the site has generated a unique URL for her -- there is some
# explenatory text to that effect.

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep

browser.quit()
