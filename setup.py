from __future__ import annotations

import zipfile

from os import listdir
from os.path import isfile, join

from pathlib import Path
import requests


URL = "https://cdn.intra.42.fr/document/document/18556/leaves.zip"
ZIP_NAME = "leaves.zip"
EXTRACT_FOLDER = "images"

def has_images_folder(folder : Path) -> bool:
    if not folder.exists():
        return False
    return any(folder.iterdir())

def download_zip(dest: Path) -> None:
    try:
        r = requests.get(URL, timeout = 10)
        r.raise_for_status()
        dest.write_bytes(r.content)
    except r.RequestException as e:
        raise RuntimeError(f"Failed to download the file:{e}") from e

def extract_zip(zip_path: Path, extract_to:Path) -> None:
    try:
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_to)
    except zipfile.BadZipFile as e:
        raise RuntimeError(f"invalid zip file: {zip_path}") from e

def delete_zip(zip_path: Path) -> None:
    try:
        zip_path.unlink()
    except FileNotFoundError as e:
        print(f"Zip file not found in deletion attempt: {e}")


def main() -> None:
    base_path = Path(__file__).parent.resolve()
    zip_path = base_path / ZIP_NAME
    images_folder = base_path / EXTRACT_FOLDER

    if not has_images_folder(images_folder):
        if not zip_path.exists():
            download_zip(zip_path)
        extract_zip(zip_path, base_path)
    delete_zip(zip_path)

if __name__ == "__main__":
    main()

