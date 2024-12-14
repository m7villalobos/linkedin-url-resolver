import re
import requests
from bs4 import BeautifulSoup
import pyperclip

# Files for input and output
input_file = "input.txt"
output_file = "output.txt"


def extract_final_url(linkedin_url):
    """Extract the external URL from LinkedIn intermediate pages."""
    try:
        response = requests.get(linkedin_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        external_link = soup.find('a', href=True)
        # Ensure the URL is absolute
        if external_link and external_link['href'].startswith('http'):
            return external_link['href']
        return linkedin_url  # Return the original URL if no valid link found
    except Exception as e:
        return linkedin_url  # Return the original URL on error


def replace_urls_in_text(text):
    """Replace LinkedIn redirect URLs with their final resolved URLs."""
    # Find all LinkedIn URLs in the text
    linkedin_urls = re.findall(r"https://lnkd\.in/\S+", text)
    for url in linkedin_urls:
        # Resolve each URL
        resolved_url = extract_final_url(url)
        # Replace the original LinkedIn URL with the resolved URL
        text = text.replace(url, resolved_url)
    return text


def main():
    # Read input content
    with open(input_file, "r") as file:
        input_text = file.read()

    # Replace LinkedIn URLs in the text
    output_text = replace_urls_in_text(input_text)

    # Write the updated content to the output file
    with open(output_file, "w") as file:
        file.write(output_text)

    # Copy the updated content to clipboard
    pyperclip.copy(output_text)


if __name__ == "__main__":
    main()
