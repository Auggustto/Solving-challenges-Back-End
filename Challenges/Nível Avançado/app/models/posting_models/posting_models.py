from models.user_models.users_models import UserManager
from db.database import session, Posting, Tag, LikeDislike
from datetime import datetime
import logging

from models.user_models.users_models import UserManager

class PostingManager:

    def filter_post(id):
        return session.query(Posting).filter_by(id=id).first()


    def create_post(email, category, title, post, image_url, tags):
        try:
            user = UserManager.filter_user(email)
            if user:
                new_post = Posting(
                    category=category,
                    title=title,
                    post=post,
                    image_url=image_url,
                )

                for tag_name in tags:
                    tag = session.query(Tag).filter_by(name=tag_name).first()
                    if not tag:
                        tag = Tag(name=tag_name)
                        session.add(tag)
                    new_post.tags.append(tag)

                user.posts.append(new_post)

                session.commit()

                return {"message": "Posting created successfully!"}, 201

        except Exception as e:
            session.rollback()
            logging.error(f"Error in create posting {e}")
            return {"error": str(e)}, 500
        

    def read_post(id):
        try:
            post = PostingManager.filter_post(id)
            if post:
                return post.as_dict()
            
            return {"error": "Posting not found!"}, 404
        
        except Exception as e:
            logging.error(f"Error posting not found {e}")
            return {"error": str(e)}


    def update_post(id, category, title, post, image_url, tags):
        try:
            post = PostingManager.filter_post(id)
            if post:
                post.category = category
                post.title = title
                post.image_url = image_url

                # Clear tags of posting
                post.tags.clear()

                for tag_name in tags:
                    tag = session.query(Tag).filter_by(name=tag_name).first()
                    if not tag:
                        tag = Tag(name=tag_name)
                        session.add(tag)
                    post.tags.append(tag)

                session.commit()

                return {"message": "Posting update sucessfully!"}, 200
            
            else:
                return {"error": "Posting not found!"}, 404
        
        except Exception as e:
            logging.error(f"Error update posting {e}")
            return {"error": str(e)}


    def delete_post(id):
        try:
            post = PostingManager.filter_post(id)
            if post:
                session.delete(post)
                session.commit()

                return {"message":"Posting deletede sucessfully!"}, 200
            
            return {"error": "Posting not found!"}, 404
        
        except Exception as e:
            session.rollback()
            logging.error(f"Error in delete post: {e}")

            return {"error": str(e)}, 500
        

    def read_all_post():
        try:
            select_all = session.query(Posting).all()

            if select_all:
                return [post.as_dict() for post in select_all]
            
            return {"error": "Posting not found!"}, 404
        
        except Exception as e:
            logging.error(f"Error reading all Posting: {e}")
            return {"error": str(e)}, 500


    def like_post(email, post_id):
        try:
            user = UserManager.filter_user(email)
            if user:
                post = session.query(Posting).filter_by(id=post_id).first()

                if post:
                    existing_like = session.query(LikeDislike).filter_by(user_id=user.id, posting_id=post.id).first()

                    if not existing_like:
                        like = LikeDislike(user_id=user.id, posting_id=post.id, like=True)
                        session.add(like)
                        session.commit()
                        return {"message": "Like added successfully!"}, 201
                    else:
                        return {"message": "User has already liked this post!"}, 400
                else:
                    return {"error": "Posting not found!"}, 404
            else:
                return {"error": "User not found!"}, 404
        except Exception as e:
            session.rollback()
            logging.error(f"Error liking post: {e}")
            return {"error": str(e)}, 500
        
    

    def dislike_post(email, post_id):
        try:
            user = UserManager.filter_user(email)
            if user:
                post = session.query(Posting).filter_by(id=post_id).first()

                if post:
                    existing_like = session.query(LikeDislike).filter_by(user_id=user.id, posting_id=post.id).first()

                    if not existing_like:
                        like = LikeDislike(user_id=user.id, posting_id=post.id, like=False)
                        session.add(like)
                        session.commit()
                        return {"message": "Deslike added successfully!"}, 201
                    else:
                        return {"message": "User has already liked this post!"}, 400
                else:
                    return {"error": "Posting not found!"}, 404
            else:
                return {"error": "User not found!"}, 404
            
        except Exception as e:
            session.rollback()
            logging.error(f"Error liking post: {e}")
            return {"error": str(e)}, 500



