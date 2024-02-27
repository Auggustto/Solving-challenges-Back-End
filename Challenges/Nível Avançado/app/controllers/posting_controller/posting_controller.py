from models.posting_models.posting_models import PostingManager

class PostingController:
    def create_posting(email, category, title, post, image_url,tags):

        if not all([email, category, title, post]):
            return {"error": "All fields are required"}, 400
        
        try:
            return PostingManager.create_post(email=email, category=category, title=title, post=post, image_url=image_url, tags=tags)
        
        except Exception as e:
            return {"error": str(e)}, 500