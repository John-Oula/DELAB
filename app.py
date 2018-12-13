from flask import Flask,render_template,url_for,redirect,request,flash,session
from Databases import User,Profile
from flask_bcrypt import generate_password_hash,check_password_hash

app = Flask(__name__)
app.secret_key ="qwerty123asdfg"



@app.route('/')
def home():
    return render_template('HOME.html')


@app.route('/DISCOVER')
def discover():
    return render_template('DISCOVER.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == "POST":
        names = request.form["name"]
        unames = request.form["username"]
        astyle = request.form["style"]
        email = request.form["email"]
        password = request.form["pwd"]
        password = generate_password_hash(password)
        User.create(names = names,username = unames,style = astyle, email = email, password = password)
        flash("Account Created Successfully")
    return render_template("SIGNUP.html")


@app.route('/PROFILE',methods=['GET','POST'])
def profile():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == "POST":
        names = request.form["names"]
        username = request.form["username"]
        email = request.form["email"]
        style = request.form["style"]
        users = User.select()
    return render_template('PROFILE.html')


@app.route('/login' , methods=['GET','POST'])
def login():
    if request.method == ['POST']:
        email = request.form["email"]
        password = request.form["pwd"]
        try:
            user = User.get(User.email==email)
            hashed_password = user.password
            if check_password_hash(hashed_password,password):
                flash("Logging in")
                session['logged_in'] = True
                session['names'] = user.names
                session['id'] = user.id
                return redirect(url_for('PROFILE'))
        except User.DoesNotExist:
            flash("Wrong Email/Username or password")
    return render_template('LOGIN.html')

@app.route('/SHOP')
def shop():
    return render_template('SHOP.html')

@app.route('/PORTFOLIO')
def designs():
    return render_template('PORTFOLIO.html')

@app.route('/BLOG')
def contacts():
    return render_template('BLOG.html')

@app.route('/CLIENT')
def client():
    return render_template('CLIENT-HOME.html')



if __name__ == '__main__':
    app.run()