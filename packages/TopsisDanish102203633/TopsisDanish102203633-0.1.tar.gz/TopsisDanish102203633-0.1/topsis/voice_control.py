import pandas as pd
import os
import speech_recognition as sr
from topsis import topsis
from file_upload import upload_file

class VoiceControl:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.command_history = []
        self.data = None
        self.weights = None
        self.impacts = None

    def listen_for_command(self):
        """Capture voice command."""
        with sr.Microphone() as source:
            print("Listening for command...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            command = self.recognizer.recognize_google(audio)
            self.command_history.append(command)
            print(f"Command received: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Sorry, the speech service is unavailable.")
            return None
        except Exception as e:
            print(f"Error in listening: {e}")
            return None

    def process_data_input(self):
        """Process data input via voice."""
        print("Please provide the file path for data analysis.")
        file_path = self.listen_for_command()
        if file_path and os.path.exists(file_path):
            print(f"Loading data from {file_path}...")
            self.data = self.load_data(file_path)
        else:
            print("Invalid file path provided.")

        print("Please provide the weights for TOPSIS analysis.")
        weights = self.listen_for_command()
        if weights:
            self.weights = self.process_weights(weights)

        print("Please provide the impacts for TOPSIS analysis.")
        impacts = self.listen_for_command()
        if impacts:
            self.impacts = self.process_impacts(impacts)

    def load_data(self, file_path):
        """Load the dataset from any file type."""
        try:
            # Check file extension
            file_extension = file_path.split('.')[-1].lower()

            if file_extension == 'csv':
                return pd.read_csv(file_path)
            elif file_extension in ['xls', 'xlsx']:
                return pd.read_excel(file_path)
            else:
                print(f"Unsupported file type: {file_extension}")
                return None
        except Exception as e:
            print(f"Error loading data: {e}")
            return None

    def process_weights(self, weights):
        """Process weights from voice input."""
        try:
            weight_list = list(map(float, weights.split(',')))
            return weight_list
        except ValueError:
            print("Invalid weight format. Please provide a comma-separated list of numbers.")
            return None

    def process_impacts(self, impacts):
        """Process impacts from voice input."""
        return impacts.split(',')

    def execute_command(self, command):
        """Execute corresponding actions based on the voice command."""
        if 'start topsis' in command:
            print("Starting TOPSIS analysis...")
            self.process_data_input()
            if self.data is not None and self.weights is not None and self.impacts is not None:
                topsis(self.data, self.weights, self.impacts)
            else:
                print("Missing data, weights, or impacts.")
        elif 'upload file' in command:
            print("Please upload the file.")
            self.upload_file_process()
        elif 'exit' in command:
            print("Exiting the application.")
            return False
        elif 'help' in command:
            print("Commands: start topsis, upload file, exit, help")
        else:
            print(f"Command '{command}' not recognized.")
        return True

    def upload_file_process(self):
        """Handle file upload via voice."""
        print("Please provide the file path to upload.")
        file_path = self.listen_for_command()
        if file_path and os.path.exists(file_path):
            upload_file(file_path)
        else:
            print("File not found.")

    def run(self):
        """Run voice control loop."""
        while True:
            command = self.listen_for_command()
            if command:
                should_continue = self.execute_command(command)
                if not should_continue:
                    break
