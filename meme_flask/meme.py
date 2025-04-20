from flask import Flask, render_template, render_template_string
import requests 
import json 

app = Flask(__name__)

def home():
    if requests.method == "POST":
        selected = requests.form.get("Variable")
        return f"You selected : {selected}"

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit    

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])


def index():
    meme_pic, subreddit = get_meme()
    return render_template("index.html", meme_pic = meme_pic, subreddit = subreddit)


if __name__ == "__main__" :
    app.debug = True
    app.run(host = "0.0.0.0", port = 80)
