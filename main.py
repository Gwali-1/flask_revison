from flask import Flask,render_template,request,send_from_directory,current_app,send_file
import os

app = Flask(__name__,static_url_path='/static')

@app.route("/",methods=["GET","POST"])
def action():
    if request.method == "POST":
        # key = request.form["name"] if "name" in request.form else "default"
        with open(os.getcwd()+"/static/records.txt","a") as f:
            f.write(f'[{request.form.get("name")},{request.form.get("number")}]\n')
        return render_template("key.html",key=request.form.get("name"))
      
    return render_template("index.html")

    # key = request.args["name"] if "name" in request.args else "default"
    # if "name" in request.args:
    #     key = request.args["name"]
    # else:
    #     key = "default"


@app.route("/download")
def down():
    print("here")
    x= os.getcwd()
    # filepath = os.path.join(current_app.root_path,"static/")
    filepath = os.path.join(current_app.root_path,"static/records.txt")
    print(filepath)
    return send_file(filepath,as_attachment=True)
    # return send_from_directory(filepath,"records.txt")
    