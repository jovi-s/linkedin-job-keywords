import pandas as pd
from selenium import webdriver
from time import sleep
import logging

def scrape_jobs(url, n_jobs):
    url = url
    no_of_jobs = n_jobs

    # this will open up new window with the url provided above 
    wd = webdriver.Chrome(executable_path="C:/Users/slamm/Downloads/AIAP8/Resume Writing LinkedIn Workshop/linkedin_jobs_tfidf-keywords/chromedriver.exe")
    wd.get(url)
    sleep(3)

    i = 2
    while i <= int(no_of_jobs/25)+1: 
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        i = i + 1
        try:
            wd.find_element_by_xpath("/html/body/main/div/section/button").click()
            sleep(5)
        except:
            pass
            sleep(5)

    jobs_lists = wd.find_element_by_class_name("jobs-search__results-list")
    jobs = jobs_lists.find_elements_by_tag_name("li") # return a list

    logging.info(f"Number of linkedin jobs to be scraped: {len(jobs)}")

    job_title = []
    company_name = []
    location = []
    date = []
    job_link = []
    logging.info("Getting job information...")
    for job in jobs:
        job_title0 = job.find_element_by_css_selector("h3").get_attribute("innerText")
        job_title.append(job_title0)

        company_name0 = job.find_element_by_css_selector("h4").get_attribute("innerText")
        company_name.append(company_name0)

        location0 = job.find_element_by_css_selector("span.job-search-card__location").get_attribute("innerText")
        location.append(location0)

        date0 = job.find_element_by_css_selector("div>div>time").get_attribute("datetime")
        date.append(date0)
        
        job_link0 = job.find_element_by_css_selector("a").get_attribute("href")
        job_link.append(job_link0)

    
    jd = []
    seniority = []
    logging.info("Getting job description and seniority information...")
    for item in range(len(jobs)):

        job_click_path = f'//*[@id="main-content"]/section[2]/ul/li[{item+1}]'
        wd.find_element_by_xpath(job_click_path).click()
        sleep(5)

        jd0 = wd.find_element_by_css_selector("section.description>div.description__text").get_attribute("innerText")
        jd.append(jd0)

        seniority0 = wd.find_element_by_css_selector("section.description>ul>li:nth-child(1)>span").get_attribute("innerText")
        seniority.append(seniority0)

    jobs_dict = ({
        "Date": date,
        "Company": company_name,
        "Title": job_title,
        "Location": location,
        "Description": jd,
        "Level": seniority,
        "Link": job_link
    })

    job_data = pd.DataFrame({ key:pd.Series(value) for key, value in jobs_dict.items() })

    # cleaning description column
    job_data["Description"] = job_data["Description"].str.replace("\n"," ")
    logging.info("Saving job data file in /reports/ ...")
    return job_data.to_excel("./reports/job_data.xlsx", index=False)