import sys
import os

# Add the project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from backend.app import app

if __name__ == "__main__":
    app.run(debug=True)
