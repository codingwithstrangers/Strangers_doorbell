from flask import Flask, render_template
count = 0
# rendering basic webpages using jinja to understand how data you want makes its way into your templateapp = Flask(__name__)

# @app.route('/')
# def hello_Stranger():
#     return 'Hello you Strangers another test!!'


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/button', methods=['POST'])
def button_pressed():
    global count
    count += 1
    if count < 10:
        return render_template('home.html', count=count)
    else:
        print('Button pressed!')
        return render_template('button.html', count=count)

if __name__ == '__main__':
    app.run()