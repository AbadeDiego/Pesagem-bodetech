import json
import easyocr
import os

model_dir = os.getenv('MODEL_DIR', "/mnt/ml/models/")
network_dir = os.getenv('NETWORK_DIR', "/mnt/ml/network/")

model_cache = {}

def lambda_handler(event, context):

    body = json.loads(event['body'])
    
    language_list = [lang.strip() for lang in body["language"].split(",")]
    
    languages_key = '_'.join(language_list)
    if languages_key not in model_cache:
        model_cache[languages_key] = easyocr.Reader(language_list, model_storage_directory=model_dir, user_network_directory=network_dir, gpu=False, download_enabled=False)        
    reader = model_cache[languages_key]   
    results = reader.readtext(body["link"])
    
    response = [result[1] for result in results]
    response = " ".join(response)
        
    # Function Return 
    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                "peso": response,
            }
        )
    }
