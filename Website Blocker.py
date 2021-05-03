from datetime import datetime as dt

host_path="C:\Windows\System32\drivers\etc"
redirect="127.0.1.1"

website_list=["www.facebook.com","www.instagram.com"]



while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        with open(host_path,'r+') as myfile:
            content= myfile.read()
            for site in website_list:
                if site in content:
                    pass
                else:
                    myfile.write(redirect+" "+ site+"\n")
        print("All sites blocked")
        break
    else:
        with open(host_path,'r+') as myfile:
            content=myfile.readlines()
            myfile.seek(0)
            for line in content:
                if not any(site in line for site in website_list):
                    myfile.write(line)
            myfile.truncate()
        print("All sites unblocked")
        break