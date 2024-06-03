import requests
from bs4 import BeautifulSoup

with open("lyrics.txt", "w", encoding='utf-8') as file:
    file.write("")  # Clear the file

# Send a GET request to the website you want to scrape
url = input("Enter the URL of Genious song website: ")

response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all divs with the desired data-attribute
lyrics_containers = soup.find_all("div", attrs={"data-lyrics-container": "true"})

# Loop through the found divs
for container in lyrics_containers:
    # Extract text from the container, including nested <a> and <span> tags
    lyrics = container.get_text(separator='\n', strip=True)

    # Split the extracted lyrics by newline characters
    lines = lyrics.splitlines()

    # Write each line to the file with proper line breaks
    with open("lyrics.txt", "a", encoding='utf-8') as file:
        for line in lines:
            try:
                file.write(line + "\n")
            except UnicodeEncodeError:
                # Handle the error here, like skipping the line or logging the issue
                print(f"Error encoding line: {line}")

print("Lyrics have been saved to lyrics.txt")