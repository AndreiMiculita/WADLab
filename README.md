# WADLab

Program for the Web Application development lab in my 3rd year at UPT. It's a pizzeria website. 
Some features:
* Static pages
* Product menu/news section linked to database
* User accounts
* Order system
* Admin interface

Setup:

    $ pip install requirements.txt
    $ python3 pizzasite/manage.py runserver 8000
    
Then visit either:
* `localhost:8000/pizza/` for client interface, or
* `localhost:8000/admin/` for admin interface (user `andrei` pwd `pizzaadmin`)
