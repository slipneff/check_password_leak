import sys
import hashlib
import requests


def check_leak_passwd(passwd):
    in_hash = hashlib.sha1(passwd.encode('utf-8'))
    in_hash = in_hash.hexdigest().upper()
    cropped_hash = in_hash[:5]
    url = f"https://api.pwnedpasswords.com/range/{cropped_hash}"
    header = {
        'User-Agent': 'leackes checker'
    }
    print
    req = requests.get(url, headers=header).content.decode('utf-8')

    hashes = req.split('\r\n')

    for h in hashes:
        leaked_hash = cropped_hash + h

        if in_hash in leaked_hash:
            return "LEAKED!"

    return "NOT LEAKED!"

try :
    if sys.argv[1] == "-p" or sys.argv[1] == "--password":
        passwd = sys.argv[2]
        print(sys.argv[2], " : ", check_leak_passwd(passwd))
    elif sys.argv[1] == "-f" or sys.argv[1] == "--file":
        with open(sys.argv[2], 'r') as f:
            for passwds in f:
                passwd = passwds.split()[0]
                print(passwd + " : " + check_leak_passwd(passwd)) 
except:
    print("Enter a password with '-p' or '--password' or enter the name of file with '-f' or '--file'! ")