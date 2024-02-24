from flask import Flask, request
from flask_restful import Resource, Api

from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


app = Flask(__name__)
api = Api(app)
app.config["JWT_SECRET_KEY"] = "2ibma*<6{8i*]slz5^217p(q4z=&4$xv_d_:[)j=+=24[8e!|0{`>634+r[%bg2"
jwt = JWTManager(app)


users = {}
next_user_id = 1


class Login(Resource):
    def post(self):
        """
        Checks if the provided email and password correspond to a registered user.

        Returns:
            dict: Success message or error message with the corresponding HTTP status.
        """
        email = request.json.get("email")
        password = request.json.get("password")

        for user in users.values():
            if user["email"] == email and user["password"] == password:
                access_token = create_access_token(identity=email)

                return access_token, 200
            
        return {"message": "E-mail or password is incorrect!"}, 401


class Users(Resource):

    @jwt_required()
    def search_user(user_id):
        """
        Searches for a user by ID.

        Args:
            user_id (int): The ID of the user to be searched.

        Returns:
            dict or None: The user information if found, otherwise, None.
        """
        if user_id in users:
            return users[user_id]


    @jwt_required()
    def post(self):
        """
        Adds a new user.
        """
        user_id = request.json.get("user_id")
        filter_user = Users.search_user(user_id)

        if filter_user:
            return filter_user, 200
        else:
            return {"message": "User not found!"}, 404


    @jwt_required()
    def put(self):
        """
        Updates the information of an existing user.
        """
        user_id = request.json.get("user_id")
        fullname = request.json.get("fullname")
        email = request.json.get("email")
        birth_date = request.json.get("birth_date")
        password = request.json.get("password")

        if user_id in users:
            users[user_id].update({
                "fullname": fullname,
                "email": email,
                "birth_date": birth_date,
                "password": password
            })
            return users[user_id], 200
        else:
            return {"message": "User not found!"}, 404


    @jwt_required()
    def delete(self):
        """
        Removes an existing user.
        """
        user_id = request.json.get("user_id")

        if user_id in users:
            users.pop(user_id)
            return {"message": f"User {user_id} deleted successfully!"}
        else:
            return {"message": "User not found!"}, 404


class ListUsers(Resource):

    @jwt_required()
    def get(self):
        """
        Gets the list of all users.
        """
        return {"users": users}, 200


    def post(self):
        """
        Adds a new user to the list.
        """
        global next_user_id

        data = request.json
        user_id = next_user_id
        users[user_id] = data
        next_user_id += 1
        return {"message": "User created successfully!"}, 201


api.add_resource(ListUsers, '/api/users')
api.add_resource(Users, '/api/user_methods')
api.add_resource(Login, '/api/login')


if __name__=="__main__":
    app.run(debug=True)
