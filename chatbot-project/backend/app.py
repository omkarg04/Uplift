from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, text

app = Flask(__name__)
CORS(app)

# MySQL connection string
# Format: mysql+pymysql://username:password@host:port/database
DB_URL = "mysql+pymysql://chatuser:ChatPass!234@localhost:3306/chatbotdb"

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
