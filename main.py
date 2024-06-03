
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup


def get_member_since(username: str) -> str:
    """
    Fetches the month and year a user joined CodeWars.

    Args:
    username (str): The CodeWars username.

    Returns:
    str: The month and year the user joined CodeWars, separated by a space.
    """
    # Construct the URL for the user's CodeWars profile
    url = f'https://www.codewars.com/users/{username}'

    # Open the URL and read the response
    response = urlopen(url)

    # Parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(response.read(), 'html.parser')

    # Find all 'div' elements with the class 'stat'
    stat_classes = soup.find_all("div", {"class": "stat"})

    member_since = ""
    # Iterate over the found elements to locate the 'Member Since' data
    for stat_class in stat_classes:
        data = str(stat_class)
        if 'Member Since' in data:
            member_since = data
            break

    # Extract the 'Member Since' date using regular expressions
    result = re.split('>|<', member_since)[-3]

    print(f'{username} is a member of CodeWars since {result}')
    return result


def main():
    # Example usages of the get_member_since function
    get_member_since('Fantasista766')
    get_member_since('jhoffner')


if __name__ == '__main__':
    main()
