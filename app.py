from flask import Flask, jsonify, request
from models import db, Post
from config import Config
from sqlalchemy.exc import NoResultFound


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
    data = request.get_json()
    if not data["title"] or not data["author"] or not data["content"] or not data["category"]:
        return jsonify('{"error":"Title, Content, Author and Category required"}')
    new_post = Post(
        title=data["title"],
        content=data["content"],
        author = data["author"],
        category=data["category"],
    )
    db.session.add(new_post)
    db.session.commit()
    return jsonify('{"message":"Blog post created"}')


# Read All Blog Posts - API
@app.route('/posts', methods=['GET'])
def get_all_posts():
    ...


# Read a Single Blog Post - API
@app.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    ...

# Delete Blog Post - API
@app.route('/delete-post/<int:id>', methods=['DELETE'])
def delete_post(id):
    try:
        post = Post.query.filter_by(id=id).one() 
        db.session.delete(post)
        db.session.commit()
        return jsonify({ "message": "Deleted post successfully" })
    except NoResultFound:
        return jsonify({ "error": "Post not found" }), 404 

@app.route('/posts/search', methods=['GET'])
def search_posts():
    term = request.args.get('term', '')
    posts = Post.query.filter(
        Post.title.contains(term) |
        Post.content.contains(term) |
        Post.category.contains(term) |
        Post.author.contains(term) |
        Post.created_at.contains(term)
    ).all()
    if not posts:
        return jsonify('{ "message" : "Post not found" }')
    posts_list = [
        {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'category': post.category,
            'created_at': post.created_at
        } for post in posts
    ]
    return jsonify(posts_list), 200



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
