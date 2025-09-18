import os
import sys
import time
import datetime
import json
import re
import requests
import openai
import numpy as np
from git import Repo
from jira import JIRA
from github import Github
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import spacy
import gitlab
from bitbucket_api import BitbucketApi
import subprocess
from pydriller import Repository
from transformers import pipeline

class DevelopersOracle:
    def __init__(self):
        self.time_tracker = {}
        self.load_config()
        self.setup_connections()
        self.setup_ml_models()
        self.nlp = spacy.load("en_core_web_sm")
        self.sentiment_analyzer = pipeline("sentiment-analysis")

    def load_config(self):
        with open('config.json', 'r') as f:
            self.config = json.load(f)
        openai.api_key = self.config['openai_api_key']

    def setup_connections(self):
        self.jira = JIRA(server=self.config['jira_url'], basic_auth=(self.config['jira_username'], self.config['jira_api_token']))
        self.github = Github(self.config['github_token'])
        self.gitlab = gitlab.Gitlab(self.config['gitlab_url'], private_token=self.config['gitlab_token'])
        self.bitbucket = BitbucketApi(self.config['bitbucket_username'], self.config['bitbucket_app_password'])
        self.repo = Repo(self.config['local_repo_path'])

    def setup_ml_models(self):
        # Initialize and train ML models for estimation
        self.estimation_model = RandomForestRegressor(n_estimators=100, random_state=42)
        # Load historical data and train the model
        # This is a placeholder - you'd need to implement data loading and training
        X, y = self.load_historical_data()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        self.estimation_model.fit(X_train_scaled, y_train)

    def load_historical_data(self):
        # Placeholder function to load historical data for ML model
        # In a real scenario, this would load data from your project management system
        return np.random.rand(100, 5), np.random.rand(100)

    def summarize_code(self, timeframe=None):
        if timeframe:
            end_time = datetime.datetime.now()
            start_time = end_time - datetime.timedelta(hours=timeframe)
            commits = list(self.repo.iter_commits(since=start_time.isoformat()))
        else:
            commits = list(self.repo.iter_commits(max_count=10))

        summary = "Code Summary:\n\n"
        for commit in commits:
            summary += f"Commit: {commit.hexsha}\n"
            summary += f"Author: {commit.author}\n"
            summary += f"Date: {commit.committed_datetime}\n"
            summary += f"Message: {commit.message}\n\n"

        return summary

    def generate_commit_message(self, diff):
        prompt = f"Generate a concise and informative Git commit message for the following code changes:\n\n{diff}\n\nCommit message:"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=50)
        return response.choices[0].text.strip()

    def recommend_reply(self, message):
        prompt = f"Recommend a professional and helpful reply to the following message:\n\n{message}\n\nRecommended reply:"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
        return response.choices[0].text.strip()

    def manage_notifications(self):
        # Implement notification management logic here
        pass

    def analyze_jira_ticket(self, ticket_id):
        issue = self.jira.issue(ticket_id)
        
        summary = issue.fields.summary
        description = issue.fields.description
        
        relevant_files = self.scan_codebase_for_relevance(summary, description)
        plan = self.generate_plan(summary, description, relevant_files)
        estimate = self.estimate_ticket(issue)
        
        return {
            'summary': summary,
            'description': description,
            'relevant_files': relevant_files,
            'plan': plan,
            'estimate': estimate
        }

    def scan_codebase_for_relevance(self, summary, description):
        # Use NLP to identify key terms
        doc = self.nlp(summary + " " + description)
        key_terms = [token.text for token in doc if token.pos_ in ['NOUN', 'VERB', 'ADJ']]

        relevant_files = []
        for root, dirs, files in os.walk(self.config['local_repo_path']):
            for file in files:
                if file.endswith(('.py', '.js', '.html', '.css')):  # Add more extensions as needed
                    with open(os.path.join(root, file), 'r') as f:
                        content = f.read()
                        if any(term.lower() in content.lower() for term in key_terms):
                            relevant_files.append(os.path.join(root, file))

        return relevant_files

    def generate_plan(self, summary, description, relevant_files):
        prompt = f"Generate a structured plan for the following task:\n\nSummary: {summary}\n\nDescription: {description}\n\nRelevant files: {relevant_files}\n\nPlan:"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=200)
        return response.choices[0].text.strip()

    def estimate_ticket(self, issue):
        # Extract features from the issue
        features = self.extract_features(issue)
        
        # Scale features
        scaler = StandardScaler()
        features_scaled = scaler.fit_transform([features])
        
        # Make prediction
        estimated_time = self.estimation_model.predict(features_scaled)[0]
        
        return estimated_time

    def extract_features(self, issue):
        # Extract relevant features from the issue
        # This is a placeholder - you'd need to implement feature extraction based on your specific needs
        return [
            len(issue.fields.summary),
            len(issue.fields.description) if issue.fields.description else 0,
            len(issue.fields.components),
            issue.fields.priority.id,
            issue.fields.issuetype.id
        ]

    def generate_client_update(self, progress):
        prompt = f"Generate a professional client update based on the following progress:\n\n{progress}\n\nClient update:"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=150)
        return response.choices[0].text.strip()

    def document_task(self, task_description, implementation_details):
        prompt = f"Generate a detailed documentation for the following task and implementation:\n\nTask: {task_description}\n\nImplementation: {implementation_details}\n\nDocumentation:"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=300)
        return response.choices[0].text.strip()

    def generate_code_comments(self, code):
        prompt = f"Generate clear and concise comments for the following code:\n\n{code}\n\nCommented code:"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=300)
        return response.choices[0].text.strip()

    def auto_reply_when_busy(self, sender):
        return f"Hi {sender}, I've seen your message and will get back to you soon. Thank you for your patience!"

    def track_time(self, task, duration):
        if task in self.time_tracker:
            self.time_tracker[task] += duration
        else:
            self.time_tracker[task] = duration

    def generate_time_chart(self):
        tasks = list(self.time_tracker.keys())
        times = list(self.time_tracker.values())

        plt.figure(figsize=(10, 5))
        plt.bar(tasks, times)
        plt.title('Time Spent on Tasks')
        plt.xlabel('Tasks')
        plt.ylabel('Time (hours)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('time_chart.png')
        plt.close()

    def suggest_code_improvements(self, code):
        prompt = f"Suggest improvements and refactoring for the following code:\n\n{code}\n\nSuggestions:"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=200)
        return response.choices[0].text.strip()

    def generate_documentation(self, code):
        prompt = f"Generate comprehensive documentation for the following code:\n\n{code}\n\nDocumentation:"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=300)
        return response.choices[0].text.strip()

    def predict_potential_issues(self, code):
        prompt = f"Analyze the following code and predict potential issues or bugs:\n\n{code}\n\nPotential issues:"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=200)
        return response.choices[0].text.strip()

    def integrate_with_ide(self, ide):
        # This is a placeholder for IDE integration
        # In reality, this would involve creating plugins or extensions for specific IDEs
        if ide.lower() == 'vscode':
            print("Integrating with Visual Studio Code...")
            # Implement VS Code extension logic
        elif ide.lower() == 'pycharm':
            print("Integrating with PyCharm...")
            # Implement PyCharm plugin logic
        else:
            print(f"Integration with {ide} is not yet supported.")

    def analyze_code_sentiment(self, code_review_comments):
        sentiments = self.sentiment_analyzer(code_review_comments)
        return sentiments

    def suggest_pair_programming(self, developer1, developer2):
        # This is a placeholder for pair programming suggestions
        # In a real scenario, this would analyze developers' skills and current tasks
        return f"Suggested pair programming session for {developer1} and {developer2} on Task X"

class OracleGUI(QWidget):
    def __init__(self, oracle):
        super().__init__()
        self.oracle = oracle
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.input_box = QTextEdit()
        layout.addWidget(self.input_box)

        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        layout.addWidget(self.output_box)

        self.run_button = QPushButton('Run Oracle')
        self.run_button.clicked.connect(self.run_oracle)
        layout.addWidget(self.run_button)

        self.setLayout(layout)
        self.setWindowTitle('DevelopersOracle')
        self.show()

    def run_oracle(self):
        input_text = self.input_box.toPlainText()
        # Implement logic to parse input and call appropriate Oracle methods
        # Display results in self.output_box

if __name__ == "__main__":
    oracle = DevelopersOracle()
    app = QApplication(sys.argv)
    gui = OracleGUI(oracle)
    sys.exit(app.exec_())