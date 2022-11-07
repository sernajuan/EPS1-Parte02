# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:11:58 2022

@author: Serna
"""

import sqlite3
conexion = sqlite3.connect("bdalmacen.db")

tabla_producto ="""CREATE TABLE producto(
             idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
             codigo TEXT UNIQUE,
             nombre TEXT,
             precio REAL
             )
             """
cursor = conexion.cursor() 
cursor = conexion.execute(tabla_producto)
conexion.close()

