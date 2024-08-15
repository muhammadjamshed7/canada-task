# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.common.by import By
# # import time
# # import random
# # import pickle
# # import csv
# # import os

# # # Configurations
# # email = 'gullshanza75@gmail.com'
# # password = os.getenv('namal123#')  # Use environment variable for security
# # group_url = 'https://www.linkedin.com/groups/1976445/'

# # # Initialize WebDriver
# # driver = webdriver.Chrome()
# # driver.get('https://www.linkedin.com/login')

# # # Login
# # username = driver.find_element(By.ID, 'gullshanza75@gmail.com')
# # password_field = driver.find_element(By.ID, 'namal123#')

# # username.send_keys(email)
# # password_field.send_keys(password)
# # password_field.send_keys(Keys.RETURN)

# # # Wait for 2FA
# # time.sleep(15)

# # # Save cookies after login
# # pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

# # # Load cookies on script restart
# # driver.get('https://www.linkedin.com')
# # cookies = pickle.load(open("cookies.pkl", "rb"))
# # for cookie in cookies:
# #     driver.add_cookie(cookie)

# # # Visit group page
# # driver.get(group_url)

# # with open('comments.txt', 'r') as f:
# #     comments = f.readlines()


# # posts = driver.find_elements(By.CLASS_NAME,                             "feed-shared-update-v2 feed-shared-update-v2--minimal-padding full-height relative  feed-shared-update-v2--wrapped")  
# # for post in posts:
# #     try:
        
# #         like_button = post.find_element(By.CLASS_NAME,                                         "reactions-react-button feed-shared-social-action-bar__action-button")
# #         like_button.click()
        
       
# #         comment_box = post.find_element(By.CLASS_NAME, 
# #                                         "artdeco-hoverable-trigger artdeco-hoverable-trigger--content-placed-top artdeco-hoverable-trigger--is-hoverable ember-view feed-shared-social-action-bar__action-button")
# #         comment_box.send_keys(random.choice(comments).strip())
# #         comment_box.send_keys(Keys.RETURN)
        
# #         # Repost the post
# #         repost_button = post.find_element(By.CLASS_NAME, "artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view feed-shared-social-action-bar__action-button")
# #         repost_button.click()
        
# #         # Follow the user/company if the follow button is visible
# #         follow_button = post.find_element(By.CLASS_NAME, 'follow-button-class')
# #         if follow_button.is_displayed():
# #             follow_button.click()
        
# #         # Record interaction to avoid duplicates
# #         post_id = post.get_attribute('data-post-id')
# #         with open('tracking.csv', 'a', newline='') as csvfile:
# #             writer = csv.writer(csvfile)
# #             writer.writerow([post_id, 'liked', 'commented', 'reposted'])

# #         # Delay to avoid detection
# #         time.sleep(random.uniform(2, 5))

# #     except Exception as e:
# #         print(f"Error interacting with post: {e}")

# #     # Pause for 10 minutes after every 100 posts
# #     if len(posts) % 100 == 0:
# #         time.sleep(600)

# # # Handle internet disconnections (simplified example)
# # while True:
# #     try:
# #         # Your script logic here
# #         pass
# #     except Exception as e:
# #         print(f"Error occurred: {e}")
# #         print("Waiting for internet reconnection...")
# #         time.sleep(30)
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# import random
# import pickle
# import csv
# import os

# # Configurations
# email = 'gullshanza75@gmail.com'
# password = "namal123#"  # Ensure this environment variable is set correctly
# group_url = 'https://www.linkedin.com/groups/1976445/'

# if not password:
#     raise ValueError("The environment variable 'LINKEDIN_PASSWORD' is not set. Please set it before running the script.")

# # Initialize WebDriver
# driver = webdriver.Chrome()
# driver.get('https://www.linkedin.com/login')

# # Login
# username_field = driver.find_element(By.ID, 'username')
# password_field = driver.find_element(By.ID, 'password')

# username_field.send_keys(email)
# password_field.send_keys(password)
# password_field.send_keys(Keys.RETURN)

# # Wait for 2FA
# time.sleep(15)  # Adjust based on your 2FA method

# # Save cookies after login
# pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

# # Load cookies on script restart
# driver.get('https://www.linkedin.com')
# cookies = pickle.load(open("cookies.pkl", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)
# driver.get(group_url)  # Visit group page again after adding cookies

# # Load comments from file
# with open('comments.txt', 'r') as f:
#     comments = f.readlines()

# # Function to interact with posts
# def interact_with_posts():
#     posts = driver.find_elements(By.CLASS_NAME, "feed-shared-update-v2")
#     for post in posts:
#         try:
#             # Like the post
#             like_button = post.find_element(By.CLASS_NAME, "reactions-react-button")
#             like_button.click()

