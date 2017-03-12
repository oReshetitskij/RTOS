from sys import argv
import modules.databaseHelper as dbHelper
import numpy as np
import matplotlib.pyplot as plt
from sympy import integrate, limit
from sympy.abc import x
import math
import sqlite3



def main():
    # Init database
    conn = sqlite3.connect(dbHelper.databaseFilePath)
    conn.executescript(dbHelper.databaseDropOrCreateQuery)
    dbHelper.fillDatabase(conn)
    conn.commit()
    conn.close()





if __name__ == "__main__":
    main()
