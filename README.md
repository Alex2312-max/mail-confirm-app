# Mail confirmation App

Application for mail confirmation, you need to create a valid mail and set the security settings to be accesible by low 
security apps. The application was implemented in the `app.py` file and the functions to send an email were implemented
in `mail.py`.

Templates contains several primitive `.html` files that are connected to the `app.py`. Also, `user_information.db` is the
database that stores:

  - First name;
  - Last name;
  - Email;
  
For security purposes I deleted the information about the Email I created, to be able to run this on `local` you need:

  1. Install `requirements.txt`
  2. Fill the information about `sender_mail` and `password`.
  
