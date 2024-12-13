# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Importation des modules utilisés
import sqlite3
import pandas

# Création de la connexion
conn = sqlite3.connect("Z:/BUT SD 2024-2025/NoSQL/ClassicModel.sqlite")

# Récupération du contenu de Customers avec une requête SQL
customers = pandas.read_sql_query("SELECT * FROM Customers;", conn)
print(customers)

Products = pandas.read_sql_query("SELECT * FROM Products;", conn)
print(Products)

Orders = pandas.read_sql_query("SELECT * FROM Orders;", conn)
print(Orders)

Offices = pandas.read_sql_query("SELECT * FROM Offices;", conn)
print(Orders)

Payments = pandas.read_sql_query("SELECT * FROM Payments;", conn)
print(Payments)

OrderDetails = pandas.read_sql_query("SELECT * FROM OrderDetails;", conn)
print(OrderDetails)

Employees = pandas.read_sql_query("SELECT * FROM Employees;", conn)
print(Employees)

## Lister les clients n’ayant jamais effecuté une commande 
order_customer = pandas.read_sql_query(
    """
    SELECT customerName
    FROM customers 
    LEFT JOIN Orders ON Customers.customerNumber = Orders.customerNumber
    Where orderNumber is null;
    """ , conn)
print(order_customer)

##Idem pour chaque bureau (nombre de clients, nombre de commandes et montant total), avec en plus le nombre de clients d’un pays différent, s’il y en a ;



# Fermeture de la connexion : IMPORTANT à faire dans un cadre professionnel
conn.close()







