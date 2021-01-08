class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

        self.ordered_coll = []
        self.pages_1 = len(collection)//items_per_page

        for i in range(0, self.pages_1+1):
            if i == self.pages_1:
                self.ordered_coll.append(collection[self.pages_1*items_per_page:])
            else:
                self.ordered_coll.append(collection[(i*items_per_page):((i+1)*items_per_page)])

            if len(self.ordered_coll)*items_per_page == len(collection):
                break

    # returns the number of items within the entire collection

    def item_count(self):
        return len(self.collection)
    # returns the number of pages

    def page_count(self):
        return len(self.ordered_coll)
    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range

    def page_item_count(self, page_index):
        if page_index < len(self.ordered_coll)-1 and page_index >= 0:
            return len(self.ordered_coll[0])
        elif page_index == len(self.ordered_coll)-1:
            return len(self.ordered_coll[-1])
        else:
            return -1
    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range

    def page_index(self, item_index):
        if item_index < 0 or item_index >len(self.collection)-1:
            return -1
        else:
            return item_index // self.items_per_page

helper = PaginationHelper(['a','b','c','d','e','f','g','h','i','j','k'], 3)
print(helper.page_item_count(-1))