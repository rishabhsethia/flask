
# @auth.verify_password
# def verify_password(username_or_token, password):
#     if request.path == "/api/login":
#         user = User.query.filter_by(username=username_or_token).first()
#         if not user or not user.verify_password(password):
#             return False
#     else:
#         user = User.verify_auth_token(username_or_token)
#         if not user:
#             return False    
#     g.user = user   
#     return True
