import requests


def main():
    print(requests.get("https://google.com?q=python"))


if __name__ == "__main__":
    main()
