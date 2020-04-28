import requests
import json

def get_ver(pkg):
    rec = requests.get("https://pypi.org/pypi/{package}/json".format(package=pkg)).json()
    return rec['info']['version']

def make_line(pkg):
    return '{}=="{}"\n'.format(pkg, get_ver(pkg))

if __name__ == '__main__':
    with open("requirements.txt", "w") as requirements:
        pkg = input("input package names, or press return to continue:\n| ")
        while pkg:
            try:
                requirements.write(make_line(pkg))
                pkg = input("| ")
            except json.decoder.JSONDecodeError:
                print("Package '{}' not found.".format(pkg))
                quit(1)