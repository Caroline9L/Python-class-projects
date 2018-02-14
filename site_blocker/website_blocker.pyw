import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts" 
hosts_temp = "C:\Users\netadmin\AppData\Local\Package-Cache\{8388fa07-1617-4b8d-8ad8-6a940ad8052c}\Python36-32\Udemy\site_blocker\hosts"
redirect = "127.0.0.1"
website_list = [
    "www.businessinsider.com", "businessinsider.com", "mail.google.com/mail/",
    "gmail.com"
]

while True:
    if dt(dt.now().year,
          dt.now().month,
          dt.now().day, 9) < dt.now() < dt(dt.now().year,
                                           dt.now().month,
                                           dt.now().day, 10):
        print("Working hours")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Chill out")
    time.sleep(5)
