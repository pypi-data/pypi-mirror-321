import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from io import StringIO
from tqdm import tqdm

def get_webdriver():
    """Set up a headless Chrome WebDriver with a custom user-agent."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
    return webdriver.Chrome(options=chrome_options)

def scrape_website(months, years, commodities, markets):
    """
    Scrape agricultural commodity data from the Karnataka market website.

    Args:
        months (list): List of months to scrape.
        years (list): List of years to scrape.
        commodities (list): List of commodities to scrape.
        markets (list): List of markets to scrape.

    Returns:
        pd.DataFrame: A DataFrame containing the scraped data.
    """
    driver = get_webdriver()

    try:
        driver.get("https://krama.karnataka.gov.in/reports/DateWiseReport")
        data_frames = []
        total_iterations = len(months) * len(years) * len(commodities) * len(markets)

        with tqdm(total=total_iterations, desc="Scraping Data", ncols=100) as pbar:
            for year in years:
                for month in months:
                    for commodity in commodities:
                        for market in markets:
                            # Select dropdown values
                            Select(driver.find_element(By.ID, "_ctl0_MainContent_ddlmonth")).select_by_visible_text(month)
                            Select(driver.find_element(By.ID, "_ctl0_MainContent_ddlyear")).select_by_visible_text(year)
                            Select(driver.find_element(By.ID, "_ctl0_MainContent_ddlcommodity")).select_by_visible_text(commodity)
                            Select(driver.find_element(By.ID, "_ctl0_MainContent_ddlmarket")).select_by_visible_text(market)

                            # Click the "View Report" button
                            driver.find_element(By.ID, "_ctl0_MainContent_viewreport").click()
                            time.sleep(2)  # Wait for the page to load

                            # Scrape the table data
                            table = driver.find_element(By.ID, "_ctl0_MainContent_pnlgrd")
                            html_buffer = StringIO(table.get_attribute("outerHTML"))
                            df = pd.read_html(html_buffer)[0]
                            df['Commodity'] = commodity
                            data_frames.append(df)

                            pbar.update(1)
                            driver.back()

        # Combine and preprocess the data
        final_dataframe = pd.concat(data_frames, ignore_index=True)
        final_dataframe = final_dataframe[~final_dataframe.apply(lambda row: row.astype(str).str.contains('Total').any(), axis=1)].copy()
        final_dataframe['Market'] = final_dataframe['Market'].ffill()
        final_dataframe['Date'] = pd.to_datetime(final_dataframe['Date'], dayfirst=True)
        final_dataframe = final_dataframe.infer_objects()
        final_dataframe.set_index('Date', inplace=True)
        return final_dataframe
    finally:
        driver.quit()