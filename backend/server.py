from threading import Thread
from catologue import Catologue

import json


def format_response(info: dict, status: int):

    response = Response(
        response = json.dumps(info),
        status = status,
        mimetype = "application/json"
    )

    response.status_code = status
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


class Server:


    def __init__(self) -> None:

        self.jobs = Catologue()

        # Don't need this just yet ...
        '''
        try:
            print("Loading jobs.json...")
            with open("jobs.json", "r") as d:
                self.data = json.load(d)
                print("jobs.json loaded")
                print("self.data")
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            print("Hello, World!")
            self.setup()
        # Start update loop
        Thread(target=self.update_loop).start()
        '''

    def get_job(self, user_json, job_pref_json):
        """
        View information about the job listing

        Request:
        {
            "id": "123456"
        }
        Response:
        {
            job
            {
                "companyName": "Apple",
                "jobTitle": "Developer",
                "ID": "123456",
                "Picture": png, jpg, or jpeg image,
                "Description": "Develope Apple",
                "Location":
                [
                    "San Francisco, California"
                    "Toronto, Ontario"
                ],
                "Pay": 15,
                "Questions": 
                [
                    "How old are you?"
                ],
                "applicationUrl": "apple.com"
            },
            status: "success"
        }
        """
        # Get job
        return format_response(self.jobs.get_random_job(), 200)