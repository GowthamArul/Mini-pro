import functools

# user = {"username": "jose", "access_level": "guest"}

# def make_fun(func):
#     @functools.wraps(func)
#     def secure_fun():
#         if user['access_level'] == 'admin':
#             return func()
#         else:
#             return f"No admin permission for {user['username']}."
#     return secure_fun

# @make_fun
# def get_admin_pwd():
#     return "1234"

# #get_admin_pwd = make_fun(get_admin_pwd)

# print(get_admin_pwd.__name__)
# print(get_admin_pwd())

# ===================================

# Decorating function with parameters

# user = {"username": "jose", "access_level": "guest"}

# def make_fun(func):
#     @functools.wraps(func)
#     def secure_fun(*args, **kwargs):
#         if user['access_level'] == 'admin':
#             return func(*args, **kwargs)
#         else:
#             return f"No admin permission for {user['username']}."
#     return secure_fun

# @make_fun
# def get_pwd(panel): # taken panel as a decorator
#     if panel == "admin":
#         return "1234"
#     elif panel == "billing":
#         return "Super_secure_password"

# #get_admin_pwd = make_fun(get_admin_pwd)

# print(get_pwd.__name__)
# print(get_pwd("billing"))

# ======================================

# Decorators with parameters

user = {"username": "jose", "access_level": "guest"}

def make_fun(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_fun(*args, **kwargs):
            if user['access_level'] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permission for {user['username']}."
        return secure_fun
    return decorator

@make_fun('admin')
def get_admin_pwd():
    return "admin: 1234"

@make_fun('user')
def get_dashboard_pwd():
    return "user: user_password"

print(get_admin_pwd())
print(get_dashboard_pwd())
