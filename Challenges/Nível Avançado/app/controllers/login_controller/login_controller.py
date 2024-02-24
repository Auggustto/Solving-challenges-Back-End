from models.login_models.login_model import LoginManager

class LoginController:
    
    @staticmethod
    def login_user(email, password):
        return LoginManager.login_user(email, password)