import requests
from colorama import Fore

url = input(f"{Fore.RED}[{Fore.GREEN}?{Fore.RED}]{Fore.GREEN} Enter webhhook url {Fore.RED}> ")

result = requests.request(method="DELETE", url=url)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"{Fore.RED}[{Fore.GREEN}!{Fore.RED}]{Fore.GREEN} " + str(err))
else:
    print(f"{Fore.RED}[{Fore.GREEN}*{Fore.RED}]{Fore.GREEN} Webhook successfully deleted\n{Fore.RED}[{Fore.GREEN}*{Fore.RED}]{Fore.GREEN} Status code: {result.status_code}")
