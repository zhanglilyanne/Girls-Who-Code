from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('home.html', scroll='about')

@app.route('/projects/')
def projects():
    return render_template('projects.html')

# start projects
@app.route('/projects/choose-your-adventure/')
def adventure_game():
    return render_template('choose_adventure.html')

@app.route('/projects/word-game/')
def word_game():
    return render_template('word_game.html')

@app.route('/projects/coding-languages/')
def coding_languages():
    return render_template('coding_languages.html')

@app.route('/projects/tic-tac-toe/')
def tic_tac_toe():
    return render_template('tic_tac_toe.html')
# end projects

@app.route('/members/')
def members():
    return render_template('members.html')

if __name__ == '__main__':
    app.run(debug=True)
