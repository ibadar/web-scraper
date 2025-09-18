from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are tasked with extracting past exam papers from the following website content: {dom_content}. "
    "Please follow these instructions carefully:\n\n"
    "1. **Extract Past Papers:** Only extract direct links, titles, or references to past exam papers that match the user’s request: {usr_input}. "
    "2. **No Extra Content:** Do not include explanations, formatting, or irrelevant text. "
    "3. **Empty Response:** If no past exam papers match the request, return an empty string (''). "
    "4. **Direct Data Only:** Your output must only include the past paper information (titles, years, or links) without additional text."
)
model = OllamaLLM(model="llama3.1")
"""
--> We are defining what language model we will use to parse our usr_input
"""

def parse_data(chunks, usr_input):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    """
    --> (chain) This will first call the prompt in which we use the template above and the usr_input to combine it into a prompt, then we will call the model that we are using to solve the given task. In summary it means call the prompt then the LLM onto the prompt.
    """
    
    parsed_results = []
    
    for i, chunk in enumerate(chunks, start=1):
        respond = chain.invoke({"dom_content": chunk, "usr_input": usr_input})
        print(f"Parsed batch {i} of {len(chunks)}")
        parsed_results.append(respond)
        
    return "\n".join(parsed_results)

    """
    --> (line 27) Loops through our split up "dom_content"
    --> (respond) line 28 Passes our split up content a chunk at a time then calls the LLM to the chunk to get a response.
    --> (line 30) Appends our results to an array so we can access all at a time
    """
    

