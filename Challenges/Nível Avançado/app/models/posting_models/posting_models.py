from models.user_models.users_models import UserManager
from db.database import session, Posting, Tag
from datetime import datetime
import logging


class PostingManager:

    def create_post(email, category, title, post, image_url, tags):
        try:
            user = UserManager.filter_user(email)
            if user:

                tag = Tag(name=tags)

                new_post = Posting(
                    category=category,
                    title=title,
                    post=post,
                    image_url=image_url
                )

                user.posts.append(new_post)
                new_post.tags.append(tag)

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