from flask import Flask
import requests as req


app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    # given "cities"
    #[cities]

    # results[]
    # for city in cities
        # response = req.get("https://api.waqi.info/search/?token=491989f2467ee8ad41a1ed72d33635bf9669f1e6&keyword=" + )
        # save response it results
        # 

    return {
        'userId': 1, 
        'title': 'Flask React Application', 
        'completed': False
    }



    