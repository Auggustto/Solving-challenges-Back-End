from models.user_models.users_models import UserManager
from db.database import session, Posting
from datetime import datetime
import logging


class PostingManager:

    def create_post(email, category, post):
        try:
            user = UserManager.filter_user(email)
            if user:
                """ Settings default """
                now = datetime.now()

                new_post = Posting(
                    category=category,
                    post=post,
                    date=now.date(),
                    time=now.time(),
                )

                user.posts.append(new_post)

                session.add(new_post)
                session.commit()

                return {"message": "Posting created sucessfully!"}, 201

        except Exception as e:
            session.rollback()
            logging.error(f"Error in create posting {e}")
            return {"error": str(e)}, 500


                

    def read_post(self):
        pass
    def update_post(self):
        pass
    def delete_post(self):
        pass
    def read_all_post(self):
        pass