{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}
# database_functions.py

import sqlite3

def create_database():
    connection = sqlite3.connect("phonebook.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone_number TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

def add_entry(name, phone_number):
    if name and phone_number:
        connection = sqlite3.connect("phonebook.db")
        cursor = connection.cursor()

        cursor.execute('''
            INSERT INTO Entries (name, phone_number) VALUES (?, ?)
        ''', (name, phone_number))

        connection.commit()
        connection.close()
        return True
    else:
        return False

def lookup_entry(name):
    if name:
        connection = sqlite3.connect("phonebook.db")
        cursor = connection.cursor()

        cursor.execute('''
            SELECT phone_number FROM Entries WHERE name = ?
        ''', (name,))

        result = cursor.fetchone()

        connection.close()

        return result[0] if result else None
    else:
        return None


    
