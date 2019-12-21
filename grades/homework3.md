Homework 3 Feedback
==================

Commit graded: b2fc050a430c943dc38e863960e259a72d78df54


### Incremental development using Git (5/10)
* -5, Ideally you should create separate commits (with detailed commit messages) for each independent change you make as you work. For example, you might have one commit for each view that you implement.

### Fulfilling the grumblr specification (16/20)
* -2, Users are unable to log out of the site. Linking to the login page is not the same as logging out.
* -2, Users are able to see Login/Register options on your Home page even though the user is already logged in

### Proper input validation (20/20)

### Request routing and configuration in Django (10/10)
* -0.1, Your application uses hard coded internal paths for your urls, or static files, a better practice would be to use the built in django static and url tags.

### Appropriate use of web application technologies in the Django framework (32/40)
* -5,  Unauthenticated users can access the stream and profile pages of your Grumblr site. You are not properly using `@login_required`.
* -1, The login page should not be shown for logged-in users. Consider redirecting them.
* -2, You do not explicitly use appropriate input type attributes. Password inputs should have `type="password"`

### Additional Information

---

#### Total score (83/100)

---

Graded by: David Yang (dzy@andrew.cmu.edu, dzy)

To view this file with formatting, visit the following page: https://github.com/CMU-Web-Application-Development/yueshanl/blob/master/grades/homework3.md

