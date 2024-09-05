class Categories:
    def __init__(self,created_date,cat_name,cat_id) -> None:
        self.created_date = created_date
        self.cat_name = cat_name
        self.cat_id = cat_id

class Item:
    def __init__(self, created_date: str, price : int, item_name : str, original_price : int, Item_id: str,category : Categories) -> None:
        self.created_date = created_date
        self.price = price
        self.item_name = item_name
        self.Original_price = original_price
        self.id = Item_id
        self.category = category

        def getProfit(sefl):
            return int(self.price - self.Original_price)

class saleItem:
    def __init__(self, created_date: str,customer_id: int, item: Item) -> None:
        self.created_date = created_date
        self.cs_id = customer_id
        self.item = item

        def getCategoryAndProfit(sefl):

            return self.item.category.cat_name,self.item.item_name,self.item.getProfit()