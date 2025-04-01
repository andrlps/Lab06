from database.DB_connect import DBConnect
from model.metodi import Metodo
from model.vendite import Vendita
from model.prodotti import Prodotto
from model.retailer import Retailer


class DAO():
    def __init__(self):
        raise RuntimeError('Do not create an instance, use the class method get_connection()!')

    @staticmethod
    def getProdotti():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM go_products")
        prodotti = dict()
        for row in cursor:
            number = row['Product_number']
            line = row['Product_line']
            type = row['Product_type']
            product = row['Product']
            brand = row['Product_brand']
            color = row['Product_color']
            cost = row['Unit_cost']
            price = row['Unit_price']
            prodotti[number] = Prodotto(number, line, type, product, brand, color, cost, price)
        cursor.close()
        cnx.close()
        return prodotti

    @staticmethod
    def getMetodi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM go_methods")
        metodi = dict()
        for row in cursor:
            method = row['Order_method_code']
            type = row['Order_method_type']
            metodi[method] = Metodo(method, type)
        cursor.close()
        cnx.close()
        return metodi

    @staticmethod
    def getRetailer():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM go_retailers")
        retailer = dict()
        for row in cursor:
            code = row['Retailer_code']
            name = row['Retailer_name']
            type = row['Type']
            country = row['Country']
            retailer[code] = Retailer(code, name, type, country)
        cursor.close()
        cnx.close()
        return retailer

    @staticmethod
    def getAnni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT DISTINCT YEAR(Date) FROM go_daily_sales")
        anni = []
        for row in cursor:
            anni.append(row['YEAR(Date)'])
        cursor.close()
        cnx.close()
        return anni

    @staticmethod
    def getBrand():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("select distinct Product_brand from go_products")
        brand = []
        for row in cursor:
            brand.append(row['Product_brand'])
        cursor.close()
        cnx.close()
        return brand

    @staticmethod
    def getVenditeCondizionate(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = ("""SELECT gds.Retailer_code, gds.Product_number, gds.Order_method_code, 
                    gds.Date, gds.Quantity, gds.Unit_price, gds.Unit_sale_price, 
                    (Quantity * Unit_sale_price) AS Total_Sales
                    FROM go_daily_sales gds, go_products gp 
                    WHERE gds.Product_number = gp.Product_number AND
                    YEAR(Date)=COALESCE(%s, YEAR(Date)) 
                    AND gds.Retailer_code = COALESCE(%s, gds.Retailer_code)
                    AND gp.Product_brand = COALESCE(%s, gp.Product_brand)
                    ORDER BY Total_Sales DESC LIMIT 5""")
        cursor.execute(query, (anno, retailer, brand,))
        vendite = []
        for row in cursor:
            code = DAO.getRetailer()[row['Retailer_code']]
            product = DAO.getProdotti()[row['Product_number']]
            method = DAO.getMetodi()[row['Order_method_code']]
            date = row['Date']
            quantity = row['Quantity']
            price = row['Unit_price']
            sale_price = row['Unit_sale_price']
            vendite.append(Vendita(code, product, method, date, quantity, price, sale_price))
        cursor.close()
        cnx.close()
        return vendite

    @staticmethod
    def getVenditeAnalizza(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = ("""SELECT gds.Retailer_code, gds.Product_number, gds.Order_method_code, 
                    gds.Date, gds.Quantity, gds.Unit_price, gds.Unit_sale_price, 
                    (Quantity * Unit_sale_price) AS Total_Sales
                    FROM go_daily_sales gds, go_products gp 
                    WHERE gds.Product_number = gp.Product_number AND
                    YEAR(Date)=COALESCE(%s, YEAR(Date)) 
                    AND gds.Retailer_code = COALESCE(%s, gds.Retailer_code)
                    AND gp.Product_brand = COALESCE(%s, gp.Product_brand)""")
        cursor.execute(query, (anno, retailer, brand,))
        ris = {
        'prodotti': [],
        'retailers': [],
        'numero': 0,
        'ricavi': 0}
        for row in cursor:
            ris['numero'] += 1
            code = row['Retailer_code']
            if code not in ris['retailers']:
                ris['retailers'].append(code)
            product = row['Product_number']
            if product not in ris['prodotti']:
                ris['prodotti'].append(product)
            quantity = row['Quantity']
            sale_price = row['Unit_sale_price']
            ris['ricavi'] += quantity*sale_price
        cursor.close()
        cnx.close()
        return ris

if __name__ == '__main__':
    print(DAO.getVenditeCondizionate(2017, "Star", None))
    print(DAO.getVenditeCondizionate(2017, "Star", None))
