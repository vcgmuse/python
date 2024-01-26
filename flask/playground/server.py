from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
# IMPORTANT HINT ON HOW TO GET CSS IN HTML NEED TO INVESTIGATE
# https://stackoverflow.com/questions/13162245/flask-jinja2-insert-content-of-css-file-inline
# https://python-web.teclado.com/section09/lectures/06_custom_css_jinja2/
# https://flask.palletsprojects.com/en/1.1.x/patterns/jquery/

@app.route('/play')
def play():
    return render_template('play.html')
@app.route('/play/<int:times>')
def play_repeat(times):
    return render_template('play.html', times=times)
@app.route('/play/<int:times>/<string:user_color>')
def play_repeat_color(times, user_color):
    return render_template('play.html', times= times, user_color=user_color)
@app.route('/<path:unknown>/')
def unknown_path(unknown):
    return f"Sorry! {unknown} is not a path. No response. Try again."

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
    
