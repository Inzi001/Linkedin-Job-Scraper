# LinkedIn Job Scraper

A Python-based web scraper that extracts job listings from LinkedIn using `requests`, `lxml`, and `pandas`. This scraper collects job titles, company names, locations, and job URLs, and stores the extracted data in a CSV file.

## Features

- Extracts job titles, companies, locations, and URLs
- Saves data in CSV format for easy analysis
- Lightweight and efficient using `requests`, `lxml`, and `pandas`

## Requirements

Ensure you have the following packages installed:

```bash
pip install requests lxml pandas
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/Inzi001/Linkedin-Job-Scraper.git
cd linkedin-job-scraper
```

2. Run the scraper:

```bash
python scraper.py
```

3. View the extracted data in `jobs.csv`.

## Project Structure

```
linkedin-job-scraper/
├── scraper.py
└── README.md
```

## Example Output

| Job Title                  | Company Name   | Location                        | Time Posted    | Job Description                 | num_applicants     | Seniority Level    | Employment Type    | Job Function                     | Industries                          | URL                             |
|----------------------------|----------------|---------------------------------|---------------|---------------------------------|--------------------|-------------------|-------------------|----------------------------------|-------------------------------------|----------------------------------|
| Executive - Recruitment    | Cognizant      | Bangalore Urban, Karnataka, India | 2 weeks ago   |                                | Over 200 applicants | Entry level       | Full-time         | Human Resources                  | IT Services and Consulting          | https://in.linkedin.com/jobs/view/executive-recruitment-at-cognizant-4138163199 |
| Accounts Payable Specialist| Cognizant      | Thane, Maharashtra, India        | 3 weeks ago   |                                | Over 200 applicants | Mid-Senior level  | Full-time         | Accounting/Auditing              | Financial Services                  | https://in.linkedin.com/jobs/view/accounts-payable-specialist-at-cognizant-4158449083 |
| Data Analyst               | Cognizant      | Bangalore Urban, Karnataka, India | 2 weeks ago   |                                | Over 200 applicants | Entry level       | Full-time         | Information Technology           | IT Services and Consulting          | https://in.linkedin.com/jobs/view/data-analyst-at-cognizant-4159393406 |
| QA Analyst Associate       | Cognizant      | Pune, Maharashtra, India         | 3 weeks ago   |                                | Over 200 applicants | Entry level       | Full-time         | Quality Assurance                | IT Services and Consulting          | https://in.linkedin.com/jobs/view/qa-analyst-associate-at-cognizant-4137290936 |
| Program Manager            | Cognizant      | Greater Kolkata Area             | 2 weeks ago   |                                | Not Available      | Entry level       | Full-time         | Project Management and IT        | IT Services and Consulting          | https://in.linkedin.com/jobs/view/program-manager-at-cognizant-4165755261 |
| React JS                   | Cognizant      | Kochi, Kerala, India             | 2 weeks ago   |                                | First 25 applicants | Not Applicable    | Full-time         | Other                            | IT Services and Consulting          | https://in.linkedin.com/jobs/view/react-js-at-cognizant-4159389817 |
| Selenium Test Engineer     | Cognizant      | Chennai, Tamil Nadu, India       | 1 week ago    |                                | Over 200 applicants | Entry level       | Full-time         | Engineering and Information Tech | IT Services and Consulting          | https://in.linkedin.com/jobs/view/selenium-test-engineer-at-cognizant-4174259024 |
| General Manager - Operations| Cognizant      | Hyderabad, Telangana, India      | 3 weeks ago   |                                | Not Available      | Executive         | Full-time         | Management and Manufacturing     | IT Services and Consulting          | https://in.linkedin.com/jobs/view/general-manager-operations-at-cognizant-4142231832 |
| Purchasing Specialist      | Cognizant      | Thane, Maharashtra, India        | 3 weeks ago   |                                | Over 200 applicants | Mid-Senior level  | Full-time         | Purchasing and Supply Chain      | Financial Services                  | https://in.linkedin.com/jobs/view/purchasing-specialist-at-cognizant-4158454245 |


## Customization

- **Search Query**: Modify the search parameters in `scraper.py` to target specific job titles or locations.
- **Output Format**: Adapt the code to store data in other formats (Excel, JSON, etc.).

## Contributions

Contributions are welcome! Feel free to fork this repository and open a pull request.

## License

This project is licensed under the MIT License.

## Disclaimer

This project is for educational purposes only. Scraping LinkedIn may violate their Terms of Service—use responsibly.

