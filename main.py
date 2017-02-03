
import webapp2
import cgi
import re

form = """
<form method='post'>
<table>
    <tr>
        <td>
        <h1>Signup</h1>
        </td>
    </tr>
    <tr>
        <td>
        <label>Username</label>
        </td>
        <td>
        <input type='text' name='user_username' value= '%(user_username)s'/>
        </td>
        <td><div style='color: red'>%(error_username)s</div>
        </td>
    </tr>
    <tr>
        <td><label>Password</label>
        </td>
        <td><input type='password' name='user_password'/>
        </td>
        <td><div style='color: red'>%(error_password)s</div>
        </td>
    </tr>
    <tr>
        <td><label>Verify Password</label>
        </td>
        <td><input type='password' name='user_verify_password'/> <div style='color: red'>%(error_verify_password)s</div>
        </td>



    </tr>
    <tr>
        <td><label>Email(optional)</label>
        </td>
        <td><input type='email' name='user_emailoptional' value='%(user_email)s'/>
        <div style='color: red'>%(error_email)s</div>
        </td>
    </tr>
    <tr>
        <td><input type='submit'/>
        </td>
    </tr>
</table>
</form>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return email or EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):
    def write_form(self, error_username="", error_password="", error_verify_password="", error_email="", user_username="", user_password="", user_email=""):
        self.response.out.write(form % {"error_username": error_username,
                                        "error_password": error_password,
                                        "error_verify_password": error_verify_password,
                                        "error_email": error_email,
                                        "user_username": user_username,
                                        "user_password": user_password,
                                        "user_email": user_email
                                        })

    def get(self):
        self.write_form()

    def post(self):
        have_error = False
        username = self.request.get("user_username")
        password = self.request.get("user_password")
        verify_password = self.request.get("user_verify_password")
        email = self.request.get("user_email")

        error_un = self.request.get("error_username")
        error_ps = self.request.get("error_password")
        error_vp = self.request.get("error_verify_password")
        error_em = self.request.get("error_email")

        if not valid_username(username):
            self.request.get(username)
            error_un = "That is not a valid username."
            have_error = True
        if not valid_password(password):
            error_ps = "That's not a valid password."
            have_error = True
        if password != verify_password:
            have_error = True
            error_vp = "Passwords don't match."
        if not valid_email(email):
            self.request.get(email)
            error_em = "That's not a valid email address."
            have_error = True

        if have_error:

            self.write_form(error_un, error_ps, error_vp, error_em, username, email)

        else:
            self.response.out.write("<h2>" + "Welcome, " + username + "!" + "</h2>")




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
