#!/usr/bin/env python
import requests
import bs4
import json
import re

all_lines = []
currently_scraping_count = 0

#################################### THIS IS THE REQUEST PART
url_to_scrape = "http://www.gutenberg.org/cache/epub/18362/pg18362.html"
our_request = requests.get(url_to_scrape)
print "requested page sent response code: %s" % our_request.status_code

#################################### THIS IS THE PARSING PART
parsed_html = bs4.BeautifulSoup(our_request.text, 'html.parser')
all_results = parsed_html.find_all('p', id=re.compile("id\d+"))

ids = [t['id'] for t in all_results]

initial = ids.index('id00082')
final = ids.index('id15977')

out = [t.text for t in all_results[initial:final+1]]

#go through all the elements in the list and print them one by one
for result in out:
    for line in result.split('\r\n'):
        if line !="":
            currently_scraping_count += 1
            if currently_scraping_count % 100 == 0:
                print "scraped line: %i/%i" % (currently_scraping_count, len(all_results))
            properly_encoded_line = line.encode('utf-8')
            all_lines.append(properly_encoded_line)


print "done scraping! writing to file..."

#################################### THIS IS THE WRITING PART
with open("all_results_2.json", 'w') as my_file:
   data_to_write = json.dumps(all_lines)
   my_file.write(data_to_write)                                                   

# with open("new_results.json", 'w') as my_file:
#     my_file.write(all_postings)
