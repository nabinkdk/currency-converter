# Currency Converter

A simple Python CLI application that converts currency amounts using real-time exchange rates from the ExchangeRate API.

## Features

- **Real-time Exchange Rates**: Fetches live conversion rates using the ExchangeRate API
- **Input Validation**:
  - Validates currency codes (must be exactly 3 alphabetic characters)
  - Validates amounts (must be numeric and non-negative)
- **Error Handling**: Handles network timeouts and API errors gracefully
- **Simple Interface**: Interactive command-line interface for easy currency conversion

## Requirements

- Python 3.8+
- requests library

## Installation

Install the required dependency:

```bash
pip install requests
```

## Usage

Run the main script:

```bash
python main.py
```

Follow the prompts to:

1. Enter a base currency code (e.g., USD, GBP)
2. Enter a target currency code (e.g., NPR, INR)
3. Enter the amount to convert

The script will display the converted amount rounded to 2 decimal places.

## Example

```
Enter a base currency(Eg: USD, GBP): USD
Enter a target currency(Eg: NPR, INR): EUR
Enter an amount to convert to target currency: 100
100.0 USD = 92.50 EUR
```

## API Information

This project uses the [ExchangeRate API](https://www.exchangerate-api.com/) for fetching current exchange rates.

## License

This project is provided as-is.
