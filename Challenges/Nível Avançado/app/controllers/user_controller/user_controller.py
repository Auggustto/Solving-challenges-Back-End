from models.user_models.users_models import UserManager
from dateutil import parser

class UserController:
    """
    Controller class for managing user-related operations.
    """

    @staticmethod
    def format_birthdata(birthdata):
        """
        Format birthdate string to date object.

        Args:
            birthdata (str): Birthdate string.

        Returns:
            date: Birthdate as date object.
        """
        return parser.parse(birthdata, dayfirst=True).date()


    @staticmethod
    def create_user(name, lastname, birthdata, email, password):
        """
        Create a new user.

        Args:
            name (str): User's first name.
            lastname (str): User's last name.
            birthdata (str): User's birthdate string.
            email (str): User's email address.
            password (str): User's password.

        Returns:
            dict: Response message indicating success or error.
        """
        if not all([name, lastname, birthdata, email, password]):
            return {"error": "All fields are required"}, 400
        try:
            object_data = UserController.format_birthdata(birthdata)
            return UserManager.create_user(name=name, lastname=lastname, birthdata=object_data, email=email, password=password)
        except Exception as e:
            return {"error": str(e)}, 500


    @staticmethod
    def read_user(email):
        """
        Read user data by email.

        Args:
            email (str): Email address of the user to read.

        Returns:
            dict: User data or error message.
        """
        if not email:
            return {"error": "E-mail required"}, 400
        try:
            return UserManager.read_user(email=email)
        except Exception as e:
            return {"error": str(e)}, 500


    @staticmethod
    def update_user(name, lastname, birthdata, email):
        """
        Update user data.

        Args:
            name (str): Updated first name.
            lastname (str): Updated last name.
            birthdata (str): Updated birthdate string.
            email (str): Email address of the user to update.

        Returns:
            dict: Response message indicating success or error.
        """
        if not all([name, lastname, birthdata, email]):
            return {"error": "All fields are required"}, 400
        try:
            object_data = UserController.format_birthdata(birthdata)
            return UserManager.update_user(name=name, lastname=lastname, birthdata=object_data, email=email)
        except Exception as e:
            return {"error": str(e)}, 500


    @staticmethod
    def delete_user(email):
        """
        Delete a user.

        Args:
            email (str): Email address of the user to delete.

        Returns:
            dict: Response message indicating success or error.
        """
        if not email:
            return {"error": "E-mail required"}, 400
        try:
            return UserManager.delete_user(email)
        except Exception as e:
            return {"error": str(e)}, 500


    @staticmethod
    def all_users():
        """
        Get all users.

        Returns:
            dict: List of user data or error message.
        """
        try:
            return UserManager.read_all_users()
        except Exception as e:
            return {"error": str(e)}, 500
