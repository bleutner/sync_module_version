#!/usr/bin/env python3
import re
import sys
from pathlib import Path
def main(file=sys.argv[1:]):
    init_file = Path(file[0])

    with init_file.open() as f:
        version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

    VERSION = (init_file.parents[2]/"VERSION.txt")
    if not VERSION.exists():
        print(f"No matching VERSION.txt file found for {init_file}")
    else:
        with open(VERSION, "r") as f:
            g = f.read()
            
            if g != version:
                print(f"Updating {VERSION} with version {version}")
                with open(VERSION, "w") as f:
                    f.seek(0)
                    f.write(version)
            else:
                print(f"{VERSION} already up to date at {version}")

if __name__ == "__main__":
    main()