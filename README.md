# NLP and Glassdoor Reviews: Analysis of the Alternative Assets Industry 
**Author**: [Nick Timpano](mailto:nick.timpano@gmail.com)

## Overview 
The alternative assets industry is often regarded as being fairly tight-lipped about firm performance, but information about company culture can be just as self-contained.  

In this project, I analyze glassdoor review data on a subset of firms in the alternative assets industry in order to better understand the current state of employee happiness in this space, and what aspects of a company/role employees value. To do so, I first gather the data by using a scraping tool (more details [here](https://github.com/timpanon/glassdoor_nlp_alternatives/tree/master/glassdoor-review-scraper)) and then proceeded to conduct EDA and several natural language processing techniques to draw out insights on employee values and sentiment. I sought to understand what qualities of a company and role employees in this industry value most. 

#### Audience 
This analysis could be useful for anyone with an interest in better understanding employee sentiment in the alternative assets industry. 

## Data 
The data was extracted from csv files, containing review information for different companies. 

In order to actually retrieve the data from each company, I wrote a web scraping tool to grab reviews from individual Glassdoor pages. This was significantly more labor intensive than interacting with an API. Full code can found [here](https://github.com/timpanon/glassdoor_nlp_alternatives/tree/master/glassdoor-review-scraper).

## Methods/Techniques 
- EDA 
- Natural language processing preprocessing techniques
- Unigrams/bigrams analysis
- Topic modeling (GSDMM and LDA) 

## Results
- Glassdoor Reviews are more likely to be written in Q1  
![reviews by month](./pictures/reviews_by_month.png)
- Average Glassdoor review scores tend to change year by year for individual companies but have been relatively similar for the past few years when looking at all companies
![average scores per year](./pictures/reviews_by_year_all_firms.png)
- Employee priorities may have changed since the pandemic. Prior to the pandemic, office location was a more significant factor. Since then, other values such as work/life balance, job security, and being part of an inclusive culture seem to be more important.
![bigrams matrix](./pictures/bigrams_matrix.png)
- Employees from different departments rated their firms differently, indicating that some functions feel more or less valued. It may be worth digging into this further.
- Top rated firms appear to have less hierarchical environments, have put resources into creating environments that are welcoming for employees through benefits and perks and have hired and retained smart, collaborative talent 
- Lower rated companies have done poorly in creating inclusive work cultures and are plagued by politics, long hours, and cutthroat environments. 

## Recommendations 
Based on the model and the analysis of data, these were the findings and recommendations: 
- Invest in human resources departments. Although pay was important, it is really people and workplace relationships that are behind the highest and lowest rated firms.
- Focus more on employees in marketing, sales and the mid and back office departments. Figure out ways to make these employees feel more valued, and make sure compensation is fair. These employees rated their employers lowest.
- Hire diverse talent. Some employees are feeling left out, and even discriminated against.

## Next Steps 
- Closer look at individual firms: Some firms are trending up and down. Why is this? Is it related to performance or any other identifiable factors? 
- Other industries: Expand beyond the alternative assets space, and look at other industries such as tech. 
- Getting predictive: Ratings can be predicted through text data using word embedding, neural networks, etc..

## More Information 
To see the full EDA please see the [Jupyter Notebook](./investment_reviews_analysis.ipynb). 

For more information, contact [Nick Timpano](mailto:nick.timpano@gmail.com)

## Repo Structure 

```
├── pictures/
├── reviews/
├── quits.csv
├── investment_links.csv
├── README.md
├── glassdoor_review_scraper.ipnyb
└── investment_reviews_analysis.ipynb
```