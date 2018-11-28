from flask import Flask as fl, request
from flask import render_template as render

app = fl(__name__)

@app.route('/')
@app.route('/dashboard')
def dashboard():
	return render('dashboard/index.html')


@app.route('/users')
def users():
	return render('users/index.html')

@app.route('/products')
def products():
	return render('products/index.html')

# @app.route('/products')
# def dashboard():
# 	return render('dashboard/index.html')

# @app.route('/users')
# def dashboard():
# 	return render('dashboard/index.html')

# @app.route('/login')
# def dashboard():
# 	return render('dashboard/index.html')

# @app.route('/users')
# def dashboard():
# 	return render('dashboard/index.html')

# @app.route('/users')
# def dashboard():
# 	return render('dashboard/index.html')




if __name__ == "__main__":
	app.run(debug=True)