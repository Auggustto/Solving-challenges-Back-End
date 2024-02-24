from models.user_models.users_models import UserManager
import logging
import bcrypt


class LoginManager:

    def login_user(email, password):
        try:
            user = UserManager.filter_user(email)

            if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
                print("deu bom")
            else:
                return {"error": "E-mail or password is incorrect!"}, 401
                
        except Exception as e:
            logging.error(f"Error login user: {e}")
            return {"error": "E-mail or password is incorrect!"}, 500

