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
    

class MetodoPost(Resource):
    def post(self, nome, sobrenome, idade):
        return {"metadata": {"nome": f"{nome}", "sobrenome": f"{sobrenome}", "idade": f"{idade}"}}

api.add_resource(Hello, '/')
api.add_resource(Saudacoes, '/saudaces/<string:nome>')
api.add_resource(MetodoPost, '/metodopost/<string:nome>/<string:sobrenome>/<int:idade>')

if __name__=="__main__":
    app.run(debug=True)