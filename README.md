# 🚰 Water Billing System (Django + Vue + Neon)

A full-stack water billing platform built with Django (REST API), Vue 3, and Neon PostgreSQL.

# 📸 Project Preview


# Dashboard

<img width="1351" height="645" alt="Dashboard" src="https://github.com/user-attachments/assets/3239007d-c29a-463b-8e8c-55dce6397ca5" />

# Clients


<img width="1330" height="639" alt="Client" src="https://github.com/user-attachments/assets/9419198a-2513-4c8a-8108-ce3f3e966610" />


# Meter Readings

<img width="1312" height="615" alt="Reading" src="https://github.com/user-attachments/assets/d3d4755d-f839-4fb7-84e2-6f51d6ca23a4" />

# Billing History


<img width="1351" height="550" alt="History" src="https://github.com/user-attachments/assets/d12fcfdd-e5b5-45a5-b146-8779efde31fb" />


# 🚀 Features

Your system actually covers many core billing operations, but here they are framed in a clean, professional way:

# 1. Dashboard

  Real-time stats: total clients, latest readings, billing summaries

  Summary widgets for quick monitoring

  Activity insights

# 2. Clients Module

  Add, edit, and delete clients

  Track client meter numbers

  View individual client billing info

  Searchable listing (fix this if your current one is slow)

# 3. Meter Readings

  Add new readings with validation

  Automatically fetch previous readings

  Prevent duplicate or reversed reading entries

  API-driven bill calculation

# 4. Billing History

  Full list of all generated bills

  Search + pagination

  Click-to-view detailed receipt

  Export capability (add CSV/PDF export if you want to impress)

# 5. Receipt Printing

  Clean, printable receipt layout

  Includes reading data, charges, totals, and client information

  Print-ready modal (don’t ship ugly receipts—design matters)

# 🏗️ Tech Stack


# Layer	                                                             
# Backend  Technology	and Notes

Django + Django REST Framework	                

This is the system’s core logic. It handles everything that actually matters behind the scenes.
# Frontend	 

Vue 3 + Composition API	                   
This is the visual side that the user interacts with.


# Database	   

Neon Serverless Postgres	                     
The storage layer — everything you save lives here.


# Auth	                       
JWT or session                                 
This is the communication pipe between frontend and backend.


# 🔌 API Endpoints

# Clients

      GET    /api/clients/


      POST   /api/clients/


      GET    /api/clients/<id>/


      PUT    /api/clients/<id>/


      DELETE /api/clients/<id>/

# Readings

      GET    /api/readings/

      
      POST   /api/readings/

      
# Billing
      POST   /api/clients/<id>/calculate-bill/

      
      GET    /api/billing-history/


# 🧑‍💻 Author

Nelson Kamau– Django/Vue Developer


Dedicated to building practical systems for SMEs and Kenyan utilities.

**How To Use The Django Template Repository**

env already installed


      env\Scripts\activate

      
Create your django project


      django-admin startproject project name .


Create django app


      python manage.py startapp appname


Register your apps in installed apps in settings.py ( in this case add 'restframework' and 'appname')
