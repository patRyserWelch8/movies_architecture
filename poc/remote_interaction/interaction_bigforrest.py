class InteractionBigForest:

    def __init__(self):
        self.title : str = None
        self.year  : int = 1900
        self.classifcation : str = None
        self.stars : int = 0
        self.country : str = None
        self.category : str = None
        self.rental : float = None
        self.purchase : float = None

    def input_flow(self):
        self._input_title()
        self._input_year()
        self._input_classification()
        self._input_category()
        self._input_country()
        self._input_rental()
        self._input_purchase()
        self._input_stars()

    def _input_title(self) -> None:
        self.title = input ("What is the title? " )

    def _input_category(self) -> None:
        print("Romantic", "Science fiction", "Fantasy", "Horror", "Real life", "Suspence")
        self.category = input("What is the category? ")

    def _input_classification(self) -> None:
        list_class : list = ['U', 'PG', "12A", '12', '15']
        print("Classification are : ", list_class)
        self.classifcation = input ("What is the classiviation? " )

    def _input_country(self) -> None:
        self.country = input ("What is the country? ")

    def _input_year(self) -> None:
        self.year = int(input("Which year was the film made?"))

    def _input_rental(self) -> None:
        self.rental = float(input("Rental cost : "))

    def _input_purchase(self) -> None:
        self.purchase = float(input("purchase cost : "))

    def _input_stars(self) -> None:
        self.stars = int(input("How many stars? 1 is poor and 5 is excellent"))
        if self.stars > 5:
            self.stars = 5

        if self.stars < 1:
            self.stars = 1




