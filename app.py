from flask import Flask,render_template,request,redirect,url_for
import sqlite3 as sql

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():  
    conn=sql.connect("youtube.db")
    conn.row_factory=sql.Row
    cur=conn.cursor() 
    cur.execute("select * from display")
    data=cur.fetchall()
    if request.method=="POST":
        store =request.json     
        cur.execute("insert into display(thumbnail,profile,description,upload,channel,views) values(?,?,?,?,?,?)",(store["thumbnail"],store["profile"],store["description"],store["upload"],store["channel"],store["views"]))
        conn.commit()
    return render_template("index.html",thumbnaillist1=data)

@app.route("/a/<string:id>",methods=["POST","GET"])
def play(id):
    conn=sql.connect("youtube.db")
    conn.row_factory=sql.Row
    cur=conn.cursor() 
    
   
    cur.execute("Select * from display where videoid=?",(id,))
    data2=cur.fetchone()
    conn.commit
    return render_template("videoplayer.html",d=data2)

@app.route("/upload",methods=["POST","GET"])
def upload():
    if request.method=="POST":
        videoid=request.form.get("videoid")
        description=request.form.get("description")
        thumbnail=request.form.get("thumbnail")
        channel=request.form.get("channel")
        views=request.form.get("views")
        upload=request.form.get("upload")
        profile=request.form.get("profile")
        conn=sql.connect("youtube.db")
        cur=conn.cursor()
        cur.execute("insert into display (videoid,thumbnail,pofile,description,upload,channel,view) values(?,?,?,?,?,?,?)",(videoid,thumbnail,profile,description,upload,channel,views))
        conn.commit()
        return redirect(url_for("home"))
    return render_template("index1.html")


if "__main__"==__name__:
    app.run(debug=True)
