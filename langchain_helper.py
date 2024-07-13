from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
import ast

from dotenv import load_dotenv

load_dotenv()

# Make sure to set your OpenAI API key in your environment variables
# os.environ["OPENAI_API_KEY"] = "your-api-key-here"

def generate_word_info(word):
    llm = OpenAI(temperature=0.7)
    
    prompt_template = PromptTemplate(
        input_variables=["word"],
        template=
        """Provide the pronunciation, meaning and real-life example sentence for the word '{word}'.\n Return your response as JSON format below. \n [Example]\npronunciation: "pronunciation of the word in IPA"\nmeaning: "meaning of the word"\nsentences: "real-life example of the word" """
    )
    
    chain = LLMChain(llm=llm, prompt=prompt_template)
    
    response = chain.run(word)
    
 # Try to parse the response as a dictionary
    try:
        result = ast.literal_eval(response)
        # Ensure all expected keys are present
        result = {
            "pronunciation": result.get("pronunciation", ""),
            "meaning": result.get("meaning", ""),
            "sentences": result.get("sentences", [])
        }
        return result
    except:
        # If parsing fails, return a dictionary with empty values
        return {
            "pronunciation": "",
            "meaning": "",
            "sentences": []
        }
        return {"error": "Failed to generate word information"}