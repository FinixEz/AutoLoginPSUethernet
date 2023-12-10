import socket
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Function to check network connectivity using ping
def is_connected():
    try:
        # Try to ping a remote server (e.g., Google's public DNS server)
        subprocess.run(["ping", "-c", "1", "8.8.8.8"], check=True)
        return True
    except subprocess.CalledProcessError:
        # If ping fails, return False
        pass
    return False

# Function to get the local IP address
def get_local_ip():
    try:
        # Connect to a remote server to get the local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except OSError:
        pass
    return None

# Set the desired IP address
desired_ip = 'this where you put you ip address'

# Set the path to your web driver executable (chromedriver.exe for Chrome)
driver_path = 'this is where u path of chromedriver.exe'

# Set your Ethernet login URL (in this case is login page)
login_url = 'https://cp-xml-40g.psu.ac.th/php/uid.php'

# Set your username and password
username = 'username in login page '
password = 'password in login page'

# Check network connectivity
if not is_connected():
    print("Network is down. Attempting to log in.")

    # Continuously check the local IP address until it matches the desired one
    while get_local_ip() != desired_ip:
        time.sleep(5)

    try:
        # Create a new instance of the Chrome driver
        driver = webdriver.Chrome(executable_path=driver_path)

        # Open the login page
        driver.get(login_url)
        print("Opened login page.")

        # Find the username and password input fields and fill them out
        username_input = driver.find_element_by_name('username')
        password_input = driver.find_element_by_name('password')

        username_input.send_keys(username)
        password_input.send_keys(password)

        # Submit the form
        password_input.send_keys(Keys.RETURN)
        print("Form submitted.")

        # Wait for a few seconds to ensure the login process is complete
        time.sleep(5)

        # Close the browser window
        driver.quit()
        print("Browser closed.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("Network is already connected.")
