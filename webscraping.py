from bs4 import BeautifulSoup
import requests
import pandas as pd

def connect_scrape(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.findAll('li', 'clearfix job-bx wht-shd-bx')

def write_job_details(job):
    job_title = job.find('h2').text.replace(' ', '')
    company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
    link_to_job = job.header.h2.a['href']
    time_posted = job.find('span', class_='sim-posted').text
    skills_required = job.find('span', class_='srp-skills').text
    skills_required_list = [skill.strip() for skill in skills_required.split(',')]
    if any(skill in familiar_skills_list for skill in skills_required_list):
        return {
            'Company Name': company_name.strip(),
            'Job Title': job_title.strip(),
            'Required Skills': skills_required.strip(),
            'Time Posted': time_posted.strip(),
            'Link to apply': link_to_job.strip()
        }
    else:
        return None

base_url = 'https://www.timesjobs.com/candidate/job-search.html'
familiar_skills_list = []

while True:
    skill = input("Enter skills you are familiar with (or 'done' to finish): ")
    if skill.lower() == "done":
        break
    familiar_skills_list.append(skill)

print('All Postings are being posted to set file...\n')

jobs_list = []

for page in range(1,21):
    url_page = f'{base_url}?searchType=Home_Search&from=submit&asKey=OFF' \
        f'&txtKeywords=&cboPresFuncArea=35&sequence={page}&page=1'
    jobs_page = connect_scrape(url_page)

    if not jobs_page:
        break  # Stops the loop if no more job postings found

    for job in jobs_page:
        job_details = write_job_details(job)
        if job_details:
            jobs_list.append(job_details)

df = pd.DataFrame(jobs_list)

# Save DataFrame to CSV file
output_csv_file = 'job_details.csv'
df.to_csv(output_csv_file, index=False)

print(f'Data has been saved to {output_csv_file}.')
