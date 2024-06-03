# CodeWars Member Since Fetcher
This Python project allows you to fetch the month and year a user joined CodeWars by scraping the user's profile page. It uses the `urllib.request` library to open URLs and the `BeautifulSoup` library to parse HTML content. Regular expressions are used to extract the relevant information.

## Features
- Fetches the "Member Since" date from a CodeWars user's profile.
- Uses web scraping techniques to extract data from HTML.
- Example usage included to demonstrate functionality.

## Prerequisites
Make sure you have the following libraries installed:

- `beautifulsoup4`
- `urllib`
- `re`

You can install `beautifulsoup4` using pip if you haven't already:

```bash
pip install beautifulsoup4
```

## Usage
To use the `get_member_since` function, follow these steps:

1. Clone the repository or download the code.
2. Ensure you have Python installed on your machine.
3. Run the script using the command:

```bash
python main.py
```

### Example
The `main` function in the script provides example usage of the `get_member_since` function:

```python
def main():
    # Example usages of the get_member_since function
    get_member_since('Fantasista766')
    get_member_since('jhoffner')
```
Running the script will print the "Member Since" date for the specified users:

```plaintext
Fantasista766 is a member of CodeWars since Jan 2022
jhoffner is a member of CodeWars since Oct 2012
```
## Code Overview
The script contains the following main components:

### `get_member_since(username: str) -> str`
Fetches the month and year a user joined CodeWars.

#### Args:
- `username` (str): The CodeWars username.
#### Returns:
- `str`: The month and year the user joined CodeWars, separated by a space.

### `main()`
Provides example usages of the `get_member_since` function.