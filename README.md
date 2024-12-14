# LinkedIn URL Resolver

## Description

This project provides a Python script to resolve LinkedIn redirect URLs and replace them with their original URLs in text files. The script is designed to help users clean up and process text files containing LinkedIn short URLs by resolving and replacing them with the final destination URLs.

---

## Features

- Automatically detects LinkedIn short URLs (e.g., `https://lnkd.in/...`) in a text file.
- Resolves these URLs to their final destinations.
- Replaces the original LinkedIn URLs with the resolved URLs in the text.
- Outputs the updated content to a new file.
- Copies the updated content to the clipboard for convenience.

---

## Requirements

To use this script, ensure you have the following installed:

- Python 3.6+
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `pyperclip`

You can install the dependencies using:
```bash
pip install requests beautifulsoup4 pyperclip
```

---

## How to Use

### 1. Input File
Create a file named `input.txt` in the same directory as the script. This file should contain text with LinkedIn short URLs. For example:

```
Check out these LinkedIn resources:
- https://lnkd.in/eShFW2GQ
- https://lnkd.in/e3wd4TNa

Enjoy exploring!
```

### 2. Run the Script
Run the script using the following command:
```bash
python lnkd_resolver.py
```

### 3. Output
After execution:
1. The script generates an `output.txt` file containing the updated text with resolved URLs.
2. The updated content is also copied to your clipboard for easy pasting.

For example, the `output.txt` might look like this:
```
Check out these LinkedIn resources:
- https://jorgectf.gitbook.io/awae-oswe-preparation-resources
- https://another-external-resource.com

Enjoy exploring!
```

---

## Code Overview

### `extract_final_url(linkedin_url)`
- Resolves a LinkedIn short URL to its final destination.
- Uses the `requests` library to fetch the intermediate LinkedIn page and BeautifulSoup to parse the external URL.
- Returns the original URL if no valid link is found or an error occurs.

### `replace_urls_in_text(text)`
- Detects all LinkedIn short URLs in the given text using regular expressions.
- Resolves each URL using `extract_final_url`.
- Replaces the original LinkedIn URLs with their resolved URLs in the text.

### `main()`
- Reads content from `input.txt`.
- Processes the text to replace LinkedIn URLs with their resolved counterparts.
- Writes the updated text to `output.txt`.
- Copies the updated content to the clipboard.

---

## File Structure

```
.
├── lnkd_resolver.py  # Python script
├── input.txt         # Input text file
├── output.txt        # Output text file
```

---

## Contributing

Feel free to fork this repository and submit pull requests to improve the script or add new features. Suggestions are always welcome!

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
