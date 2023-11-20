from flask import Flask, request
from flask import jsonify
from dotenv import load_dotenv
import os
from business_rule_engine import RuleParser

load_dotenv()




def create_app(enviroment):
    app = Flask(__name__)
    return app

app = create_app('development')

@app.route('/api/v1/getCarrer', methods=['POST'])
def get_carrer():
    
    data = request.get_json()

    math = data.get('math')
    we = data.get('we')
    ns = data.get('ns')
    fl = data.get('fl')
    ss = data.get('ss')
    hum = data.get('hum')
    eng = data.get('eng')
    sci = data.get('sci')
    health = data.get('health')

    res = []
    
    params = {
    "Math": math,
    "Written_expression": we,
    "Natural_sciences": ns,
    "Foreign_language": fl,
    "Social_sciences": ss,
    "Humanities": hum,
    "Engineering": eng,
    "Sciences": sci,
    "Health": health
    }


    with open('rules.txt', 'r') as file:
        rules = file.read()
    

    def getRes(msg):
        res.append(msg)
        return True

    
    parser = RuleParser()
    parser.register_function(getRes)
    parser.parsestr(rules)
    response = parser.execute(params)
    
    # if (response == False):
    #     response = "You can't study any career"
    print(response)
    return jsonify(res)
                                                                                    



if __name__ == '__main__':
    app.run(debug=True)