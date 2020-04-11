def describe_city(city, country="United States"):
    print(f"{city.title()} is in {country.title()}.")

describe_city('philadelphia')
describe_city('paris', 'france')
describe_city('toronto', country="canada")
