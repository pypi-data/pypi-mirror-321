import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd


def get_paper_detail(code, year):
    url = f"https://www.waikato.ac.nz/study/papers/{code}/{year}/"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        html_content = response.text  # Get the HTML content as text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        # Handle the error appropriately (e.g., exit, retry, log)
        exit()  # Or other error handling

    with open("./paper_detail.html", 'w') as file:
        file.write(html_content)

    soup = BeautifulSoup(html_content, "html.parser")

    code = soup.find_all("h1", attrs={"class": "paper-page__code"})
    title = soup.find_all("p", attrs={"class": "paper-page__title"})
    summaries = soup.find_all("section", attrs={
        "class": "paper-page-section paper-page__body-summary restricted-width-element"
    })

    summary = summaries[0].text.strip() if len(summaries) > 0 else ""
    paragraphs = soup.find_all("div", attrs={"class": "key-info__item"})

    paper = {
        "Code": code[0].text,
        "Title": title[0].text,
        "Summary": summary
    }

    for paragraph in paragraphs:
        paper[paragraph.findChildren(
            "glossary-tooltip")[0]["term"]] = paragraph.text.strip()

    return paper


def get_papers(year, page, level):
    print(year, page, level, level[0])
    url = f"https://www.waikato.ac.nz/study/papers/?page={page}&filters=%7B%22academic_year%22%3A%7B%22academic_year%22%3A%7B%22{year}%22%3A{year}%7D%7D%2C%22paper_level%22%3A%7B%22paper_level_code%22%3A%7B%22Level+{level}%22%3A%22{level[0]}%22%7D%7D%7D"
    options = Options()
    options.add_argument("--headless=new")  # Run Chrome in headless mode

    # Or webdriver.Firefox(), webdriver.Edge() etc.
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "paper-listing-page__result-list")
            )
        )

        html_content = driver.page_source

        with open("./papers.html", 'w') as file:
            file.write(html_content)

        soup = BeautifulSoup(html_content, "html.parser")
        code = soup.find_all(
            "ul", attrs={"class": "paper-listing-page__result-list"}
        )
        lis = code[0].find_all("li")
        papers = []
        for li in lis:
            papers.append(
                {
                    "code": li.find_all("span", attrs={"class": "paper-listing-page__paper-code"})[0].text,
                    "title": li.find_all("span", attrs={"class": "paper-listing-page__paper-title"})[0].text
                }
            )
        return papers
    finally:
        driver.quit()  # Close the browser


def add_a_paper(paper):
    df = pd.DataFrame([paper])

    file_path = "./papers.csv"

    try:
        existing_df = pd.read_csv(file_path)  # Read existing data
    except FileNotFoundError:
        existing_df = pd.DataFrame()  # Create an empty DataFrame if the file doesn't exist

    updated_df = pd.concat(
        [existing_df, df], ignore_index=True)  # Append new data
    updated_df.to_csv(file_path, index=False)  # Write back to the CSV
