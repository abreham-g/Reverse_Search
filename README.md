# Reverse_Search

### Objective:
Our task is to reverse search the provided product titles and return their corresponding Amazon.com links (US version only) and ASINs (Amazon Standard Identification Numbers). 

### Provided Data:
We are given a list of product titles and prices in an Excel file. Your goal is to find the matching product on Amazon and retrieve the following details:


### our Reverse Search Strategy:
        ◦ Start by using the product titles provided to search for matching products on Amazon.com.
        ◦ If direct searching on Amazon.com doesn’t yield clear results, you may first use a general search engine (e.g., Google or Bing) to find the correct product, and then follow the link to its Amazon.com page.
        ◦ Ensure the product title and price match as closely as possible to the provided information.
### Data to Return:
        ◦ Amazon Link: Once a match is found, retrieve the full product URL from Amazon.com.
        ◦ ASIN: Extract the ASIN from the product’s URL or page. The ASIN is a 10-character alphanumeric string found in the product URL (e.g., B00X4WHP5E).


### Requirements
- Python 3.10+
- Dependencies listed in requirements.txt
### Clone the repository:
      - git clone https://github.com/abreham-g/Reverse_Search.git
      - cd Reverse_Search/scrip
      - python main.py