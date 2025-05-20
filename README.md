# Upwork Job Analyzer

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![HTTPX](https://img.shields.io/badge/HTTPX-Latest-green)](https://www.python-httpx.org/)
[![Selectolax](https://img.shields.io/badge/Selectolax-Latest-yellow)](https://github.com/rushter/selectolax)
[![NoDriver](https://img.shields.io/badge/NoDriver-Latest-red)](https://github.com/ultrafunkamsterdam/nodriver)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-lightgray)](https://github.com/Esethucreates/upwork_scraper_demo)

A data collection tool designed to analyze Upwork job postings for market research purposes. This project helps identify trending skills and opportunities in the freelance marketplace.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Challenges & Limitations](#challenges--limitations)
- [Future Development](#future-development)
- [License](#license)

## 🔍 Project Overview

The Upwork Job Analyzer is a specialized web scraping tool that collects job posting data from Upwork. The primary goal is to gather intelligence on market demand for different skills and services, allowing for data-driven decisions on which services to offer as a freelancer.

**For non-technical readers:** Think of this as a research assistant that collects information about what skills businesses are looking for right now. Instead of manually checking thousands of job postings, this tool can do it automatically and help identify profitable service opportunities.

## ✨ Key Features

- **Automated Data Collection:** Extracts job titles and descriptions from Upwork listings
- **Cookie Management:** Handles authentication challenges with a sophisticated cookie system
- **Headless Browser Integration:** Uses browser simulation for more natural web interactions
- **Anti-Detection Measures:** Implements strategies to appear as a regular user (with limited success)
- **Configurable Search Parameters:** Easily adjust search criteria through configuration file

## 🛠️ Technology Stack

- **Python:** Core programming language
- **HTTPX:** Modern HTTP client for making web requests
- **NoDriver:** Headless browser library for cookie extraction
- **Selectolax:** Fast HTML parsing library
- **JSON:** Data storage format for cookie persistence
- **PyAutoGUI (Planned Alternative):** Library for GUI automation and screenshot-based data extraction

## 📁 Project Structure

The project consists of three main components:

1. **`cookie_manager.py`**
   - Launches a headless browser session
   - Completes the Cloudflare challenge
   - Extracts and stores authentication cookies
   - Refreshes cookies approximately every 15 minutes

2. **`json_cookie_manager.py`**
   - Retrieves stored cookies from JSON file
   - Formats cookies into a dictionary for HTTP requests
   - Provides a clean interface for the scraper module

3. **`upwork_scraper.py`**
   - Main scraping functionality
   - Uses cookies to authenticate requests
   - Extracts job titles and descriptions
   - Handles request errors and retries

## 💻 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Esethucreates/upwork_scraper_demo.git
   cd upwork_scraper_demo
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install httpx selectolax nodriver
   or 
   pip install -r requirements.txt
   ```



## 🚀 Usage

1. First, generate fresh cookies:
   ```bash
   python cookie_manager.py
   ```

2. Run the scraper:
   ```bash
   python upwork_scraper.py
   ```

3. View the collected data:
   ```bash
   python analyze_results.py  # (Planned for future development)
   ```

## ⚠️ Challenges & Limitations

This project faced a significant hurdle with Cloudflare's bot detection system. Despite using advanced browser emulation through NoDriver, the scraper was consistently detected as automated traffic after brief periods of operation.

The current implementation can successfully:
- Extract cookies and make initial requests
- Parse job data from successful responses
- Store cookies for reuse

However, it cannot:
- Maintain long scraping sessions without being blocked
- Collect large datasets in a single run
- Completely bypass sophisticated anti-bot measures

**Important Note on Testing:** Frequent testing can result in your IP address being blocked by Upwork/Cloudflare. Consider using a VPN or limiting test frequency if developing this project further.

**Note for employers:** This project demonstrates my ability to work with HTTP requests, browser automation, HTML parsing, and data extraction, even though the complete market research goal wasn't fully realized due to external constraints.

## 🔮 Future Development

If Cloudflare detection issues could be overcome, planned features include:

- Natural Language Processing to categorize jobs by required skills
- Data visualization of job market trends
- Automated reporting on high-demand services
- Keyword analysis for job descriptions
- Pricing analysis for different service categories

### Alternative Approach

An alternative development path being considered is to pivot to a GUI automation approach:
- Using PyAutoGUI to control the browser directly
- Implementing screenshot-based data extraction
- This would simulate human interaction more effectively and potentially bypass anti-bot measures
- Would require different dependencies but could be more resilient against detection

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

*Created by [Esethu Zikhali](https://github.com/Esethucreates)*
