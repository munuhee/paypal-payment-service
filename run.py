"""
run.py

This script runs the Flask application in debug mode.
"""

from app import app

if __name__ == '__main__':
    app.run(debug=True)
