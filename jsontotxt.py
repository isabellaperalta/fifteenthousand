#!/usr/bin/env python

import json

input_file = "all_results_2.json"

with open(input_file, 'r') as my_file:
    retrieved_postings = json.load(my_file)
    with open("full_poem.txt", 'w') as my_poem:
        for posting in retrieved_postings:
            my_poem.write(posting.encode('utf-8') + '\n')  
