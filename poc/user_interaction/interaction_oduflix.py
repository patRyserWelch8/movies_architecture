class InteractionOduFlix:

    def __init__(self):
        self.title : str = None
        self.producer : str = None
        self.type  : str = None
        self.year  : int = 1900
        self.classifcation : str = None
        self.stars : int = 0
        self.actors : list = []
        self.country : str = None

    def input_flow(self):
        self._input_title()
        self._input_producer()
        self._input_year()
        self._input_type()
        self._input_classification()
        self._input_actors()
        self._input_country()
        self._input_stars()


    def _input_title(self) -> None:
        self.title = input ("What is the title? " )

    def _input_type(self) -> None:
        print("Romantic", "Science fiction", "Fantasy", "Horror", "Real life", "Suspence")
        self.type = input ("What is the type? " )

    def _input_classification(self) -> None:
        list_class : list = ['U', 'PG', "12A", '12', '15']
        print("Classification are : ", list_class)
        self.classifcation = input ("What is the classiviation? " )

    def _input_producer(self) -> None:
        self.producer = input ("Who is the producer? ")


    def _input_actors(self) -> None:
        print ("Who are the main actors ? ")
        actors : str = input("Please, separate the actors with a comma.")
        self.actors = actors.split(",")


    def _input_country(self) -> None:
        self.country = input ("What is the country? ")

    def _input_year(self) -> None:
        self.year = int(input("Which year was the film made?"))


    def _input_stars(self) -> None:
        self.stars = int(input("How many stars? 1 is poor and 5 is excellent"))
        if self.stars > 5:
            self.stars = 5

        if self.stars < 1:
            self.stars = 1




