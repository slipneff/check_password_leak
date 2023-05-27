# Check Password Leak

This script is designed to check if a given password has been leaked in any known data breaches. It helps users determine whether their password has been compromised and if they need to update it for better security.

## Features

- Uses the Have I Been Pwned (HIBP) API to check if the password has been previously leaked.
- Supports both single password checks and bulk checks from a file containing multiple passwords.
- Provides clear and concise results, indicating whether the password has been leaked or not.
- Respects user privacy by securely handling passwords without sending them to external servers.

## Installation

1. Clone the repository or download the script from [GitHub](https://github.com/slipneff/check_password_leak).
2. Make sure you have Python 3.x installed on your system.
3. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage

To check a single password, run the script with the following command:

```
python check_password_leak.py --password <your_password>
```

Replace `<your_password>` with the password you want to check.

To perform a bulk check using a file with multiple passwords, create a text file containing one password per line. Then run the script with the following command:

```
python check_password_leak.py --file <path_to_file>
```

Replace `<path_to_file>` with the path to your password file.

Please note that the script does not store or transmit your password or any other sensitive information. It securely hashes your password using the SHA-1 algorithm before sending the first five characters of the hash to the HIBP API.

## Example

To check a single password:

```
python check_password_leak.py --password mypassword123
```

To perform a bulk check using a password file named `passwords.txt`:

```
python check_password_leak.py --file passwords.txt
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on [GitHub](https://github.com/slipneff/check_password_leak).


## Disclaimer

While this script can help identify if a password has been leaked, it is important to note that it does not guarantee the security of your password or online accounts. It is always recommended to use strong and unique passwords, enable two-factor authentication, and follow best practices for online security. The script is provided as-is, without any warranty or guarantee of its effectiveness.
