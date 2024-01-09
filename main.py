from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chatbot/",methods=["GET","POST"])
def chatbot():
    query=""
    if request.method == "POST":
        query = request.form['input_text']
    headers = {
        'x-api-key': 'sec_V4eXR85Jnl3yx39CryHVljRDa5gpjVDQ',
        "Content-Type": "application/json",
    }
    data = {
        'sourceId': "cha_FDDtg2m0cEX2riLIEir8z",
        'messages': [
            {
                'role': "user",
                'content':f"{query}. Explain in 100 words." ,
            }
        ]
    }
    ans=""
    response = requests.post('https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)
    if response.status_code == 200:
        print('Result:', response.json()["content"])
        ans=response.json()["content"]
    else:
        print('Status:', response.status_code)
        print('Error:', response.text)
    return render_template("chatbot.html", generated_text = ans)

@app.route("/cl/")
def  cl():
    return render_template("cl.html")

@app.route("/cs/")
def  cs():
    return render_template("cs.html")

@app.route("/jl/")
def  jl():
    return render_template("jl.html")

@app.route("/js/")
def  js():
    return render_template("js.html")

@app.route("/ll/")
def  ll():
    return render_template("ll.html")

@app.route("/ls/")
def  ls():
    return render_template("ls.html")

@app.route("/rl/")
def  rl():
    return render_template("rl.html")

@app.route("/rs/")
def  rs():
    return render_template("rs.html")

@app.route("/civilian/")
def  civilian():
    return render_template("civilian.html")

@app.route("/judge/")
def  judge():
    return render_template("judge.html")

@app.route("/lawyer/")
def  lawyer():
    return render_template("lawyer.html")

@app.route("/registrar/")
def  registrar():
    return render_template("registrar.html")

if __name__=="__main__":
    app.run(debug=True,port=6969)