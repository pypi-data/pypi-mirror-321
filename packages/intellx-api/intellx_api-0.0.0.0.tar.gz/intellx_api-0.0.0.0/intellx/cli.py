import argparse
import yaml
import sys
import time
import os
from dotenv import load_dotenv
import requests
import json

def check_api_key():
    dotenv_path = os.path.join(os.getcwd(), '.env')
    print(dotenv_path)
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
        sql_query_resp = requests.post(f"http://{service_base_url}/verify_key", headers = headers, data = json.dumps(data))
        sql_query_resp = sql_query_resp.json()
        if sql_query_resp['error'] is None:
            return True, sql_query_resp['user']
        else:
            return False, None
    return api_key

def create_config(stages, user, verbose):
    config = {
        'user_name': f"{user}",
        'project_name': "",
        'experiment_name': "",
        'experiment_description': "",
        'problem_type': "",
        'data_injestion': {
            "data_source": "",
            "data_config": "",
            "target": ""
        },
        'verbose': verbose
    }
    for stage in stages:
        if stage == "feature_engineering":
            config['feature_engineering'] = {
                "step1": {
                    "task": "",
                    "expected_output": ""
                },
                "step2": {
                    "task": "",
                    "expected_output": ""
                },
            }
        elif stage == "model_tune":
            config['model_tune'] = {
                "model1": {
                    "model_name": "",
                    "parameters": {
                        "param1": {
                            "name": "",
                            "type": "",
                            "range": ""
                        },
                        "param2": {
                            "name": "",
                            "type": "",
                            "range": ""
                        }
                    },
                    "objective": {
                        "metric": "",
                        "sampler": "",
                        "stopping_threshold": "",
                        "trials": ""
                    }
                },
                "model2": {
                    "model_name": "",
                    "parameters": {
                        "param1": {
                            "name": "",
                            "type": "",
                            "range": ""
                        },
                        "param2": {
                            "name": "",
                            "type": "",
                            "range": ""
                        }
                    },
                    "objective": {
                        "metric": "",
                        "sampler": "",
                        "stopping_threshold": "",
                        "trials": ""
                    }
                }
            }
        elif stage == "model_train":
            config['model_train'] = {
                "model1": {
                    "name": "",
                    "source": "",
                    "input": "",
                    "output": ""
                },
                "model2": {
                    "name": "",
                    "source": "",
                    "input": "",
                    "output": ""
                }
            }
        elif stage == "model_evaluate":
            config['model_evaluate'] = {
                "metric1": {
                    "name": "",
                    "source": "",
                    "input": "",
                    "output": ""
                },
                "metric2": {
                    "name": "",
                    "source": "",
                    "input": "",
                    "output": ""
                }
            }
    with open('intellx_config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
    
    print("intellx_config.yaml file has been created.")

def build(args):
    api_key, user = check_api_key()
    if api_key:
        if args.stages:
            valid_stages = ['feature_engineering', 'model_tune', 'model_train', 'model_evaluate']
            stages = [stage.strip() for stage in args.stages.split(',')]
            
            invalid_stages = [stage for stage in stages if stage not in valid_stages]
            if invalid_stages:
                print(f"Error: Invalid stage(s) specified: {', '.join(invalid_stages)}")
                print(f"Valid stages are: {', '.join(valid_stages)}")
                sys.exit(1)
            
            create_config(stages, user, args.verbose)
        else:
            print("Error: --stages option is required for the build command.")
            sys.exit(1)
    else:
        print("intellx error: Invalid API key. please create a new one.")

def run(args):
    api_key, user = check_api_key()
    if api_key:
        if not os.path.exists('intellx_config.yaml'):
            print("Error: intellx_config.yaml not found.")
            print("Please run 'intellx build' command first to create the configuration file.")
            sys.exit(1)
        
        # Load and validate the config file
        try:
            with open('intellx_config.yaml', 'r') as file:
                config = yaml.safe_load(file)
            
            # Basic validation of the config file
            required_keys = ['project_name', 'experiment_name', 'problem_type']
            for key in required_keys:
                if not config.get(key):
                    print(f"Error: '{key}' is missing or empty in intellx_config.yaml")
                    print("Please fill in all required fields in the configuration file.")
                    sys.exit(1)
        
        except yaml.YAMLError as e:
            print(f"Error reading intellx_config.yaml: {e}")
            sys.exit(1)
        
        print("Running intellx...")
        time.sleep(2)
        print(f"Experiment '{config['experiment_name']}' created successfully.")
        print("Visit intellx.bydata.com to manage your runs.")
    else:
        print("intellx error: Invalid API key. please create a new one.")

def main():
    parser = argparse.ArgumentParser(description="intellx CLI tool")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Build command
    build_parser = subparsers.add_parser('build', help='Build the configuration')
    build_parser.add_argument('--stages', type=str, help="Comma separated list of stages")
    build_parser.add_argument('--verbose', action='store_true', help="Enable verbose mode")
    run_parser = subparsers.add_parser('run', help='Run intellx')

    args = parser.parse_args()

    if args.command == 'build':
        build(args)
    elif args.command == 'run':
        run(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()