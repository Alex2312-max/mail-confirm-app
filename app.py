from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from mail import send_email, check_verification_code

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_information.db'
db = SQLAlchemy(app)
ver_li = []


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<User %s>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        user_name = request.form['user_name']
        last_name = request.form['last_name']
        email = request.form['email']
        new_user = Data(user_name=user_name, last_name=last_name, email=email)

        try:
            db.session.add(new_user)
            db.session.commit()
        except:
            return 'Invalid information provided.'

        verification_code = send_email(email)
        ver_li.append(str(verification_code))

        return redirect('/confirmation')

    return render_template('index.html')


@app.route('/confirmation', methods=['POST', 'GET'])
def confirm():

    if request.method == 'POST':
        code = request.form['code']
        print(code)
        print(ver_li)
        if ver_li[-1] == str(code):

            users = Data.query.order_by(Data.id).first()

            return render_template('validation.html', users=users)
        else:
            return render_template('notvalid.html')

    return render_template('confirmation.html')


if __name__ == '__main__':
    app.run(debug=True)
