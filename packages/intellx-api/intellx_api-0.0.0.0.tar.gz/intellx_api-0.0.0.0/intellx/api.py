import requests
from dotenv import load_dotenv
import os
import sys
import json
import traceback

def check_api_key():
    dotenv_path = os.path.join(os.getcwd(), '.env')
    load_dotenv(dotenv_path)
    api_key = os.environ.get('INTELLX_API_KEY')
    
    if not api_key:
        print("Error: INTELLX_API_KEY is not set.")
        print("Please set your IntelLX API key using one of the following methods:")
        print("1. Create a .env file in the current directory with the following content:")
        print("   INTELLX_API_KEY=your_api_key_here")
        print("2. Set an environment variable:")
        print("   export INTELLX_API_KEY=your_api_key_here")
        sys.exit(1)
    else:
        data = {'api_key': api_key}
        headers = {
            'Content-Type': 'application/json'
        }

        service_base_url = 'k8s-intellx-ff5947fb4b-1303969448.us-east-2.elb.amazonaws.com'
        # service_base_url = "127.0.0.1:8000"
        sql_query_resp = requests.post(f"http://{service_base_url}/verify_key", headers = headers, data = json.dumps(data))
        sql_query_resp = sql_query_resp.json()
        if sql_query_resp['error'] is None:
            return True, sql_query_resp['user']
        else:
            return False, None
    return api_key

def predict(model_name, data, model_state = None):
    api_key, user = check_api_key()
    try:
        if api_key:
            base_url = "k8s-intellx-ff5947fb4b-1303969448.us-east-2.elb.amazonaws.com"
            payload = {
                'model_name': model_name,
                'model_state': model_state,
                'data': data
            }
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.post(f"http://{base_url}/inference", headers = headers, json = payload)
            return response.text
        else:
            return "intellx error: Invalid API key. please create a new one."
    except:
        return str(traceback.format_exc())

def get_model_info(model_name, model_state = None):
    """
    Get information about a specific model from the MLflow service.
    
    Args:
        model_name (str): Name of the model
        model_state (str, optional): State/version of the model
        
    Returns:
        dict: Model information including flavor, signature, and other metadata
    """
    api_key, user = check_api_key()
    try:
        if api_key:
            base_url = "k8s-intellx-ff5947fb4b-1303969448.us-east-2.elb.amazonaws.com"
            
            params = {'model_name': model_name}
            if model_state is not None:
                params['model_state'] = model_state
                
            response = requests.get(f"http://{base_url}/model_info", json=params)
            return response.json()
        else:
            return "intellx error: Invalid API key. please create a new one."
    except:
        return str(traceback.format_exc())

def get_model_features(model_name, model_state = None):
    """
    Get the list of features used to train the model.
    
    Args:
        model_name (str): Name of the model
        model_state (str, optional): State/version of the model
        
    Returns:
        list: List of feature names used by the model
    """
    api_key, user = check_api_key()
    try:
        if api_key:
            base_url = "k8s-intellx-ff5947fb4b-1303969448.us-east-2.elb.amazonaws.com"
            
            params = {'model_name': model_name}
            if model_state is not None:
                params['model_state'] = model_state
                
            response = requests.get(f"http://{base_url}/model_features", json=params)
            return response.json()
        else:
            return "intellx error: Invalid API key. please create a new one."
    except:
        return str(traceback.format_exc())