#             # Comment on the post
#             comment_box = post.find_element(By.CLASS_NAME, "artdeco-hoverable-trigger")
#             comment_box.click()  # Click to focus the comment box
#             comment_box.send_keys(random.choice(comments).strip())
#             comment_box.send_keys(Keys.RETURN)

#             # Repost the post
#             repost_button = post.find_element(By.CLASS_NAME, "artdeco-dropdown")
#             repost_button.click()

#             # Follow the user/company if the follow button is visible
#             follow_button = post.find_element(By.CLASS_NAME, 'follow-button-class')
#             if follow_button.is_displayed():
#                 follow_button.click()

#             # Record interaction to avoid duplicates
#             post_id = post.get_attribute('data-post-id')  # Ensure this attribute exists
#             with open('tracking.csv', 'a', newline='') as csvfile:
#                 writer = csv.writer(csvfile)
#                 writer.writerow([post_id, 'liked', 'commented', 'reposted'])

#             # Delay to avoid detection
#             time.sleep(random.uniform(2, 5))

#         except Exception as e:
#             print(f"Error interacting with post: {e}")

#     # Pause for 10 minutes after every 100 posts
#     if len(posts) % 100 == 0:
#         time.sleep(600)

# # Scroll to load more posts if needed
# def scroll_and_interact():
#     while True:
#         interact_with_posts()
#         # Scroll down to load more posts
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(7)  # Adjust based on how quickly posts load

# # Handle internet disconnections (simplified example)
# while True:
#     try:
#         scroll_and_interact()
#     except Exception as e:
#         print(f"Error occurred: {e}")
#         print("Waiting for internet reconnection...")
#         time.sleep(30)


#corrected code above


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import pickle
import csv
import os

# Configurations
email = 'gullshanza75@gmail.com'
password = "namal123#"  # Ensure this environment variable is set
group_url = 'https://www.linkedin.com/groups/1976445/'

# Validate environment variable
if not password:
    raise ValueError("The environment variable 'LINKEDIN_PASSWORD' is not set. Please set it before running the script.")

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/login')

# Login
username_field = driver.find_element(By.ID, 'username')
password_field = driver.find_element(By.ID, 'password')

username_field.send_keys(email)
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# Wait for 2FA
time.sleep(15)  # Adjust based on your 2FA method

# Save cookies after login
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

# Load cookies on script restart
driver.get('https://www.linkedin.com')
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get(group_url)  # Visit group page again after adding cookies

# Load comments from file
comments = [
    'Great post!',
    'Thanks for sharing!',
    'Interesting insights.',
    'I agree with this point.',
    'Nice article!',
    'Very informative.',
    'Well written!',
    'Great perspective!',
    'Insightful thoughts!',
    'Good read!'
]

# Function to interact with posts
def interact_with_posts():
    posts = driver.find_elements(By.CLASS_NAME, "feed-shared-update-v2")
    for post in posts:
        try:
            # Like the post
            like_button = post.find_element(By.CLASS_NAME, "reactions-react-button")
            like_button.click()

            # Comment on the post
            # comment_box = post.find_element(By.CLASS_NAME, 
            #                                 "artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view social-actions-button comment-button flex-wrap ")
            comment_box = post.find_element(By.CLASS_NAME, "artdeco-button.artdeco-button--muted.artdeco-button--4.artdeco-button--tertiary.ember-view.social-actions-button.comment-button.flex-wrap"
    )
            comment_box.click()  # Click to focus the comment box
            comment_box.send_keys(random.choice(comments).strip())
            comment_box.send_keys(Keys.RETURN)

            # Repost the post
            repost_button = post.find_element(By.CLASS_NAME, "artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view feed-shared-social-action-bar__action-button")
            repost_button.click()

            # Follow the user/company if the follow button is visible
            follow_button = post.find_element(By.CLASS_NAME,                                               "follow   update-components-actor__follow-button update-components-update-v2__follow-button artdeco-button")
            if follow_button.is_displayed():
                follow_button.click()

            # Record interaction to avoid duplicates
            post_id = post.get_attribute('ember258')  # Ensure this attribute exists
            with open('tracking.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([post_id, 'liked', 'commented', 'reposted'])

            # Delay to avoid detection
            time.sleep(random.uniform(2, 5))

        except Exception as e:
            print(f"Error interacting with post: {e}")

    # Pause for 10 minutes after every 100 posts
    if len(posts) % 100 == 0:
        time.sleep(600)

# Scroll to load more posts if needed
def scroll_and_interact():
    while True:
        interact_with_posts()
        # Scroll down to load more posts
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(8)  # Adjust based on how quickly posts load

# Handle internet disconnections (simplified example)
while True:
    try:
        scroll_and_interact()
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Waiting for internet reconnection...")
        time.sleep(30)
