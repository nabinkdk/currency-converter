def user_input():
    base_curr = input("Enter a base currency(Eg: USD, GBP): ").upper()
    target_curr = input("Enter a base currency(Eg: NPR, INR): ").upper()
    return base_curr, target_curr


def main():
    while True:
        base_curr, target_curr = user_input()

        if not base_curr.isalpha() or not target_curr.isalpha():
            print("Currency must contain letters only!")
            continue

        if len(base_curr) != 3 or len(target_curr) != 3:
            print("Currency code must contain exactly 3 letters!")
            continue
        break

if __name__ == "__main__":
    main()

   
