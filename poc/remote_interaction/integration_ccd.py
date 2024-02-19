class IntegrationCCD:

    def __init__(self):
        self.title: str = None
        self.type_program: str = None
        self.year: int = 1900
        self.classifcation: str = None
        self.category: str = None
        self.country: str = None
        self.channel: str = None

    def ingest(self):

    def set_title(self, title: str) -> None:
        self.title = title

    def set_channel(self, channel: str) -> None:
        self.channel = channel

    def set_classification(self, classification: str) -> None:
        list_class: list = ['U', 'PG', "12A", '12', '15']
        if classification in list_class:
            self.classifcation = classification
        else:
            self.classifcation = 'Unknown'

    def set_category(self, category: str) -> None:
        list_cat: list = ["Romantic", "Science fiction", "Fantasy", "Horror", "Real life", "Suspence"]
        if category in list_cat:
            self.category = category
        else:
            self.category = "Unknown"

    def set_program(self, program: str) -> None:
        list_programmes: list = ['Series', 'Film', "News", 'Live', 'Documentatary']
        if program in list_programmes:
            self.type_program = list_programmes
        else:
            self.type_program = "Unknown"

    def set_country(self, country: str) -> None:
        self.country = country

    def set_year(self, year: int) -> None:
        self.year = year

