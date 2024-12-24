from app import app

@app.route('/')
def home():
    return "Backend is running!"