cookie_list = [
    {'domain': 'localhost', 'httpOnly': False, 'name': 'PHPSESSID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'plmojp8h1rlgotki1emrfuvbpp'},
    {'domain': 'localhost', 'httpOnly': True, 'name': 'wordpress_logged_in_d0ae86309cda26b347aa32d9ce217696', 'path': '/test_lite1/', 'sameSite': 'Lax', 'secure': False, 'value': 'armember9%7C1704210724%7CtgsJQ9Q6zH31OH7JlRgBoOv3pi2rnDpdgJvhloMFcZ8%7Cdbf9ef2b1e3dc5a8e767261eb6f30d27bc5daf61278c79f25fa26c04f3df2608'}
]

desired_name = 'wordpress_logged_in_d0ae86309cda26b347aa32d9ce217696'

# Find the dictionary that matches the specified name
desired_cookie = next((cookie for cookie in cookie_list if cookie['name'] == desired_name), None)

if desired_cookie:
    value = desired_cookie['value'].split('|')[0]  # Extracting 'armember9' from the value
    print(value)  # Output: armember9
else:
    print("Cookie with the specified name not found.")