from operator import index
from flask import Flask, request, render_template, jsonify
from model import SentimentRecomModel

app = Flask(__name__)

sentiment_model = SentimentRecomModel()

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/predict', methods=['POST'])
def predicton():
    # get user specific details 
    usr=request.form['usrName']
    usr=usr.lower()
    itms=sentiment_model.getSentimentRecommendations(usr)
    if(not(itms is None)):
        print(f"retrieving items....{len(itms)}")
        print(itms)
        # data=[items.to_html(classes="table-striped table-hover", header="true",index=False)
        return render_template("table.html", column_names=itms.columns.values,usrname=usr.upper(), row_data=list(itms.values.tolist()), zip=zip)
    else:
        return render_template("table.html", message="The user is not Analyzed ! No Recomendation at this point")

if __name__ == '__main__':
    app.run()