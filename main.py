import requests


def currency_converter(base_curr, target_curr):
    url = f"https://v6.exchangerate-api.com/v6/c8a947d057693bbed9de9153/pair/{base_curr}/{target_curr}"
    try:
        response = requests.get(
            url,
            timeout=3,
            verify=True,
        )
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error")
        print(errh.args[0])
    except requests.exceptions.ReadTimeout as errt:
        print("Time Out")
    except requests.exceptions.ConnectionError as conerr:
        print("Connection Error !")

    except requests.exceptions.SSLError as sslerr:
        print("SSL Error")
    except requests.exceptions.RequestException:
        print("Something Went Wrong! ")
    else:
        data = response.json()
        rate = data["conversion_rate"]
        return rate


def user_input():
    base_curr = input("Enter a base currency(Eg: USD, GBP): ").upper()
    target_curr = input("Enter a target currency(Eg: NPR, INR): ").upper()
    amt = input("Enter an amount to convert to target currency: ")
    return base_curr, target_curr, amt


def main():
    while True:
        base_curr, target_curr, amt = user_input()
        if not base_curr.isalpha() or not target_curr.isalpha():
            print("Currency must contain letters only!")
            continue

        if len(base_curr) != 3 or len(target_curr) != 3:
            print("Currency code must contain exactly 3 letters!")
            continue

        try:
            amt = float(amt)
            if amt < 0:
                continue

        except ValueError:
            print("Amount must be number !")
            continue
        break
    rate = currency_converter(base_curr, target_curr)
    if rate is None:
        print("Failed to get exchange rate.")
        return

    converted = amt * rate

    print(f"{amt} {base_curr} = {converted:.2f} {target_curr}")


if __name__ == "__main__":
    main()
