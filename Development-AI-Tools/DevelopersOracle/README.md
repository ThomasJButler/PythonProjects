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

1. Navigate to the DevelopersOracle directory
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download spaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Configuration

⚠️ **IMPORTANT SECURITY NOTE**: The `config.json` file contains sensitive API keys and is included in `.gitignore` to prevent accidental commits.

1. Copy the template configuration:
   ```bash
   cp config.json.template config.json
   ```

2. Edit `config.json` with your actual API keys and configuration:

```json
{
    "openai_api_key": "YOUR_OPENAI_API_KEY_HERE",
    "jira_url": "https://your-domain.atlassian.net",
    "jira_username": "your-jira-email@example.com",
    "jira_api_token": "YOUR_JIRA_API_TOKEN_HERE",
    "github_token": "YOUR_GITHUB_PERSONAL_ACCESS_TOKEN_HERE",
    "gitlab_url": "https://gitlab.com",
    "gitlab_token": "YOUR_GITLAB_PERSONAL_ACCESS_TOKEN_HERE",
    "bitbucket_username": "your-bitbucket-username",
    "bitbucket_app_password": "YOUR_BITBUCKET_APP_PASSWORD_HERE",
    "local_repo_path": "/path/to/your/local/repository"
}
```

### Getting API Keys

- **OpenAI**: Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
- **GitHub**: Create a Personal Access Token in [GitHub Settings](https://github.com/settings/tokens)
- **GitLab**: Generate a Personal Access Token in [GitLab Settings](https://gitlab.com/-/profile/personal_access_tokens)
- **JIRA**: Create an API token in [Atlassian Account Settings](https://id.atlassian.com/manage-profile/security/api-tokens)
- **Bitbucket**: Create an App Password in [Bitbucket Settings](https://bitbucket.org/account/settings/app-passwords/)

## Usage

Run from the repository root:

```bash
python Development-AI-Tools/DevelopersOracle/DevelopersOracle.py
```

### Key Methods

- `summarize_code(timeframe=None)`: Generate code summaries from Git commits
- `generate_commit_message(diff)`: AI-generated commit messages
- `analyze_jira_ticket(ticket_id)`: Analyze JIRA tickets and generate development plans
- `recommend_reply(message)`: Get AI recommendations for message replies

## File Structure

```
DevelopersOracle/
├── DevelopersOracle.py          # Main application
├── config.json.template         # Configuration template
├── requirements.txt             # Dependencies
├── README.md                    # This documentation
└── DevelopersOracle.ipynb      # Interactive demo notebook
```

## Dependencies

See `requirements.txt` for complete list:
- Core: openai, numpy, scikit-learn
- NLP: spacy, transformers
- Version Control: GitPython, pydriller
- Platforms: jira, PyGithub, python-gitlab
- GUI: PyQt5
- Visualization: matplotlib, seaborn

## Status

🚧 **Under Development**: This project contains many placeholder functions that need implementation. The configuration template and documentation are now complete, but core ML and integration features require further development.

## Security

- All sensitive configuration is excluded from version control
- API keys should never be hardcoded in source files
- Use environment variables or secure secrets management for production