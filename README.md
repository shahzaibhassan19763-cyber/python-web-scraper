# Python Web Scraper & Automation

A Python-based web scraping and automation project that collects book titles and prices from Books to Scrape using Requests and BeautifulSoup.

The scraped data is sent from Python to an n8n webhook, where it is processed and automatically added to Google Sheets. After the data is added successfully, an email notification is sent using Gmail.

This project was built as a practical learning project while developing my skills in Python, Web Scraping, APIs, Webhooks, n8n, and AI Automation.
## 🚀 Features

- Scrapes book titles and prices using Python
- Uses Requests for HTTP requests
- Uses BeautifulSoup for HTML parsing
- Sends scraped data to an n8n webhook
- Processes data using n8n
- Splits scraped data into individual items
- Automatically adds data to Google Sheets
- Sends an email notification after processing
- Demonstrates Python + API + Automation integration
  ## 🔄 Automation Workflow

The project follows this workflow:

Python Web Scraper
↓
n8n Webhook
↓
Split Out
↓
Google Sheets
↓
Gmail

### 1. Python Web Scraper

Python sends a request to the Books to Scrape website and extracts book titles and prices using BeautifulSoup.

### 2. n8n Webhook

The scraped data is sent from Python to an n8n webhook using an HTTP POST request.

### 3. Split Out

The n8n Split Out node processes the received data and separates the individual book records.

### 4. Google Sheets

The processed book information is automatically added as rows in Google Sheets.

### 5. Gmail

After the data is processed, the workflow sends an email notification using Gmail.

## 🛠️ Technologies Used

- Python
- Requests
- BeautifulSoup
- n8n
- Webhooks
- Google Sheets
- Gmail
- Git
- GitHub

 ## 📸 Automation Workflow

![n8n Automation Workflow](workflow.png)

## ⚙️ Installation

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/shahzaibhassan19763-cyber/python-web-scraper.git
```

### 2. Open the project folder

```bash
cd python-web-scraper
```

### 3. Install required libraries

```bash
pip install requests beautifulsoup4
```

### 4. Run the Python scraper

```bash
python n8n23.py
```

> Make sure Python is installed on your computer before running the project.

## 🔄 How It Works

This project connects Python web scraping with an n8n automation workflow.

### 1. Python Web Scraper

The Python script uses Requests and BeautifulSoup to collect book titles and prices from the Books to Scrape website.

### 2. Send Data to Webhook

After collecting the data, Python sends the scraped information to an n8n Webhook using an HTTP POST request.

### 3. Split Out the Data

The n8n Split Out node separates the received book data into individual records so each book can be processed separately.

### 4. Add Data to Google Sheets

The processed book information is automatically added as rows to a Google Sheets spreadsheet.

### 5. Send Email Notification

After the data is added successfully, the workflow uses Gmail to send an email notification.

### 🔁 Workflow

Python Scraper  
↓  
n8n Webhook  
↓  
Split Out  
↓  
Google Sheets  
↓  
Gmail

## 🧠 What I Learned

By building this project, I practiced and improved my understanding of:

- Python web scraping
- Requests and HTTP requests
- BeautifulSoup and HTML parsing
- Python lists and dictionaries
- JSON data handling
- HTTP POST requests
- Webhooks
- n8n workflow automation
- Google Sheets integration
- Gmail integration
- Connecting Python with automation tools
- Git and GitHub
- Building and documenting practical projects

  ## 🎯 Portfolio Goal

This project is part of my journey toward becoming an AI Automation Freelancer.

My goal is to build practical projects that demonstrate real-world skills in:

- Python
- Web Scraping
- APIs
- Webhooks
- n8n
- Workflow Automation
- AI Automation
- AI Agents

I am building and documenting practical projects on GitHub to create a professional portfolio that can demonstrate my skills and work to potential freelance clients.

My focus is not only on learning concepts, but also on building real projects and gradually developing the skills needed for professional automation work.
## 🔮 Future Improvements

This project can be improved further by adding:

- Scraping more book information
- Automatically scraping additional pages
- Saving scraped data to CSV or Excel
- Adding better error handling
- Adding data validation
- Scheduling the workflow to run automatically
- Connecting the workflow with AI tools
- Adding AI-based data analysis
- Creating more advanced automation workflows
- Adding monitoring and notifications for failed workflows

## 📌 Project Status

**Status:** Completed for learning and portfolio purposes

**Level:** Beginner → Intermediate

**Focus:** Python Web Scraping + Webhooks + n8n Automation

---

## ⚠️ Disclaimer

This project was created for educational and learning purposes. The website used in this project is a practice website designed for learning web scraping.

This project is not affiliated with or endorsed by WhatsApp, Meta, or any other third-party service. 
