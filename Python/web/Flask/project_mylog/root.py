import service.user_serv as user_serv
from app import create_app,db
from models.user import User
from sys import argv

# create user
# usage: python root.py admin password
# if __name__=='__main__':
#     app=create_app()
#     with app.app_context():
#         db.create_all()
#         user_serv.add_user_with_username_password(argv[1], argv[2])

#--------------------------------#

# get user info by usename
# usage: python root.py admin
if __name__=='__main__':
    app=create_app()
    with app.app_context():
        db.create_all()
        user=user_serv.get_by_username(argv[1])
        print(f'user info:\nusername:\t{user.username}\
            \npassword:\t{user.password}\npassword salt:\t{user.salt}')