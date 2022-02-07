import requests

def main():

    payload = {"amount" : "2", "blacklistFlags": "religious"}
    response = requests.get("https://v2.jokeapi.dev/joke/Any",
                                params=payload)
                                
    if response.status_code != 200:
        raise Exception("There was a client side error!")
    else:
        print("Content: ", response.json())




if __name__ == "__main__":
    main()