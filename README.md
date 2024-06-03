## Genius Lyrics Extractor

If you ever needed to extract lyrics from a Genius song website, you know the pain of copying the lyrics without coping andy ads or other unwanted text. This Python script scrapes lyrics from a Genius song website and saves them to a text file to make the process easier and more efficient.

**Requirements:**

-   Python 3.x
-   `requests` library: `pip install requests`
-   `beautifulsoup4` library: `pip install bs4`

**How to use:**

1. **Run the script:** Execute the Python code.
2. **Enter the URL:** The script will prompt you to enter the URL of the Genius song website you want to scrape.
3. **Lyrics saved:** The script will scrape the lyrics from the provided URL and save them to a file named `lyrics.txt`.

**Usage Example:**

```
Enter the URL of Genius song website: https://genius.com/Eminem-houdini-lyrics
```

The script will then scrape the lyrics from the given URL and save them to the `lyrics.txt` file.

**Notes:**

-   The script assumes that the Genius website uses the `data-lyrics-container` attribute to identify the lyrics container.
-   The script handles `UnicodeEncodeError` by printing an error message and skipping the line. You can adjust this error handling as needed.
-   This script is for educational purposes only. Please respect the copyright of the songwriters and artists.
