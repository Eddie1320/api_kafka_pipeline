def get_data():
    import requests

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]

    return res

if __name__ == "__main__":
    from pprint import pprint
    data = get_data()
    pprint(data)