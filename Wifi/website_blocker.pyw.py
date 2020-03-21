import time
host=r"C:\Windows\System32\drivers\etc\hosts"

redirect="127.0.0.1"
website_list=["facebook.com","www.facebook.com","facebook"]

while True:
    with open(host,'r+') as file:
        content=file.read()
        for web in website_list:
            if web in content:
                pass
            else:
                file.write(redirect+" "+web+"\n")
            
    print("hello")
    time.sleep(5)