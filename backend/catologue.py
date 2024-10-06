from openai import OpenAI
from secret import API_KEY, ORGANIZATION_ID
from const import SUMMARY_PROMPT, IMAGE_PROMPT
from bs4 import BeautifulSoup
from random import randint, shuffle

import requests
import json


client = OpenAI(
    api_key = API_KEY,
    organization = ORGANIZATION_ID
)


class Catologue:


    def __init__(self):

        self.data = {
            "jobs": []
        }
        self.visited_jobs = list()
        self.load()
        self.read_catalogue()
    

    def load(self):

        with open('jobs.json', 'r') as f:
            
            data = f.read()
            if len(data) != 0:
                self.data = json.loads(data) 


    def dump(self):

        with open('jobs.json', 'w') as f:
            json.dump(self.data, f)


    def add_job(self, url):
        
        print("ADDING NEW JOB")
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        text = soup.body.get_text(' ', strip=True)

        response = client.chat.completions.create(
            model = 'gpt-4o-mini',
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": SUMMARY_PROMPT.replace('{insert}', text)
                        }
                    ]
                }
            ]
        )

        new_id = randint(1, 1000000)
        self.data["jobs"].append({
            "ID": str(new_id),
            "applicationURL": url
        })

        content = response.choices[0].message.content.split('\n')
        
        for line in content:
            header, body = line.split(' ', 1)
            self.data["jobs"][-1][header[:len(header)-1]] = body.rstrip()

        image_prompt = IMAGE_PROMPT
        image_prompt = image_prompt.replace('{name}', self.data["jobs"][-1]['companyName'])
        image_prompt = image_prompt.replace('{title}', self.data["jobs"][-1]["jobTitle"])
        image_prompt = image_prompt.replace('{description}', self.data["jobs"][-1]['description'])

        response = client.images.generate(
            model = "dall-e-3",
            prompt = image_prompt,
            size = "1024x1024",
            n = 1,
        )

        self.data["jobs"][-1]['picture'] = response.data[0].url
        self.dump()
        
    

    def read_catalogue(self):

        with open('jobList.txt', 'r') as f:
            lines = f.read().split()

            for nxt in lines:
                url = nxt.rstrip('\n')

                job_found = False
                for job in self.data["jobs"]:

                    if job["applicationURL"] == url:
                        job_found = True
                
                if not job_found:
                    self.add_job(url)
    

    def get_random_job(self):
        
        pool = []
        for nxt in self.data["jobs"]:
            if nxt["applicationURL"] not in self.visited_jobs:
                pool.append(nxt)

        if len(pool) == 0:
            self.visited_jobs = list()
            return self.get_random_job()
        
        shuffle(pool)
        self.visited_jobs.append(pool[0]["applicationURL"])
        return pool[0]