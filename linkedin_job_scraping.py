import requests
from lxml import html
import pandas as pd

class LINKEDIN:
    def crawl_job(self, company_name, location):
        flag = True
        start = 0  
        batch_size = 10
        id_list = []
        while flag:
            try:
                list_url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={company_name}&location={location}&start={start}"
                response = requests.get(list_url)
                print(response.status_code)
                dom = html.fromstring(response.text)
                page_jobs = dom.xpath("//div[contains(@class, 'base-card')]/@data-entity-urn | //a[contains(@class, 'base-card')]/@data-entity-urn")
                for job in page_jobs:
                    job_id = job.split(":")[-1]
                    id_list.append(job_id)
                start += batch_size
            except Exception as e:
                flag = False
        return id_list
    
    def grab_data(self, id_list):
        count = len(id_list)
        job_list = []
        for job_id in id_list:
            try:
                job_url = f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}"
                job_response = requests.get(job_url)
                dom = html.fromstring(job_response.text)
                job_title = dom.xpath("//h2[contains(@class, 'top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title')]/text()")
                company_name = dom.xpath("//a[contains(@class, 'topcard__org-name-link topcard__flavor--black-link')]/text()")
                time_posted = dom.xpath("//span[contains(@class, 'posted-time-ago__text topcard__flavor--metadata')]/text()")
                location = dom.xpath("//span[contains(@class, 'topcard__flavor topcard__flavor--bullet')]/text()")
                num_applicants = dom.xpath("//figcaption[contains(@class, 'num-applicants__caption')]/text()")
                info_text = dom.xpath("//span[contains(@class, 'description__job-criteria-text description__job-criteria-text--criteria')]/text()")
                job_post = {}
                job_post["Job Title"] = job_title[0].strip() if job_title else 'Not Available'
                job_post['Company Name'] = company_name[0].strip() if company_name else 'Not Available'
                job_post['Location'] = location[0].strip() if location else ''
                job_post['Time Posted'] = time_posted[0].strip() if time_posted else 'Not Available'
                job_post['Job Description'] = ""
                job_post['num_applicants'] =  num_applicants[0].strip() if num_applicants else 'Not Available'
                job_post['Seniority level'] = info_text[0].strip() if info_text else 'Not Available'
                job_post['Employment type'] = info_text[1].strip() if info_text else 'Not Available'
                job_post['Job function'] = info_text[2].strip() if info_text else 'Not Available'
                job_post['Industries'] = info_text[3].strip() if info_text else 'Not Available'
                job_post['URL'] = dom.xpath("//a[contains(@class, 'topcard__link')]/@href")[0]
                job_list.append(job_post)
                print(f"Job {count} done")
                count -= 1
            except Exception as e:
                print(e)
        return job_list

            

if __name__ == "__main__":
    linkedin = LINKEDIN()
    id_list = linkedin.crawl_job("cognizant", "India")
    data = linkedin.grab_data(id_list)
    jobs_df = pd.DataFrame(data)
    jobs_df.to_csv('cognizant.csv', index = False)
