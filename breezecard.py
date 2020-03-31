import requests

from flask import Flask, jsonify
from bs4 import BeautifulSoup;


def getBreezeCardInfo(cardnumber):
    if (len(cardnumber) != 20):
        return "Inapporiate Card Value:" + cardnumber, 400

    urlx = 'https://balance.breezecard.com/breezeWeb/jsp/web/cardnumberweb.jsp'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

    # The post to get the actual results is to this url.
    post = "https://balance.breezecard.com/breezeWeb/cardnumber_qa.do"

    with requests.Session() as s:
        s.get(urlx)
        print(s)
        try:
            results = s.post(post, data={"cardnumber": cardnumber, "submitButton.x":38,"submitButton.y":17})
        except:
            return "Server Side Error", 500

    soup = BeautifulSoup(results.content, 'html.parser')

    tb = soup.get_text().split("\n\n")
    ab = tb[19].split("\n")

    if (len(tb) != 40):
        return "Card Not Found", 404

    try:
        cardInfo = {
            "cardNum" : cardnumber,
            "balanceProtc":  tb[14].split(": ")[1],
            "cardExprDate":  tb[15][len(tb[15])-10:len(tb[15])],
            "passType": ab[1],
            "passExp": ab[2],
            "remRides": ab[3],
            "remBal": tb[22].split("\n")[1],
            "pendTrans":  tb[26]
        }
    except:
        return "Error Creating Parsing Data", 500

    return jsonify(cardInfo)
