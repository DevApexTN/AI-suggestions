import requests
from flask import Flask, request, jsonify
from rapidfuzz import process
from flask_cors import CORS
app = Flask(__name__)
CORS(app, origins="http://localhost:4200")
SPRING_BOOT_API_URL = 'http://localhost:8083/api'  # Update with your Spring Boot app URL

# Fetch team members and skills from Spring Boot
def get_team_members():
    response = requests.get(f'{SPRING_BOOT_API_URL}/team-members')
    if response.status_code == 200:
        return response.json()
    return []

def get_skills():
    response = requests.get(f'{SPRING_BOOT_API_URL}/skills')
    if response.status_code == 200:
        return response.json()
    return []

# Function to suggest employees based on task description
def suggest_employees(task_description):
    task_description = task_description.lower()  # Normalize the task description
    suggestions = []

    # Fetch team members and skills from Spring Boot API
    team_members = get_team_members()
    skills = get_skills()

    # Loop through each team member and their skills
    for team_member in team_members:
        matched_skills = []
        for skill_data in team_member['teamMemberSkills']:
            skill_name = skill_data['skill']['name'].lower()
            proficiency = skill_data['proficiency']

            # Check if skill matches task description
            match_score = process.extractOne(task_description, [skill_name])[1]

            if match_score > 80:  # Threshold for good match
                matched_skills.append({
                    'skill': skill_name,
                    'proficiency': proficiency,
                    'match_score': match_score
                })

        if matched_skills:
            suggestions.append({
                'id': team_member['id'],
                'name': team_member['name'],
                'matched_skills': matched_skills
            })

    return suggestions

@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.json
    task_description = data['task_description']
    suggested = suggest_employees(task_description)
    return jsonify({'suggested_employees': suggested})

if __name__ == '__main__':
    app.run(port=5001, debug=True)