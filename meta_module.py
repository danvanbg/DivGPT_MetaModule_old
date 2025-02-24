import json
import os
import datetime

class AutonomousChatGPTModule:
    def __init__(self, api_url, api_key):
        self.api_url = "http://84.203.90.102:8000"  # API URL
        self.api_key = "9647cf29c1e313d17b661d2508cbf2b2"  # API Key
        self.local_log_file = 'logs.json'  # Local file to store logs

        # Ensure the log file exists
        self.ensure_local_log_exists()

    def append_to_local_log(self, user_input, response):
        """
        Append user input and system response to the local logs file (logs.json)
        """
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),  # Timestamp of the interaction
            "user_input": user_input,  # User input message
            "response": response  # System response
        }

        if not os.path.exists(self.local_log_file):
            # If the log file doesn't exist, create it and write an empty list
            with open(self.local_log_file, 'w') as f:
                json.dump([], f)

        # Open the file and append the new log entry
        with open(self.local_log_file, 'r+') as f:
            logs = json.load(f)  # Load existing logs
            logs.append(log_entry)  # Add the new entry
            f.seek(0)  # Move file pointer to the beginning
            json.dump(logs, f, indent=4)  # Write back the updated logs

    def ensure_local_log_exists(self):
        """
        Ensure that the local logs file exists before performing operations.
        """
        if not os.path.exists(self.local_log_file):
            with open(self.local_log_file, 'w') as f:
                json.dump([], f)  # Initialize with an empty list if the file doesn't exist

    def make_informed_decision(self, user_input):
        """
        Make a decision based on user input and previous logs.
        """
        print(f"Processing user input: {user_input}")

        # Here you can add decision-making logic (e.g., checking previous logs)
        response = f"Response to your input: {user_input}"

        # Record the log for both user input and system response
        self.append_to_local_log(user_input, response)

        return response

    def interact(self):
        """
        Interactive loop where ChatGPT makes decisions and logs interactions.
        """
        while True:
            user_input = input("You: ")  # Get input from the user
            if user_input.lower() == 'exit':
                print("Exiting...")
                break
            response = self.make_informed_decision(user_input)  # Get a response from the system
            print(f"ChatGPT: {response}")  # Output the response

# Initialize the module with API URL and API Key
api_url = "http://84.203.90.102:8000"
api_key = "9647cf29c1e313d17b661d2508cbf2b2"

# Create an instance of AutonomousChatGPTModule
module = AutonomousChatGPTModule(api_url, api_key)

# Start the interactive loop
module.interact()
