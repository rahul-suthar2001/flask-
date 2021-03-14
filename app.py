import smtplib 
from flask import Flask , render_template,request




app=Flask("firstapp")
@app.route("/")
def home():
	html=render_template("index.html")
	return html
@app.route("/form")
def form():
	return render_template("from.html")
@app.route("/mail" ,methods=["GET"])
def  mail():
	w=request.args.get("em")
	x=request.args.get("emm")
	y=request.args.get("pas")
	z=request.args.get("message")
	
	smtp_object = smtplib.SMTP('smtp.gmail.com',587)
	smtp_object.ehlo()
	smtp_object.starttls()
	email= w
	password= y
	smtp_object.login(email,password)
	from_id = w
	to = x
	msg= z
	smtp_object.sendmail(from_id , to , msg )
	smtp_object.quit()

	return "ok "


	