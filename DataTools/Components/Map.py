class Map(object):
    def __init__(self, index, img):
        self.index = index
        self.img = img


class normalEstate(Map):
    def __init__(self, index, img, price, owner, numberOfHouses, roadToll):
        Map.__init__(self, index, img)
        self.price = price
        self.owner = owner
        self.numberOfHouses = numberOfHouses
        self.roadToll = roadToll

class ChancesDestinies(Map):
    def __init__(self,index,img,noOfCards):
        Map.__init__(self,index,img)
        self.noOfCards = noOfCards

class specialEstate(normalEstate):
    def __init__(self, index, img, price, owner, numberOfHouses, roadToll):
        normalEstate.__init__(self, index, img, price, owner, numberOfHouses, roadToll)