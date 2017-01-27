
#
import webapp2
import cgi


def build_page(self):
    header = "<h2>Signup</h2>"

    username_label = "<label>Username</label>"
    username_input = "<input type='text' name='username'/>"

    password_label = "<label>Password</label>"
    password_input = "<input type='text' name='password'/>"

    verify_password = "<label>Verify Password</label>"
    verify_password_input = "<input type='text' name='verifypassword'/>"

    email_optional = "<label>Email(optional)</label>"
    email_optional_input = "<input type='text' name='emailoptional'/>"

    submit = "<input type='submit'/>"
    form = ("<form method='post'>" + header + username_label + username_input
            + "<br>" + password_label + password_input + "<br>"
            + verify_password + verify_password_input + "<br>"
            + email_optional + email_optional_input + "<br>" + submit)

    "<table>"
  "<tr>"
    "<th>username_label</th>"
    "<th>username_input</th>"
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
  <tr>
    <td>February</td>
    <td>$80</td>
  </tr>
</table>

    return form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify_password = self.request.get("verify_password")
        email_optional = self.request.get("email_optional")
        escaped_form = cgi.escape(username + password + verify_password + email_optional)
        content = build_page(escaped_form)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
