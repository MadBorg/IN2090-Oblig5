import psycopg2

# MERK: Må kjøres med Python 3

user = 'sanders' # Sett inn ditt UiO-brukernavn ("_priv" blir lagt til under)
pwd = 'Jie0taom4s' # Sett inn passordet for _priv-brukeren du fikk i en mail

connection = \
    "dbname='" + user + "' " +  \
    "user='" + user + "_priv' " + \
    "port='5432' " +  \
    "host='dbpg-ifi-kurs.uio.no' " + \
    "password='" + pwd + "'"

def administrator():
    conn = psycopg2.connect(connection)
    
    ch = 0
    while (ch != 3):
        print("-- ADMINISTRATOR --")
        print("Please choose an option:\n 1. Create bills\n 2. Insert new product\n 3. Exit")
        ch = int(input("Option: "))

        if (ch == 1):
            make_bills(conn)
        elif (ch == 2):
            insert_product(conn)

def make_bills(conn):
    cur = conn.cursor()
    print("-- BILLS --  ")
    username = input("Username: ") or None

    # quary
    # Name, adress, total due. From orders.
    if username:
        select = ("name", "address", "Total due")
        q = f"""
            SELECT u.name, u.address, SUM(o.num * p.price)
            FROM ws.orders AS o
            INNER JOIN ws.products AS p
                USING(pid)
            INNER JOIN ws.users AS u
                USING(uid)
            WHERE o.payed = 0 AND u.username = '{username}'
            GROUP BY u.uid, u.name, u.address;
            """
    else:
        select = ("Total due")
        q = f"""
            SELECT SUM(o.num * p.price)
            FROM ws.orders AS o
            INNER JOIN ws.products AS p
                USING(pid)
            WHERE o.payed = 0;
            """
    cur.execute(q)
    rows = cur.fetchall() # Retrieve all restults into a list of tuples
    bill = dict(zip(select, rows[0]))
    # print(f"bill: {bill}")
    # print(f"select:{select}, rows:{rows}")
    print("-- BILL --")
    for key in bill:
        print(f"{key}: {bill[key]}")
    

    
def insert_product(conn):
    # TODO
    raise NotImplementedError()


if __name__ == "__main__":
    administrator()
