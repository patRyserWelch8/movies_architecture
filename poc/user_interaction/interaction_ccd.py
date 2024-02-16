class InteractionCCD:

    def __init__(self):
        self.title: str = None
        self.type_program: str = None
        self.year: int = 1900
        self.classifcation: str = None
        self.category: str = None
        self.country: str = None
        self.channel: str = None

    def input_flow(self):
        self._input_title()
        self._input_year()
        self._input_type_program()
        self._input_classification()
        self._input_category()
        self._input_country()
        self._input_channel()

    def _input_title(self) -> None:
        self.title = input("What is the title? ")
        print(self.title)

    def _input_channel(self) -> None:
        self.channel = input("What is the channel? ")
        print(self.channel)

    def _input_classification(self) -> None:
        list_class: list = ['U', 'PG', "12A", '12', '15']
        print("Classification are : ", list_class)
        self.classifcation = input("What is the classiviation? ")
        print(self.classifcation)

    def _input_category(self) -> None:
        print("Romantic", "Science fiction", "Fantasy", "Horror", "Real life", "Suspence")
        self.category = input("What is the category? ")
        print(self.category)

    def _input_type_program(self) -> None:
        list_class: list = ['Series', 'Film', "News", 'Live', 'Documentatary']
        print("Programme types are : ", list_class)
        self.type_program = input("What is the programme type? ")
        print(self.type_program)

    def _input_country(self) -> None:
        self.country = input("What is the country? ")
        print(self.country)

    def _input_year(self) -> None:
        self.year = int(input("Which year was the film made?"))
        print(self.year)


