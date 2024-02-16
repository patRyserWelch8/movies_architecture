import json

from integration_streamers.data_capture import Streamers
from user_interaction.interaction import InteractionGeneral


class IntegrationFrontBack():

    def __init__(self):
        self.streamers: Streamers = Streamers()
        self.cli: InteractionGeneral = InteractionGeneral()


    def capture_and_insert(self):
        self.cli.input_flow()
        print("************")
        if self.cli.typeOfStream == Streamers.CCD:
            data : str      = self._transform_ccd
            self.streamers.insert_new_stream(data, Streamers.CCD)
        elif self.cli.typeOfStream == Streamers.ODUFLIX:
            data : str   = self._transform_oduflix
            self.streamers.insert_new_stream(data, Streamers.ODUFLIX)
        elif self.cli.typeOfStream == Streamers.BIGFOREST:
            data : str = self._transform_bigforest
            self.streamers.insert_new_stream(data,Streamers.BIGFOREST)


    @property
    def _transform_ccd(self) -> str:
        # Title, TypeProgram, Classification, Country, Year,
        # Category, Channel

        values: str = self.cli.ccd_ui.title + ","
        values  = values + self.cli.ccd_ui.type_program + ","
        values  = values + self.cli.ccd_ui.classifcation + ","
        values  = values + self.cli.ccd_ui.country + ","
        values  = values + str(self.cli.ccd_ui.year) + ","
        values  = values + self.cli.ccd_ui.category + ","
        values  = values +  self.cli.ccd_ui.channel
        return values

    @property
    def _transform_oduflix(self) -> str:
        # Title , Producer, Year, Classification, Stars,
        # Actors, Country

        values : dict = {}
        values.update({ "Title" : self.cli.oduflix_ui.title})
        values.update({ "Producer": self.cli.oduflix_ui.producer})
        values.update({ "Year": self.cli.oduflix_ui.year})
        values.update({ "Classification": self.cli.oduflix_ui.classifcation})
        values.update({ "Stars": self.cli.oduflix_ui.stars})
        values.update({ "Actors": self.cli.oduflix_ui.actors})
        values.update({ "Country": self.cli.oduflix_ui.country})
        values_str : str  = json.dumps(values)
        print(values_str)
        return values_str

    @property
    def _transform_bigforest(self) -> str:
        # Title, Year, Category, Rental, Purchase, Stars
        # Classification,  Country

        values: dict = {}
        values.update({"Title": self.cli.bigforest_ui.title})
        values.update({"Year": self.cli.bigforest_ui.year})
        values.update({"Category": self.cli.bigforest_ui.category})
        values.update({"Rental": self.cli.bigforest_ui.rental})
        values.update({"Purchase": self.cli.bigforest_ui.purchase})
        values.update({"Stars": self.cli.bigforest_ui.stars})
        values.update({"Classification": self.cli.bigforest_ui.classifcation})
        values.update({"Country": self.cli.bigforest_ui.country})
        values_str: str = json.dumps(values)
        print(values_str)
        return values_str

