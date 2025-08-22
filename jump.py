from flask import Flask as f , render_template,request
mera_apk = f(__name__,template_folder=".") #Flask Application


@mera_apk.route("/")
def home():
    return render_template("index.html")# home page is done


@mera_apk.route("/signin.html")
def sign():
    return render_template("signin.html") # sign in page done

@mera_apk.route("/up",methods=['POST'])
def updown():
    if request.method== 'POST':
        user = request.form['username']
        password = request.form['password']
        if user == 'admin' and password == 'admin':
            return render_template("ok.html")

if __name__ =="__main__":
    mera_apk.run(debug=True)
    
    
    
    # here we cover sign in demo 
    
