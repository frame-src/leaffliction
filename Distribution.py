from pathlib import Path
import sys

IMGS_PATH='images'


def check_path(arg:str) -> None:
    p = Path(__file__).parent / IMGS_PATH

    if not p.exists():
        raise FileNotFoundError(f"Path not found: {p}")
    ls_folder = []
    for value in p.iterdir():
        if arg.lower() in value.name.lower():
            ls_folder.append(value.name)

def 


def main() -> None:
    check_path((sys.argv)[1])

if __name__ == "__main__":
    main()
