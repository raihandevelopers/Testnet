from flask import Flask, render_template, request
import requests

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    data__list = []
    website = ""
    if request.method == "POST":
        website = request.form.get("website")
        try:
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
            response = requests.get(f"https://data.similarweb.com/api/v1/data?domain={website}", headers=headers)
            data = response.json()
            website_name = data["SiteName"]
            global_rank = data["GlobalRank"]["Rank"]
            monthly_revenew = data["Engagments"]["Visits"]
            b_rate = data["Engagments"]["BounceRate"]
            b_rate_slice = b_rate[0: 4]


            data__list.append(website_name)
            data__list.append(monthly_revenew)
            data__list.append(b_rate_slice)
            data__list.append(global_rank)
        except:
            data__list.append("Some Error Occured")
            data__list.append("Err")
            data__list.append("Err")
            data__list.append("Err")
    return render_template("index.html", data = data__list, data_len = len(data__list), input = website)


if __name__ == "__main__":
    app.run()