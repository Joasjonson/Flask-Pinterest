from flask import render_template, url_for, redirect
from mypinterest import app, db, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from mypinterest.forms import FormLogin, FormCreateUser, FormPicture
from mypinterest.models import User, Picture
import os
from werkzeug.utils import secure_filename


@app.route("/", methods=["GET", "POST"])
def index():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        user = User.query.filter_by(email=form_login.email.data).first()
        if user and bcrypt.check_password_hash(user.password.encode("utf-8"), form_login.password.data):
            login_user(user)

            return redirect(url_for("profile", id_user=user.id))

    return render_template("index.html", form_login=form_login)


@app.route("/account", methods=["GET", "POST"])
def account():
    create_user = FormCreateUser()
    if create_user.validate_on_submit():
        password = bcrypt.generate_password_hash(create_user.password.data).decode("utf-8")
        user = User(username=create_user.username.data, password=password, email=create_user.email.data)

        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)

        return redirect(url_for("profile", id_user=user.id))
    return render_template("account.html", create_user=create_user)


@app.route("/profile/<id_user>", methods=["GET", "POST"])
@login_required
def profile(id_user):
    if int(id_user) == int(current_user.id):

        form_picture = FormPicture()
        if form_picture.validate_on_submit():
            file = form_picture.picture.data
            secure_name = secure_filename(file.filename)

            path = os.path.join(os.path.abspath(os.path.dirname(__file__))
                            , app.config["UPLOAD_FOLDER"], secure_name)
            file.save(path)

            picture = Picture(image=secure_name, id_user=current_user.id)
            db.session.add(picture)
            db.session.commit()

        return render_template("profile.html", user=current_user, form_picture=form_picture)
    else:
        user = User.query.get(int(id_user))
        return render_template("profile.html", user=user, form_picture=None)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/feed")
@login_required
def feed():
    pictures = Picture.query.order_by(Picture.load_date.desc()).all()
    return render_template("feed.html", pictures=pictures)







