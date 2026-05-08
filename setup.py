import requests
import zipfile
from os import listdir
from os.path import isfile, join

import pathlib

def check_image_folder(path:str) -> bool:
    file = [f for f in listdir(path) if isfile(join(path, "images"))]
    if not file:
        return False
    return True

def main():
    mypath = pathlib.Path(__file__).parent.resolve()
    if not check_image_folder(mypath):
        r = requests.get('https://cdn.intra.42.fr/document/document/18556/leaves.zip')
        zip_name = "leaves.zip"
        with open(zip_name, 'wb') as f:
            f.write(r.content)
    zip_path = join(mypath,'leaves.zip')
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(mypath)


if __name__ == "__main__":
    main()

