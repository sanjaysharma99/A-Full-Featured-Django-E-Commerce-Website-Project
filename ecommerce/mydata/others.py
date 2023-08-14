class categories:
    def __init__(self):
        from .models import Categories
        self.r1=Categories.objects.all()
        self.categories_list=[]
        for category in self.r1:
            self.categories_list.append((f'{category.category_slug}',f'{category.category_slug}'))

    def getlist(self):
        return self.categories_list