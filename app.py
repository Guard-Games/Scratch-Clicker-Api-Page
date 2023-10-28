from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return "Welcome to the API Page, to get started download our pip package"

class apipage(Resource):
    def get(self):
        return {"data": "Try using our pip package to get started"}
    def post(self):
        return {"data": "Try using our pip package to get started"}
class platform(Resource):
    def get(self, platform):
        if platform == "gamejolt":
            return {"data": "Gamejolt", "link": "https://gamejolt.com/games/scratchclicker/795634"}
        if platform == "itch":
            return {"data": "Itch.io", "link": "https://sourceguy.itch.io/scratchclickeritchio"}
        if platform == "classic":
            return {"data": "Classic", "link": "https://gamejolt.com/games/scratch/794525"}
    def post(self):
        return {"data": "Try using our pip package to get started"}
    
    
api.add_resource(apipage, '/api')
api.add_resource(platform, '/platform/<platform>')
    
if __name__ == '__main__':
    app.run(debug=True)