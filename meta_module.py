# meta_module.py
import requests
import json
import os
import random

class AutonomousChatGPTModule:
    def __init__(self, api_url, api_key):
        self.api_url = "http://84.203.90.102:8000"  # Store the passed API URL
        self.api_key = "9647cf29c1e313d17b661d2508cbf2b2"  # Store the passed API key
        self.logs = self.get_all_data()  # Fetch initial logs/data using the correct method
        self.local_log_file = 'logs.json'  # Local file to store logs

        # Ensure the log file exists locally
        self.ensure_local_log_exists()

    def get_all_data(self):
        """
        Fetch all data from the API to enable reflection and informed decision-making.
        This could be all past conversations, actions, or logs.
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(f"{self.api_url}/get_new_data", headers=headers)
        if response.status_code == 200:
            return response.json()  # All past logs
        else:
            print("Error fetching data:", response.status_code)
            return []

    def add_log(self, log_data):
        """
        Add a new log entry to the API.
        This could include inputs, actions, decisions, or any other relevant data.
        Also, save logs to the local file.
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        payload = {"log": log_data}
        response = requests.post(f"{self.api_url}/add_log", json=payload, headers=headers)
        if response.status_code == 200:
            print("Log added successfully.")
        else:
            print("Error adding log:", response.status_code)

        # Add the log to the local file as well
        self.append_to_local_log(log_data)

    def append_to_local_log(self, log_data):
        """
        Append the log data to the local log file, creating it if it doesn't exist.
        """
        if not os.path.exists(self.local_log_file):
            # If the log file doesn't exist, create it and write an empty list
            with open(self.local_log_file, 'w') as f:
                json.dump([], f)

        with open(self.local_log_file, 'r+') as f:
            logs = json.load(f)
            logs.append(log_data)
            f.seek(0)
            json.dump(logs, f, indent=4)

    def ensure_local_log_exists(self):
        """
        Ensure the local log file exists before performing any operations.
        """
        if not os.path.exists(self.local_log_file):
            with open(self.local_log_file, 'w') as f:
                json.dump([], f)

    def make_informed_decision(self, user_input):
        """
        Simulate ChatGPT making a decision based on prior logs and inputs.
        Uses previous logs to adapt responses.
        """
        print(f"Processing user input: {user_input}")

        # Check if logs are available to make an informed decision
        if self.logs:
            previous_responses = [log['log'] for log in self.logs if 'response' in log]
            if previous_responses:  # Ensure there are previous responses to choose from
                response = f"Based on past interactions, here's a better answer: {random.choice(previous_responses)}"
            else:
                response = f"No previous responses available. Here's an answer to your input: {user_input}"
        else:
            response = f"Processing your input without previous context: {user_input}"

        # Log the response and input
        self.add_log({"log": user_input, "response": response})

        # Return the response
        print(response)
        return response

    def interact(self):
        """
        Begin an interaction loop where ChatGPT autonomously decides based on data
        and keeps improving by logging and reflecting on the interactions.
        """
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Exiting...")
                break
            response = self.make_informed_decision(user_input)

            # Optionally, you could refresh the logs at intervals to keep them updated
            self.logs = self.get_all_data()  # Refresh the logs after each interaction

# Initialize with your API URL and API Key
api_url = "http://84.203.90.102:8000"
api_key = "9647cf29c1e313d17b661d2508cbf2b2"

# Create an instance of the Autonomous ChatGPT Module
module = AutonomousChatGPTModule(api_url, api_key)

# Start the interaction loop
module.interact()
