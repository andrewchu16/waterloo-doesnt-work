from flask import Flask, request
from flask_cors import CORS
import json

from server import Server

app = Flask(__name__)
CORS(app)

server = Server()

if __name__ == '__main__':
    app.run()


@app.route("/get_job", methods=["GET"])
def get_job():
    """
        View information about the user's job preferences

        Request:
        {
            "id": "123456"
            user: {
                "name": "aaaa"
                "email": "aaaaa"
                "ethnicity": ["Asian"]
                "resumeSummary": "Here is the summary haha"
                "education": "uWaterloo"
                "graduationYear": "2024"
                "seasonAvailable": “winter 2025” | “summer 2025” | “fall 2025” | “spring 2025”;
            }
            activity:{
                {
                    "Liked Jobs": ["idk what to put here"];
                    "Disliked Jobs": ["here too"];
                }
            }
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
    #id = request.form.get("id")
    #user = request.form.get("user")
    #activity = request.form.get("activity")
    return server.get_job()

@app.route("/summarize_resume", methods=["GET"])
def summarize_resume():
    """
    Summarizes user resume

    Request:
    {
        "Resume": file, pdf, 
    }
    Response:
    {
        "Summary": idk what to put here
    }
    """
    #resume = server.add_resume(request.data)
    #summary = summarize(f"{resume}")

    return {} #summary