
def get_admin_pwd():
    return "1234"

def make_fun(func):
    def secure_fun():
        if user['access_level'] == 'admin':
            return func()
        else:
            return f"No admin permission for {user['username']}."
    return secure_fun

get_admin_pwd = make_fun(get_admin_pwd)
user = {"username": "jose", "access_level": "guest"}
print(get_admin_pwd())