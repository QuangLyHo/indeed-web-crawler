from bs4 import BeautifulSoup
import requests

def get_url(position, location):
    template = 'https://www.indeed.com/jobs?q={}&l={}'
    url = template.format(position, location)
    return url


job_position = input('Enter Job Position: ')
job_location = input('Enter City State: ')
url = get_url(job_position, job_location)
response = requests.get(url)


def find_job():
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('div', class_='jobsearch-SerpJobCard')
    for job in jobs:
        date_posted = job.find('span', attrs={'class': 'date'}).text
        date_list = date_posted.replace('+', '').split()
        if date_list[0] == 'Today' or date_list[0] == 'Just' or int(date_list[0]) <= 14:
            company_name = job.find('span', class_='company').text.lstrip()
            skills = job.find('div', class_='summary').text.lstrip()
            date_published = job.find('span', class_='date').text.lstrip()
            try:
                salary = job.find('span', class_='salary no-wrap').text.lstrip()
            except AttributeError:
                salary = 'NA'
            a_tag = job.h2.a['href']
            more_info = 'https://indeed.com' + a_tag

            print(f"""
Company Name: {company_name.strip()}
Skills: {skills.strip()}
Date Posted: {date_published.strip()}
Salary: {salary.strip()}
More Info: {more_info.strip()}
""")

find_job()





