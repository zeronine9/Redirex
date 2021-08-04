import requests
import threading 
from colorama import Fore
import argparse
import time

logo = '''   __          _ _         __  __
  /__\ ___  __| (_)_ __ ___\ \/ /
 / \/// _ \/ _` | | '__/ _ \\  / 
/ _  \  __/ (_| | | | |  __//  \ 
\/ \_/\___|\__,_|_|_|  \___/_/\_\

                            
                coded by Zahir Tariq'''

print(Fore.BLUE + logo)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
parser = argparse.ArgumentParser()
parser.add_argument("-f","--file",help="urls file to scan", required=True)
parser.add_argument("-p","--payloads",help="payloads file", required=True)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

args = parser.parse_args()


result = []


def req(url,payload):
    try:
        url = url.strip()
        payload = payload.strip()
        uurl = url + payload
        uurl = uurl.strip()
        response = requests.get(uurl)
        time.sleep(.2)
        location = response.url
        if response.is_redirect == True:
            print(uurl + " || " + response.status_code + " || " + location)
            result.append(uurl)
        else : 
            print(Fore.GREEN+"Testing")
    except Exception:
        None



def main():
    start = time.perf_counter()
    list_of_threads = []
    urls_file = args.file.strip()
    paylods_file = args.payloads.strip()
    for url in open(urls_file,'r').readlines():
        for payload in open(paylods_file).readlines():
            new_threading = threading.Thread(target=req,args=[url,payload])
            new_threading.start()
            list_of_threads.append(new_threading)
                    

    for thread in list_of_threads:
        thread.join()

    finish = time.perf_counter()
    print(f'\n\n\Finished in {round(finish-start,2)} second(s)\n')


if __name__ == '__main__':
    main()

###############
## Results
###############

out = open('result.txt','w')
for target in result:
    out.write(str(target))
    out.write('\n')

out.close()

















