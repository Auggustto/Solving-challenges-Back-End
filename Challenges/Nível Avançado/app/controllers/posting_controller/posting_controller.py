from models.posting_models.posting_models import PostingManager

class PostingController:

    def create_posting(email, category, title, post, image_url,tags):

        if not all([email, category, title, post]):
            return {"error": "All fields are required"}, 400
        
        try:
            return PostingManager.create_post(email=email, category=category, title=title, post=post, image_url=image_url, tags=tags)
        
        except Exception as e:
            return {"error": str(e)}, 500
        

    def read_posting(id):
        if not id:
            return {"error": "ID are required"}, 400
        
        try:
            return PostingManager.read_post(id=id)
        except Exception as e:
            return {"error": str(e)}


    def update_posting(id, category, title, post, image_url, tags):

        if not all([id, category, title, post, image_url, tags]):
            return {"error": "All fields are required"}, 400
        
        try:
            return PostingManager.update_post(id, category, title, post, image_url, tags)
        
        except Exception as e:
            return {"error": str(e)}
        

    def delete_posting(id):
        if not id:
            return {"error": "ID are required"}, 400
        
        try:
            return PostingManager.delete_post(id=id)
        
        except Exception as e:
            return {"error": str(e)}, 500
        
    
    def read_all_posting():
        try:
            return PostingManager.read_all_post()
        
        except Exception as e:

            return {"error": str(e)}
        
    
    def like_posting(email, posting_id):
        try:
            return PostingManager.like_post(email, posting_id)
        
        except Exception as e:

            return {"error": str(e)}
        
    
    def dislike_posting(email, posting_id):
        try:
            return PostingManager.dislike_post(email, posting_id)
        
        except Exception as e:

            return {"error": str(e)}