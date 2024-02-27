
from db.database import session, User
from models.hash_models.hash_model import HashModels
import logging

class UserManager:
    
    @staticmethod
    def filter_user(email):
        """
        Filters a user by email.

        Args:
            email (str): Email of the user to filter.

        Returns:
            User or None: User object found or None if not found.
        """
        try:
            return session.query(User).filter_by(email=email).first()
        except Exception as e:
            logging.error(f"Error filtering user: {e}")
            raise


    def create_user(name, lastname, birthdata, email, password):
        """
        Creates a new user.

        Args:
            name (str): User's first name.
            lastname (str): User's last name.
            birthdata (str): User's birthdate.
            email (str): User's email.
            password (str): User's password.

        Returns:
            dict: Message indicating success or error.
        """
        try:
            existing_user = UserManager.filter_user(email=email)

            if existing_user:
                return {"message": f"Email {email} is already in use!"}, 500
            
            new_user = User(name=name, lastname=lastname, birthdata=birthdata, email=email, password=HashModels.hash(password))
            session.add(new_user)
            session.commit()

            return {"message": "User created successfully!"}, 201
            
        except Exception as e:
            session.rollback()
            logging.error(f"Error creating user: {e}")
            return {"error": str(e)}, 500
        
        
    def read_user(email):
        """
        Reads user data based on email.

        Args:
            email (str): Email of the user to read.

        Returns:
            dict: User data in dictionary format.
        """
        try:
            read_user = UserManager.filter_user(email)

            if read_user:
                return read_user.as_dict()
            
            return {"error": f"User {email} not found!"}, 404
        
        except Exception as e:
            logging.error(f"Error reading user: {e}")
            return {"error": "An unexpected error occurred"}, 500


    def update_user(name, lastname, birthdata, email):
        """
        Updates user data.

        Args:
            name (str): Updated first name.
            lastname (str): Updated last name.
            birthdata (str): Updated birthdate.
            email (str): Email of the user to update.

        Returns:
            dict: Message indicating success or error.
        """
        try:
            select_user = UserManager.filter_user(email)

            if select_user:
                select_user.name = name
                select_user.lastname = lastname
                select_user.birthdata = birthdata

                session.commit()
                
                return {"message": "User updated successfully!"}, 200
            
            return {"error": f"User: {email} not found!"}, 500
            
        except Exception as e:
            session.rollback()
            logging.error(f"Error updating user: {e}")
            return {"error": "An unexpected error occurred"}, 500


    def delete_user(email):
        """
        Deletes a user.

        Args:
            email (str): Email of the user to delete.

        Returns:
            dict: Message indicating success or error.
        """
        try:
            select_user = UserManager.filter_user(email)

            if select_user:
                session.delete(select_user)
                session.commit()

                return {"status": f"User {email} deleted successfully!"}, 200
            
            return {"message": f"User: {email} not found!"}, 404
            
        except Exception as e:
            session.rollback()
            logging.error(f"Error deleting user: {e}")
            return {"error": "An unexpected error occurred"}, 500
        

    def read_all_users():
        """
        Reads all users.

        Returns:
            dict: List of user data or error message.
        """
        try:
            select_all = session.query(User).all()

            if select_all:
                return [user.as_dict() for user in select_all]
            
            return {"error": "Users not found!"}, 404
        
        except Exception as e:
            logging.error(f"Error reading all users: {e}")
            return {"error": "An unexpected error occurred"}, 500
