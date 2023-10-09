class MyList(list):
    """is a class under my list"""


    def print_sorted(self):
        """prints a list which is sorted"""
        l1 = self.copy()
        l1.sort()
        print(l1)
