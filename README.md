<!-- TABLE OF CONTENTS -->

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#resouces">Resources</a></li>
  </ol>
</details>





<!-- ABOUT THE PROJECT -->
## About The Project

This project aims to extract keywords from a set of LinkedIn job postings. This is done via scraping from LinkedIn jobs search URL, https://www.linkedin.com/jobs. The user is encouraged to select relevant filters for a more precise search regarding specific jobs.

Scraping is done using Selenium and the results are saved into a .xlsx file for further use. An automatic webpage should open and the program will automatically click, and copy the relevant information. This is done through going into 'inspect' and via finding elements by `xpath`, `class_name`, `tag_name`, `css_selector` from the webpage.  

Regex is used on the job description column of the dataframe to clean it, a custom dataset of non essential words are removed from the text and words are then lemmatized using WordNetLemmatizer. A corpus is formed from the column and "english" stop words are removed and finally keyword extraction is done using TF-IDF or KeyBert. The user has the option to select which method to use from the command line.



### Built With

major frameworks that you built your project using
* NTLK
* TF-IDF
* KeyBert



<!-- GETTING STARTED -->
## Getting Started

instructions on setting up your project locally to get a local copy up and running follow these simple example steps. It is encouraged to run this on a virtual environment, steps to create one can be found 

[here]: https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/

 and 

[here]: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

### Prerequisites

Python

ChromeDriver

### Installation

1. Clone and change into the repo

   ```sh
   git clone https://github.com/jovi-s/linkedin-job-keywords.git && cd "$(basename "$_" .git)"
   ```

2. Install necessary packages

   ```
   pip install -r requirements.txt
   ```

3. Download chromedriver from https://chromedriver.chromium.org/downloads. Move 'chromedriver.exe' to "linkedin-job-keywords" folder.

4. Download wordnet

   ```sh
   $ python
   >>> import nltk
   >>> nltk.download('wordnet')
   ```



<!-- USAGE EXAMPLES -->
## Usage

How the project can be used

```
python -m run --url --num_jobs --type 
```

Example: Searching for relevant Finance jobs in Singapore (default)

```
python -m run --url https://www.linkedin.com/jobs/search?keywords=Finance&location=Singapore&locationId=&geoId=102454443&sortBy=R&f_TPR=r2592000&f_JT=F&f_E=3&position=1&pageNum=0
```

Arguments

- num_jobs (default=100)

  Number of jobs to search from the url provided.

- type (default=tf-idf)

  Keyword extraction method. ["tf-idf", "keybert"]

  

Presently, under the KeyBert method, a SentenceTransformer using `distilbert-base-nli-mean-tokens `model will be used to transform the document into vectors before KeyBert. 



#### Customization

- To add custom non essential words, open `non_essential_words.py` in an IDE and add/ remove from list
- Read KeyBert resource below and customize `keybert.py`



For more examples, please refer to the [Documentation](https://example.com)



<!-- ROADMAP -->

## Roadmap

- Develop Flask application for a graphical user interface.

See the [open issues](https://github.com/jovi-s/Best-README-Template/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->

## Contact

Jovinder Singh - [@j0v3s](https://twitter.com/j0v3s) - jovinder@yahoo.com

Project Link: [https://github.com/jovi-s/linkedin-job-keywords](https://github.com/jovi-s/linkedin-job-keywords)

Website: https://jovinder.com/



<!-- RESOURCES -->

## Resources

https://github.com/MaartenGr/KeyBERT

