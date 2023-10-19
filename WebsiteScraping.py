from bs4 import BeautifulSoup
import requests
import time
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
print('Enter your unwanted skill')
skill = input('>')
print('Enter your unwanted skill 2')
skill2 = input('>')
print(f"Unwanted skill is: {skill} and {skill2}")

def findJob():
    jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')
    #print(jobs)
    for index,job in enumerate(jobs):
        jobtime = job.find('span', class_='sim-posted').span.text

        #print(jobtime)
        if 'few' in jobtime:
            fjob = job.find('h3',class_ = 'joblist-comp-name').text.replace(' ', '')
            #print(fjob)
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            if skill not in skills and skill2 not in skills:
                #print(skills)
                with open(f'posts/{index}.txt','w') as f:

                    linkk = job.find('header',class_="clearfix").h2.a['href']
                    f.write(f"Link: {linkk}")
                    f.write(f"Company Name: {fjob.strip()}")
                    f.write(f"Skills Required: {skills.strip()}")
                    f.write('')

if __name__ == '__main__':
    while True:
        findJob()
        print('Waiting for 10 mins')
        time.sleep(600)
