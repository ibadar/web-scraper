import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def grab_data(website):
    print("Launching web page...")
    
    driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    
    try:
        driver.get(website)
        print("Page loading ... ")
        html = driver.page_source
        
        return html
    finally:
        driver.quit()
    
    """
    --> (driver_path) Specifies where our chrome driver path is 
    --> (options) Specify how our chrome driver works, can ignore certain things if wanted such as images etc
    --> (driver) Setting up the driver and what service we will use and what options we will use to run the driver
    
    """
def extract_body_content(results):
    soup = BeautifulSoup(results, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

    """
    --> (body_content) BS extracts all the body data that was collected by our web scraper
    --> Then if it does exist then we return the string of the body_content, otherwise we return nothing
    """
def remove_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    """
    This gets rid of anything within the soup body that has the tags realted to "SCRIPTS" or "STYLES"
    """
    
    clean_content = soup.get_text(separator="\n")
    clean_content = "\n".join(
        line.strip() for line in clean_content.splitlines() if line.split()
    )
    """
    --> (clean_content) line 47 Gets all the text and separates it with a new line "\n"
    --> (clean_content) line 48 Makes sure that \n character is separating something, i.e if there are no texts between the \n then we will remove the \n which is meaningless
    """
    return clean_content

def split_all_content(dom_content, max_length=6000):
    return [
        dom_content[i : i+max_length] for i in range(0, len(dom_content), max_length)
    ]
    """
    This subroutine splits all our content that has now been cleaned into chunks.
    Since the LLM that we will be using has a character limit i.e token limit of approx 6000, we will feed the LLM with "chunks" of content so that all of our extracted data gets parsed.
    """