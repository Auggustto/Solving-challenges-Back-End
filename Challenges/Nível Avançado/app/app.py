from flask import Flask, request
from flask_restful import Resource, Api

from controllers.user_controller.user_controller import UserController
from controllers.login_controller.login_controller import LoginController
from controllers.posting_controller.posting_controller import PostingController



app = Flask(__name__)
api = Api(app)


class Login(Resource):

    def post(self):
        email = request.json.get("email")
        password = request.json.get("password")

        return LoginController.login_user(email, password)


class AllUser(Resource):

    def get(self):
        return UserController.all_users()


class UserResource(Resource):

    @staticmethod
    def get_metadata():
        return (
            request.json.get("name"),
            request.json.get("lastname"),
            request.json.get("birthdata"),
            request.json.get("email"),
            request.json.get("password")
        )
    

    def post(self):
        name, lastname, birthdata, email, password = self.get_metadata()

        return UserController.create_user(name=name, lastname=lastname, birthdata=birthdata, email=email, password=password)


    def get(self, email):
        # _, _, _, email, _= self.get_metadata()
        return UserController.read_user(email=email)


    def put(self):
        name, lastname, birthdata, email, _ = self.get_metadata()

        return UserController.update_user(name, lastname, birthdata, email)
    

    def delete(self):
        email = request.json.get("email")

        return UserController.delete_user(email)


class PostingResource(Resource):

    @staticmethod
    def get_posting():
        return (
            request.json.get("id"),
            request.json.get("email"),
            request.json.get("category"),
            request.json.get("title"),
            request.json.get("post"),
            request.json.get("image_url"),
            request.json.get("tags"),
        )
    
    def post(self):
        _, email, category, title, post, image_url, tags = self.get_posting()
        
        return PostingController.create_posting(email, category, title, post, image_url, tags)


    def get(self, id):
        
        return PostingController.read_posting(id)
    

    def delete(self):
        id = request.json.get("id")

        return PostingController.delete_posting(id)
    

    def put(self):
        
        id, _, category, title, post, image_url, tags = self.get_posting()

        return PostingController.update_posting(id, category, title, post, image_url, tags)


class Like(Resource):
    def post(self, post_id):
        email = request.json.get("email")
        
        return PostingController.like_posting(email, post_id)


    def delete(self, post_id):
        email = request.json.get("email")
        
        return PostingController.dislike_posting(email, post_id)


api.add_resource(Login, '/api/login')
api.add_resource(UserResource, '/api/user', '/api/user/<string:email>')
api.add_resource(PostingResource, '/api/post', '/api/post/<int:id>')
api.add_resource(Like, '/api/post/<int:post_id>/like', '/api/post/<int:post_id>/dislike')


if __name__ == "__main__":
    app.run(debug=True)