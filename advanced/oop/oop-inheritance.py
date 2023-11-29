class Category:
    def __init__(self, category_name):
        self.category_name = category_name

    def get_category_info(self):
        return f'Category: {self.category_name}'


class Subcategory(Category):
    def __init__(self, category_name, subcategory_name):
        super().__init__(category_name)
        self.subcategory_name = subcategory_name

    def get_category_info(self):
        return f'{super().get_category_info()}, Subcategory: {self.subcategory_name}'


subcat = Subcategory('Monitor', 'IPS panel')

print(subcat.get_category_info())
print(subcat.category_name)
# print(subcat.get_subcategory_info())
