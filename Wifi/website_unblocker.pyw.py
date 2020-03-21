import time
#host=r"C:\Windows\System32\drivers\etc\hosts"
host="hosts"
redirect="127.0.0.1"
website_list=["facebook.com","www.facebook.com"]

while True:
    with open(host,'r+') as file:
        content=file.readlines()
        file.seek(0)
        for lines in content:
            if not any(website in lines for website in website_list):
                file.write(lines)
        file.truncate()
    print("hello")
    time.sleep(5)