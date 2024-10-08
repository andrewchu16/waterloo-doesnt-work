SUMMARY_PROMPT = """
Given a description of a job opening, summarize all the key information in the format below in separate lines:

companyName: string
jobTitle: string
description: string
location: string
pay: int

{insert}
"""

IMAGE_PROMPT = """
Given the summary of a job, generate an image of two employees of this company working on the job.

CompanyName: {name}
JobTitle: {title}
Description: {description}
"""