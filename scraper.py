import requests
import json

api_url = 'https://www.page2api.com/api/v1/scrape'
payload = {
  "api_key": "7edeaff2611052d88b393cdaa514d523cc9c8c69",
  "url": "https://www.glassdoor.com/Reviews/Glassdoor-Reviews-E100431.htm",
  "real_browser": True,
  "merge_loops": True,
  "premium_proxy": "us",
  "scenario": [
    {
      "loop": [
        { "wait_for": "div.gdReview" },
        { "execute": "parse" },
        { "execute_js": "document.querySelector(\".nextButton\").click()" }
      ],
      "iterations": 2
    }
  ],
  "parse": {
    "reviews": [
      {
        "_parent": "div.gdReview",
        "title": "a.reviewLink >> text",
        "author_info": ".authorInfo >> text",
        "rating": "span.ratingNumber >> text",
        "pros": "span[data-test=pros] >> text",
        "cons": "span[data-test=cons] >> text",
        "helpful": "div.common__EiReviewDetailsStyle__socialHelpfulcontainer >> text"
      }
    ]
  }
}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.post(api_url, data=json.dumps(payload), headers=headers)
result = json.loads(response.text)

print(result)
