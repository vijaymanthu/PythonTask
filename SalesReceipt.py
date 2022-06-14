class SalesReceipt:
    __sales_tax = 0.1
    def __init__(self,file):
        self.file = file
        self.inputs = []
        self.__total_cost = 0
        self.__total_sales_tax = 0
        self.tax = 0
        self.extractfile()

    def extractfile(self):
        with open(self.file, "r") as file:
            fileLines = file.readlines()  # read from input file

        for line in fileLines:
            item = []       # list of list of item-values

            item.append(int(line[0])) # quantity
            if "imported" in line:
                item.append('imported')
            else:
                item.append('')

            item.append(line[1: line.rindex("at")].strip())  # name
            item.append(float(line[line.rindex("at")+2:].strip()))  # price
            item.append(True if "book" in line or "chocolate" in line or "pills" in line else False) # exempted flag

            self.inputs.append(item)

    @classmethod
    def setSalesTax(cls, tax):
        cls.sales_tax = tax

    @classmethod
    def getSalesTax(cls):
        return cls.__sales_tax

    def rounded(self, x):
        return round(float(x) / 0.05) * 0.05

    def setTotalCost(self, val):
        self.__total_cost += val

    def getTotalCost(self):
        return self.__total_cost

    def calculateTaxAmount(self,cost, taxval):
        return self.rounded(cost * taxval)

    def getTotalSalesTax(self):
        return self.__total_sales_tax


    def calculatePrices(self):
        for i in range(len(self.inputs)):
            tax = 0
            quantity,goodstype, name, cost, exempted, = self.inputs[i]
            if not exempted:
                tax = self.calculateTaxAmount(cost, SalesReceipt.getSalesTax())
            if goodstype == "imported":
                tax += self.calculateTaxAmount(cost, 0.05)
            self.inputs[i][3] = round(cost + tax,2)
            self.setTotalCost(self.inputs[i][3])
            self.__total_sales_tax += tax

    def Receipt(self):
        for i in range(len(self.inputs)):
            print(f"{self.inputs[i][0]} {self.inputs[i][2]} :{self.inputs[i][3]}")

