from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return {"message": "Olá, Mundo!"}

class Saudacoes(Resource):
    def get(self, nome):
        return {"message": f"Olá, {nome}!"}

api.add_resource(Hello, '/')
api.add_resource(Saudacoes, '/saudaces/<string:nome>')

if __name__=="__main__":
    app.run(debug=True)