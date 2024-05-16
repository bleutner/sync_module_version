#!/usr/bin/env python3

import re
import sys
from pathlib import Path

def main(argv=None):
    # Check if the commit contains changes to __init__.py
    print(argv)
    if "__init__.py" in argv[0]:
        init_file = Path("__init__.py")

        with init_file.open() as f:
            version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

        with open("VERSION.txt", "rw") as f:
            g = f.read()
            if g != version:
                f.seek(0)
                f.write(version)

if __name__ == "__main__":
    main()