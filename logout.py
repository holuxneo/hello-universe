from flask import Flask, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)