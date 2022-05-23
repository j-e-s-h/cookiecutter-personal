import os
import sys
import re

project_slug = "{{ cookiecutter.project_slug }}"


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"


if not re.match(MODULE_REGEX, project_slug):
    print(f'{ERROR_COLOR}ERROR: %s is not a valid name.{RESET_ALL}')

    sys.exit(1)

print(f"{MESSAGE_COLOR}Let's do it! You're are going to create something awesome!")
print(f"Creating project at { os.getcwd() }{RESET_ALL}")