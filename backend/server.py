from threading import Thread

import json

class Server:
    def __init__(self) -> None:
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

    def get_job(self, id: str):
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
        if id not in self.data:
            return format_response({"status": "error", "message": "Job not found"}, 404)
        # idk return something