from flask import Flask as fl, render_template as render

app = fl(__name__)
@app.route('/index')
@app.route('/')
def index():
	return render('index.html')

if __name__ == "__main__":
	app.run(debug=True)