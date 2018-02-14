import time
from datetime import datetime as dt

hosts_path=r"C:\Windows\System32\drivers\etc\hosts" # needs to be opened in a cmd with admin rights
# hosts_temp = "hosts"
hosts_temp = "C:\Users\netadmin\AppData\Local\Package-Cache\{8388fa07-1617-4b8d-8ad8-6a940ad8052c}\Python36-32\Udemy\site_blocker\hosts"
redirect = "127.0.0.1"
website_list = [
    "www.businessinsider.com", "businessinsider.com", "mail.google.com/mail/", "gmail.com"
]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 1):
        print("Working hours")
        # open hosts_temp
        # with open(hosts_temp, 'r+') as file:
        with open(hosts_path, 'r+') as file:
            # if these lines don\'t already exist -
            content=file.read()
            # print(content)
            # write redirect + websitelist[i] <-- loop thru to iterate
            for website in website_list:
                # if the site is in the file
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
                    # save/close
    else:
        # open hosts_temp
        # with open(hosts_temp, "r+") as file:
        with open(hosts_path, "r+") as file:
            # if these lines do already exist, store file as a series of lists
            content = file.readlines()
            # erase last 4 lines - move cursor to start of doc
            file.seek(0)
            for line in content:
                # loop thru and check each line for the strings in the website list
                if not any(website in line for website in website_list):
                    # do "nothing" - just write the line back out as is
                    file.write(line)
            # remove everything after that
            file.truncate()
        print("Chill out")
    time.sleep(5)

# print(1) # print 1 every millisecond (because python, not time - time would convert this from ms to sec)
# time.sleep(5) # take 5 seconds (because time) between each print