from user_interaction.interaction_bigforrest import InteractionBigForest
from user_interaction.interaction_ccd import InteractionCCD
from user_interaction.interaction_oduflix import InteractionOduFlix


class InteractionGeneral(object):
    CCD = 0
    ODUFLIX = 1
    BIGFOREST = 2
    def __init__(self):
        self.typeOfStream: int = -1
        self.oduflix_ui : InteractionOduFlix     = InteractionOduFlix()
        self.ccd_ui : InteractionCCD             = InteractionCCD()
        self.bigforest_ui : InteractionBigForest = InteractionBigForest()


    def _input_typeOfStream(self) -> None:
        type : int = int(input("Streaming platform: 0 - CCD, 1 - OduFlix, 2 - BigForest "))
        if type in [0,1,2]:
            print(type , "is a correct choice")
            self.typeOfStream = type
        else:
            print('Incorrect')

    def input_flow(self) -> None:
        self._input_typeOfStream()
        if self.typeOfStream == InteractionGeneral.CCD:
            self.ccd_ui.input_flow()
        elif self.typeOfStream == InteractionGeneral.ODUFLIX:
            self.oduflix_ui.input_flow()
        elif self.typeOfStream == InteractionGeneral.BIGFOREST:
            self.bigforest_ui.input_flow()



