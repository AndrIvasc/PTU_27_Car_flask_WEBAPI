"""
Web api
"""

from models import db, CarProject
from flask import Flask, render_template, request, redirect, url_for, jsonify
from serializers import ProjektasSchema
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# fizines db prijungimas, configas
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projektai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# paleidziam db
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/api/models")  # http://127.0.0.1:5002/api/models
def home():
    all_projects = CarProject.query.all()
    projects_data = [ProjektasSchema.model_validate(project).model_dump() for project in all_projects]
    return jsonify(projects_data)


@app.route("/frontend")
def frontend():
    return render_template("main_index.html")


if __name__ == "__main__":
    app.run(port=5002)
