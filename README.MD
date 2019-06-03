### NEIGHBOURHOOD
This is an application that allows users in an area to interact with other people who also live in the same area. The users can look up businesses in that area and also create posts that let the other neighbours know of the happenings in the nieghbourhood.

### By Ephraim Kamau

### Description
This is an application that allows users in an area to interact with other people who also live in the same area. Users an create posts that details what is going on within the neighbourhood and also create posts that detail businesses located in that area. Users can also find the contacts for the local police authorities and health centres.

### Setup/Installation Requirements
- Ensure you have Python3.6 installed.
- Clone the Neighbourhoods directory.
- Create your own virtual environment and activate it using these respective commands `python3.6 -m venv --without-pip virtual` and  `source virtual/bin/activate`
- Install all the necessary dependencies necessary for running the application using this command `pip install -r requirements.txt`
- Open the terminal and run this command `psql` You can then create a database by running this command
`CREATE DATABASE hood`
- Run migrations using these respective commmands `python3.6 manage.py makemigrations projects` then `python3.6 manage.py migrate`
- Run the app using this command `python3.6 manage.py runserver` on the terminal.You can then open the app on your browser.


### Technologies Used
<ul>
<li>Python 3.6</li>
<li>Django</li>
<li>Heroku</li>
<li>Bootstrap</li>
<li>HTML</li>
</ul>

### Support and Contact Details
For more information, questions, or feedback, get in touch with me on +254 710 700358 or email: kephraim19@gmail.com

### Licence
Copyright(c) 2019 Ephraim Kamau