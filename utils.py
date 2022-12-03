import requests, os
from secret import session

def createInputFile(year=2022, day=1):
    path = f"{year}/Day{day}/"
    url = f'http://adventofcode.com/{year}/day/{day}/input'
    filename = f"{path}input.txt"
    if os.path.exists(filename):
        print(f"{filename} already exists, skipping fetch")
        return True
    response = requests.get(url, cookies={'session': session()})
    if response.status_code == 200:
        with open(filename, "w") as f:
            f.write(response.text)
    else:
        print(f"Response failed? status code{response.status_code} Probably need to update sesion :)")

createInputFile()