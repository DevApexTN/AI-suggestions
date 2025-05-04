# AI Suggestions

AI Suggestions is a Flask-based web application that helps suggest employees for specific tasks based on their skills and proficiency. It integrates with a Spring Boot API to fetch team members and their skills, and uses fuzzy matching to determine the best candidates for a given task description.

## Features

- Fetches team members and their skills from a Spring Boot API.
- Uses fuzzy matching to suggest employees based on task descriptions.
- Provides a RESTful endpoint for task-based employee suggestions.
- Cross-Origin Resource Sharing (CORS) enabled for frontend integration.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or later
- pip (Python package manager)
- A running instance of the Spring Boot API at `http://localhost:8083/api`

## Getting Started

Follow these steps to set up and run the application:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-suggestions.git
cd AI-suggestions
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, manually install the dependencies:

```bash
pip install flask flask-cors requests rapidfuzz
```

### 4. Run the Application

Start the Flask application:

```bash
python app.py
```

The application will run on `http://localhost:5001`.

### 5. Test the API

Use a tool like Postman or `curl` to test the `/suggest` endpoint. Example request:

```bash
curl -X POST http://localhost:5001/suggest \
-H "Content-Type: application/json" \
-d '{"task_description": "Optimize server performance"}'
```

### 6. Frontend Integration

The application is CORS-enabled, allowing integration with a frontend running on `http://localhost:4200`.

## File Structure

- `app.py`: Main application file containing the Flask app and API logic.
- `.gitignore`: Specifies files and directories to ignore in version control.
- `README.md`: Documentation for the project.

## API Endpoints

### `/suggest` (POST)

- **Description**: Suggests employees for a given task description.
- **Request Body**:
  ```json
  {
    "task_description": "string"
  }
  ```
- **Response**:
  ```json
  {
    "suggested_employees": [
      {
        "id": "string",
        "name": "string",
        "matched_skills": [
          {
            "skill": "string",
            "proficiency": "string",
            "match_score": "number"
          }
        ]
      }
    ]
  }
  ```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.