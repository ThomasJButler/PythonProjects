import pandas as pd
import openai

# Set up your OpenAI API key
openai.api_key = "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"

# Load the CSV data into a Pandas DataFrame
data = pd.read_csv('premier_league_data.csv')
data['date'] = pd.to_datetime(data['date'])

# Filter data to include only matches before April 20th
historical_data = data[data['date'] < '2023-04-20']

# Function to generate predictions using ChatGPT and historical data
def predict_match_outcome(team1, team2):
    # Filter historical data for the two teams
    team1_data = historical_data[(historical_data['team1'] == team1) | (historical_data['team2'] == team1)]
    team2_data = historical_data[(historical_data['team1'] == team2) | (historical_data['team2'] == team2)]

    # Generate a prompt using historical data of the two teams
    prompt = f"Based on historical data up to April 20th, predict the outcome of the Premier League football match between {team1} and {team2}."
    prompt += f"\n\n{team1} matches:\n{team1_data}\n\n{team2} matches:\n{team2_data}"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    prediction = response.choices[0].text.strip()
    return prediction

# Define the upcoming matches to predict
upcoming_matches = ["Liverpool", "Nottingham Forest"]
("Team A", "Team B"),("Team C", "Team D"),
    # Add more team pairs as needed


# Call the function to generate predictions for the upcoming matches
for match in upcoming_matches:
    team1, team2 = match
    prediction = predict_match_outcome(team1, team2)
    print(f"{team1} vs {team2}: {prediction}")
