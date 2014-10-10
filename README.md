acu
===

Anti-Corruption University


## Setup

1. Install django 1.6
2. Checkout anti-corruption university - "git clone git@github.com:MayOneUS/acu.git"
3. In the root of the application, run "python manage.py syncdb". This will configure the database prompt you to set up an admin user. You can use this to login to the admin section, located at localhost:port/admin.
4. Again, in the root, run "python manage.py shell", followed by "exec(open('first_issue_questions.py'))"

This will create a code called "testcode" which will work to enter the application.
