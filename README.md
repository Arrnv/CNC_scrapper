# CNC Project

This project involves web scraping to collect supplier data for CNC machine components and a cost estimation algorithm to predict CNC part costs. The project is split into two main scripts: `WebScraper.py` and `CNC_Predicter.py`.

## Prerequisites

1. **Anaconda**: It is recommended to use Anaconda for creating a virtual environment. You can download Anaconda from [here](https://www.anaconda.com/products/distribution).

## Setup

### Step 1: Create a Conda Environment

1. Open Anaconda Prompt or your terminal.
2. Create a new conda environment:

   ```bash
   conda create --name cnc_project python=3.9
3. Activate the newly created environment:

   ```bash
   conda activate cnc_project
   ```
### Step 2: Install Required Packages

1. Clone the repository or download the project files.

2. Navigate to the project directory where the requirements.txt file is located.

3. Install the required packages:

  ```bash
  pip install -r requirements.txt
  ```
### Step 3: Download the Necessary Libraries
Make sure you have the following Python libraries installed in your environment:

BeautifulSoup4
requests
pandas

```bash

  pip install -r requirements.txt
```
# How to run
### Step 1: Run the Web Scraper
The first step is to run the WebScraper.py script to collect supplier data and create the dataset.

Ensure you are in the project directory.

Run the WebScraper.py script:

  ```bash
  python WebScraper.py
  ```
This script will scrape data from the specified URLs and generate a CSV file named suplyer.csv containing the supplier data.

### Step 2: Run the CNC Cost Predictor
After generating the supplier dataset, you can run the CNC_Predicter.py script to estimate CNC part costs.

Run the CNC_Predicter.py script:

  ```bash
  python CNC_Predicter.py
  ```
The script will prompt you to input the required specifications for the CNC part. The input format is provided within the script. The algorithm will then calculate and display the estimated cost range for the CNC part based on the input specifications.

Detailed Instructions
# WebScraper.py
This script scrapes supplier data from the specified URLs and compiles it into a CSV file.
It uses the BeautifulSoup library to parse HTML content and the requests library to fetch web pages.
The script iterates through each product link found on the web pages, extracts relevant data, and stores it in a dictionary.
The dictionary is then converted into a Pandas DataFrame and exported to a CSV file named suplyer.csv.
# CNC_Predicter.py
This script uses the supplier data from suplyer.csv to estimate CNC part costs.
It requires user input for the material type, material usage, part size, and complexity level.
The script validates the input and calculates the cost range using predefined cost factors for materials, machine time, tooling, labor, and overhead.
The estimated cost range is displayed based on the input specifications.






