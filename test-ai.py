import openai

openai.api_type = "azure"
openai.azure_endpoint = "https://gabriel-magalhaes-useast.openai.azure.com/"  # Substitua pelo seu endpoint do Azure
openai.api_version = "2024-05-01-preview"
openai.api_key = "61a06db77c434b2dbe2b5b7af025e73c"

deployment_name = "atividadeGPT"


chat_prompt = [
{
    "role": "system",
    "content": "Responda ás perguntas de forma clara"
}
]  

speech_result = chat_prompt  

response = openai.chat.completions.create(
    model=deployment_name,
    messages=speech_result,  
    max_tokens=10
)

print(response.to_json())  
    