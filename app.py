import os
from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv

app = Flask(__name__)


load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}"
}


def fetch_github_data(username):
    user_response = requests.get(f"https://api.github.com/users/{username}", headers=HEADERS)
    repos_response = requests.get(f"https://api.github.com/users/{username}/repos", headers=HEADERS)
    
    if user_response.status_code == 200 and repos_response.status_code == 200:
        user_data = user_response.json()
        repos_data = repos_response.json()
        return user_data, repos_data
    else:
        return None, None


@app.route("/")
def resume():
    user_data, repos_data = fetch_github_data(GITHUB_USERNAME)
    if user_data:
        return render_template("resume.html", user=user_data, repos=repos_data)
    else:
        return "Failed to fetch GitHub data", 500


@app.route("/update", methods=["POST"])
def update_resume():
    user_data, repos_data = fetch_github_data(GITHUB_USERNAME)
    if user_data:
        return render_template("resume.html", user=user_data, repos=repos_data)
    else:
        return "Failed to update data", 500


@app.route("/api/repos", methods=["GET"])
def api_repos():
    user_data, repos_data = fetch_github_data(GITHUB_USERNAME)
    if repos_data:
        return jsonify(repos_data)
    else:
        return jsonify({"error": "Failed to fetch repositories"}), 500


if __name__ == "__main__":
    app.run(debug=True)
