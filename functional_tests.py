from selenium import webdriver

browser = webdriver.Firefox()

# Edith has heard about a cool new online to-do app.She goes
# to check out it's homepage
browser.get('http://localhost:8000')

# She notices the page title and header mention to-do lists
assert 'To-DO' in browser.title

# She is invited to enter a to-do item straight away

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
