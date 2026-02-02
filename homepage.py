from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    profile = {
        'name': 'Your Name',
        'title': 'Software Engineer | Python Developer',
        'bio': 'Passionate about building elegant solutions to complex problems.',
        'skills': ['Python', 'Web Development', 'Data Science'],
        'projects': [
            {'title': 'Project 1', 'description': 'Brief description'},
            {'title': 'Project 2', 'description': 'Brief description'}
        ],
        'social_links': {
            'github': 'https://github.com/yourprofile',
            'linkedin': 'https://linkedin.com/in/yourprofile'
        }
    }
    return render_template('index.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)