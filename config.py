# config.py

from flask import Flask
import os

# Initialize Flask application
app = Flask(__name__)

# Configuration settings

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///career_agent.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Claude API configuration
app.config['CLAUDE_API_KEY'] = os.getenv('CLAUDE_API_KEY', 'your_api_key_here')
app.config['CLAUDE_API_URL'] = os.getenv('CLAUDE_API_URL', 'https://api.claude.ai/v1')

# Other settings
app.config['DEBUG'] = True
