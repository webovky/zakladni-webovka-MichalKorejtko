from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
""" secret_key se generuje pomoc os.urandom(počet znaku davej 24)
    ale obecně je to prostě velké náhodné číslo
    proměnnou secret_key nikdy nesdílím v depozitáři tak jako teď
"""

app.secret_key = b'os.urandom(24)' 


@app.route("/")
def index():
    return render_template("base.html.j2")

"""
@app.route("/abc/", methods=["GET"])
def abc():
    try:
        x = request.args.get("x") 
        y = request.args.get("y")
        soucet = int(x) + int(y)
    except TypeError:
        soucet = None
    except ValueError:
        soucet = "Nedělej si srandu!!!"
    
    slovo = request.args.get('slovo')
    if slovo:
        session['slovo'] = slovo

    return render_template("abc.html.j2", soucet=soucet)


@app.route("/abc/", methods=["POST"])
def abc_post():

    jmeno = request.form.get("jmeno")
    heslo = request.form.get("heslo")
    print("POST:", jmeno, heslo)

    return redirect(url_for("abc"))
"""
"""
@app.route("/banany/<parametr>")
def banany(parametr):
    return render_template("banany.html.j2", parametr=parametr)
"""

@app.route("/torque/")
def torque():
    if "user" in session: 
        return render_template("torque.html.j2")
    else:
        flash(f"Pro zobrazení této stránky ({request.path}) je nutné se přihlásit!", "err")
        return redirect(url_for("login", next=request.path))

@app.route("/sender/")
def sender():
    if "user" in session: 
        return render_template("sender.html.j2")
    else:
        flash(f"Pro zobrazení této stránky ({request.path}) je nutné se přihlásit!", "err")
        return redirect(url_for("login", next=request.path))

@app.route("/firma/")
def firma():
    return render_template("firma.html.j2")

@app.route("/spectral/")
def spectral():
    return render_template("spectral.html.j2")

@app.route("/Login/", methods=["GET"])
def login():
    if request.method== "GET":
        login=request.args.get("login")
        passwd= request.args.get("password")
        print(login, passwd)
    return render_template("login.html.j2")
    

@app.route("/Login/", methods=["POST"])
def login_post():
    login= request.form.get("login")
    passwd= request.form.get("password")
    print(login, passwd)
    if login =="mici36" and passwd =="1234":
        session["user"]=login
        flash("úspěšně jsi se přihlasil", "pass")
        next= request.args.get("next")
        if next:
            return redirect(next)
    else:
        flash("neplatné přihlašovací údaje", "err")
    if next:
        return redirect(url_for("login",next=next))
    else:
        return redirect(url_for("login"))

@app.route("/Logout/")
def logout():
    session.pop("user", None)
    flash("právě jsi se odhlásil", "pass")
    return redirect (url_for("login"))