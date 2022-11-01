from app import login_manager
from models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

