from flask import Flask, render_template, redirect, request

# creating a flask instance.the __name__ helps flask find all the files and directory
app=Flask(__name__)



@app.route('/index')
def index():
    name='Dev'
    return render_template('index.html',name=name)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

#Now we are creating custom error pages.For such pages flask offers a mechanism called #@app.errorhandler

# 1. For INVALID URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



# 2.Internal server error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
