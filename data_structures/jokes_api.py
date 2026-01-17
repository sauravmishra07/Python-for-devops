import requests

base_uri = "https://v2.jokeapi.dev/joke/Any?"

blacklist_type = "political"

joke_type = "single"

amount_of_jokes = int(input("How many jokes you want to fetch? : "))

def fetch_jokes(amount):
    api_uri = f"{base_uri}blacklistFlags={blacklist_type}&type={joke_type}&amount={amount}"
    response = requests.get(api_uri)
    print(api_uri)

    if response.status_code == 200:
        jokes_data = response.json()
        # print(jokes_data)

        found_joke = False

        for key, value in jokes_data.items():
            if key == "joke":
                print(f"Joke: {value}\n")
                found_joke = True

        if not found_joke:
            print("No jokes found.")
    else:
        print("Failed to fetch the jokes data from the api.")

    


fetch_jokes(amount_of_jokes)
