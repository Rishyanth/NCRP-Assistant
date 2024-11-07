from llama_index.llms.gemini import Gemini
from llama_index.core import PromptTemplate
from llama_index.core.query_pipeline import QueryPipeline
import os
from dotenv import load_dotenv
from logger import customlogging as log
import json


# Load the .env file
load_dotenv()
# Access the variables
api_key = os.getenv('GOOGLE_API_KEY')

class Suggestions_model:
    def __init__(self):
        try:
            self.llm_model = Gemini(api_key=api_key,model_name="models/gemini-1.5-pro")
            log.info("Gemini Model Initialized Successfully")
        except:
            log.info("Gemini Model Initialization Failed")
    def get_suggestions(self,user_input):
        prompt="""
        You are front end officer of Cyber crime division you have to analyse this complaint
        {complaint}  and provide short suggestions to improve the complaints The suggestions 
        should be consice and should be exactly two lines make sure the user has mentioned
        the date of the incident else it should be reminded to the user
        and the output should be in json format
        """
        prompt_tmpl = PromptTemplate(prompt)
        pipe = QueryPipeline(chain=[prompt_tmpl, self.llm_model], verbose=True)
        log.info("QueryPipline Created Starting Prediction using Gemini API")
        response=pipe.run(complaint=user_input)
        log.info("Prediction using Gemini API completed outputing response")
        response=response.message.content
        response=response.replace("```json","")
        response=response.replace("```","")
        return json.loads(response)
    
