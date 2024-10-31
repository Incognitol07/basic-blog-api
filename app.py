from flask import Flask, jsonify
from models import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


# Home - View All Blog Posts
@app.route('/')
def home():
    return {"message":"Welcome to our Blog API"}


# Create Blog Post - API
@app.route('/posts', methods=['POST'])
def create_post():
    ...


# Read All Blog Posts - API
@app.route('/posts', methods=['GET'])
def get_all_posts():
    ...


# Read a Single Blog Post - API
@app.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    ...

# Delete Blog Post - API
@app.route('/delete-post/<int:id>', methods=['POST'])
def delete_post(id):
    ...



if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(debug=True)
