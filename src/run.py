import argparse
import logging
from .job_scraping import scrape_jobs
from .tfidf_keywords import keyword_weights
from .keybert import bert_keywords

def run(url, num_jobs, type):
    logging.info("Starting job scraping...")
    scrape_jobs(url, int(num_jobs))
    logging.info("Finished job scraping.")
    if type=="tf-idf":
        logging.info("Starting keyword analysis with tf-idf...")
        keyword_weights()
    elif type=="keybert":
        logging.info("Starting keyword analysis with BERT...")
        bert_keywords()
    logging.info("Completed keyword analysis. Please view excel file in /reports/")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--url', default="https://www.linkedin.com/jobs/search?keywords=Finance&location=Singapore&locationId=&geoId=102454443&sortBy=R&f_TPR=r2592000&f_JT=F&f_E=3&position=1&pageNum=0")
    parser.add_argument('-n','--num_jobs', default="100")
    parser.add_argument('-t','--type', default="tf-idf")

    args = parser.parse_args()
    run(args.url,
        args.num_jobs,
        args.type
    )