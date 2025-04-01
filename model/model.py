from database.DAO import DAO

class Model:
    def __init__(self):
        pass

    def getProdotti(self):
        return DAO.getProdotti()

    def getMetodi(self):
        return DAO.getMetodi()

    def getRetailer(self):
        return DAO.getRetailer()

    def getAnni(self):
        return DAO.getAnni()

    def getBrand(self):
        return DAO.getBrand()

    def getVendite(self, anno, brand, retailer):
        return DAO.getVenditeCondizionate(anno, brand, retailer)

    def getVenditeAnalizza(self, anno, brand, retailer):
        return DAO.getVenditeAnalizza(anno, brand, retailer)