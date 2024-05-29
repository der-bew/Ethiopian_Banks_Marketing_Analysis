# Ethiopian Banks Marketing Analysis
## Overview
This project aims to analyze the marketing strategies of Ethiopian banks, focusing on the effectiveness of advertisements and their impact on customer engagement. As a Marketing Analytics Engineer, the goal is to provide the marketing and sales team with insights into the efficiency of their campaigns and suggest improvements.

## Repository Structure
```
Ethiopian_Banks_Marketing_Analysis/
├── .dvc/                   # DVC (Data Version Control) configuration
├── .github/workflows/      # GitHub Actions workflows
├── data/                   # Directory for storing data files
├── notebooks/              # Jupyter notebooks for exploratory data analysis (EDA)
│   ├── EDA.ipynb
├── scripts/                # Python scripts for data collection and processing
│   ├── __init__.py
│   ├── app_scrape.py       # Script for scraping data from Google Play Store
│   ├── db_connect.py       # Script for connecting to PostgreSQL database
│   ├── handler.py          # General handler script
│   ├── telegram_scrape.py  # Script for scraping data from Telegram
│   ├── visualizer.py       # Script for data visualization
├── .dvcignore              # Files and directories to ignore in DVC tracking
├── .gitignore              # Files and directories to ignore in Git
├── README.md               # Project documentation
├── docker-compose.yaml     # Docker Compose configuration for setting up the environment
├── Dockerfile
├── requirements.txt
```
## Setup Instructions
### Prerequisites
- Docker
- Docker Compose
- Python 3.8+
- PostgreSQL
## Clone the Repository
```
git clone https://github.com/der-bew/Ethiopian_Banks_Marketing_Analysis.git
cd Ethiopian_Banks_Marketing_Analysis
```
### Set Up Docker
To set up the environment using Docker, run:
```
docker-compose up
```
This command will start all necessary services, including the PostgreSQL database.

### Install Python Dependencies
If you prefer to run the scripts locally without Docker, install the required Python packages:
```
pip install -r requirements.txt
```
### Set Up PostgreSQL Database
Ensure that PostgreSQL is running and create a database for the project. Update the database connection settings in db_connect.py as needed.

### Run Data Collection Scripts
To collect data from various sources, run the following scripts:
1. Google Play Store Data:
  ```
  python scripts/app_scrape.py
  ```
2. Telegram Data:
     ```
     python scripts/telegram_scrape.py
    ```

## Project Objectives
- Collect advertisement data from the Tikvah-Ethiopia channel and store it in a PostgreSQL data warehouse.
- Gather Android app reviews and download counts from the Google Play Store.
- Acquire subscription data from the main bank's Telegram channel.
- Set up a dynamic dashboard system for real-time monitoring of marketing performance.
- Analyze the effectiveness of different advertisements and their impact on app downloads and Telegram subscriptions.
## Contributions
Contributions are welcome! Please open an issue or submit a pull request for any improvements or additions.

## Contact
For any questions or inquiries, please contact [der-bew](https://github.com/der-bew).
