import requests
import json

from openai import OpenAI
from secret import API_KEY, ORGANIZATION_ID
from const import SUMMARY_PROMPT, IMAGE_PROMPT
from bs4 import BeautifulSoup
from random import randint


client = OpenAI(
    api_key = API_KEY,
    organization = ORGANIZATION_ID
)


class Catalogue:


    def __init__(self):

        self.data = dict()
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
        self.data[url] = {
            "ID": str(new_id),
            "ApplicationURL": url
        }

        content = response.choices[0].message.content.split('\n')
        
        for line in content:
            header, body = line.split(' ', 1)
            print(header + " HEY " + body)
            self.data[url][header[:len(header)-1]] = body

        image_prompt = IMAGE_PROMPT
        image_prompt = image_prompt.replace('{name}', self.data[url]['CompanyName'])
        image_prompt = image_prompt.replace('{title}', self.data[url]["JobTitle"])
        image_prompt = image_prompt.replace('{description}', self.data[url]['Description'])

        response = client.images.generate(
            model = "dall-e-3",
            prompt = image_prompt,
            size = "1024x1024",
            n = 1,
        )

        self.data[url]['Picture'] = response.data[0].url
        self.dump()
        
    

    def read_catalogue(self):

        with open('jobList.txt', 'r') as f:
            lines = f.read().split()

            for nxt in lines:
                url = nxt.rstrip('\n')

                if url not in self.data:
                    self.add_job(url)
    

    def test(self):

        for nxt in self.data:

            print(nxt, self.data[nxt])


c = Catalogue()
