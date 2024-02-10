from flask import Flask, render_template

app = Flask(__name__)

'''
# Routing for your application.
# Put your routes below this comment
'''
<<<<<<< HEAD
@app.route('/')
def home():
    return 'My home page'
=======

>>>>>>> d0782897ead00ac245fd3545a3342d063ec0a2d1

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
