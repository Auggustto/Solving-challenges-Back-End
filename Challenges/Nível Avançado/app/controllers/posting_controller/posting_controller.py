from models.posting_models.post_models import PostingManager

class PostingController:
    def create_posting(email, category, post):

        if not all([email, category, post]):
            return {"error": "All fields are required"}, 400
        
        try:
            return PostingManager.create_post(email=email, category=category, post=post)
        
        except Exception as e:
            return {"error": str(e)}, 500