import web
from Models import RegisterModel, LoginModel

web.config.debug = False
urls = (
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login',
    '/logout', 'Logout',
    '/postregistration', 'Postregistration',
    '/check-login', 'CheckLogin'
)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("session"), initializer={"user": None})
session_data = session._initializer

render = web.template.render("Views/Templates", base="MainLayout",
                             globals={"session": session_data, "current_user": session_data["user"]})


# Classes/Routes

class Home:
    def GET(self):
        return render.Home()


class Register:
    def GET(self):
        return render.Register()


class Login:
    def GET(self):
        return render.Login()


class Postregistration:
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data.username, data.name, data.email, data.password)


class CheckLogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data.username, data.password, data)
        if isCorrect:
            session_data["user"] = isCorrect
            return isCorrect

        return "error"


class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None
        session.kill()
        return "Logout Success"


if __name__ == "__main__":
    app.run()
