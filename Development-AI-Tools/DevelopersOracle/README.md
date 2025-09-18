# DevelopersOracle

An AI-powered developer assistant that integrates with multiple platforms to enhance development productivity. This tool provides intelligent code analysis, project management assistance, and automated development workflows.

## Features

- **Multi-Platform Integration**: Connect to GitHub, GitLab, Bitbucket, and JIRA
- **AI-Powered Code Analysis**: Generate commit messages and code summaries using OpenAI
- **Project Management**: Analyze JIRA tickets and generate development plans
- **Time Tracking**: Built-in time tracking for development tasks
- **Sentiment Analysis**: Analyze project communications using NLP
- **Machine Learning**: Task estimation using Random Forest models
- **GUI Interface**: PyQt5-based graphical user interface

## Prerequisites

- Python 3.8+
- OpenAI API key
- Platform-specific API tokens (GitHub, GitLab, Bitbucket, JIRA)
- spaCy English model: `python -m spacy download en_core_web_sm`

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install openai numpy GitPython jira3 PyGithub python-gitlab bitbucket-api matplotlib PyQt5 scikit-learn spacy pydriller transformers
   ```
3. Download spaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Configuration

Create a `config.json` file in the project directory:

```json
{
    "openai_api_key": "your_openai_api_key",
    "jira_url": "https://your-domain.atlassian.net",
    "jira_username": "your_username",
    "jira_api_token": "your_jira_token",
    "github_token": "your_github_token",
    "gitlab_url": "https://gitlab.com",
    "gitlab_token": "your_gitlab_token",
    "bitbucket_username": "your_username",
    "bitbucket_app_password": "your_app_password",
    "local_repo_path": "/path/to/your/repo"
}
```

## Usage

```bash
python DevelopersOracle.py
```

### Key Methods

- `summarize_code(timeframe=None)`: Generate code summaries from Git commits
- `generate_commit_message(diff)`: AI-generated commit messages
- `analyze_jira_ticket(ticket_id)`: Analyze JIRA tickets and generate development plans
- `recommend_reply(message)`: Get AI recommendations for message replies

## Dependencies

- openai
- numpy
- GitPython
- jira3
- PyGithub
- python-gitlab
- bitbucket-api
- matplotlib
- PyQt5
- scikit-learn
- spacy
- pydriller
- transformers

## Status

This project is under active development. Some features may require additional configuration or implementation.