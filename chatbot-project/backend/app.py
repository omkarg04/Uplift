from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

app = Flask(__name__)
CORS(app)

# Read from .env
DB_USER = os.getenv("MYSQL_USER")
DB_PASS = os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("MYSQL_DATABASE")
DB_PORT = os.getenv("HOST_DB_PORT", "3306")

DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@localhost:{DB_PORT}/{DB_NAME}"

# Create database engine
engine = create_engine(DB_URL, echo=True)

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/testdb")
def testdb():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT DATABASE();"))
            db_name = result.scalar()
        return jsonify({"connected_to": db_name})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
