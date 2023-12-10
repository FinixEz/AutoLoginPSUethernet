# Auto Login Script (still only work in Linux for me becasue i can't install Selenium in windows)

This script automates the login process to a specific network upon detecting a network connection. It is designed to work on both Linux and Windows environments.

## Features

- Automatically logs in to a network upon detecting an active connection.
- Cross-platform support for Linux and Windows.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Selenium library (install using `pip install selenium`)

For Windows:
- ChromeDriver (ensure the path is set correctly in the script)

## Configuration

Update the following variables in `auto_login.py` with your specific information:

- `desired_ip`: The desired local IP address.
- `driver_path`: Path to ChromeDriver executable (for Windows).
- `login_url`: URL for the login page.
- `username`: Your username.
- `password`: Your password.

## Running the Script

### Linux

```bash
python3 auto_login.py
