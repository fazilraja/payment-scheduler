from date import Date
import json
import requests

class CountryNotFoundError(Exception):
    pass

def getCountryHolidays(country: str, startYear: int, endYear: int) -> dict:
    """Get a list of holidays for a given country.

    Args:
        country (str): The country to get the holidays for.

    Returns:
        dict: A list of holidays for the given country.
    """
    country_holidays = {}
    country_code = ''

    if country == "United States":
        country_code = 'US'
    elif country == "Australia":
        country_code = 'AU'
    elif country == "Brazil":
        country_code = 'BR'
    elif country == "Germany":
        country_code = 'DE'
    elif country == "Italy":
        country_code = 'IT'
    elif country == "South Africa":
        country_code = 'ZA'
    else:
        raise CountryNotFoundError(f"Country not found: {country}")

    for year in range(startYear, endYear + 1):
        response = requests.get(f'https://date.nager.at/api/v3/publicholidays/{year}/{country_code}')
        holidays = json.loads(response.content)

        for holiday in holidays:
            if (holiday['global']):
                year, month, day = holiday['date'].split('-')
                country_holidays[Date(int(day), int(month), int(year))] = holiday['localName']
    return country_holidays

if __name__ == "__main__":
    pass