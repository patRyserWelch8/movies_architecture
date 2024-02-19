from front_back_integration.communicate import IntegrationFrontBack
from integration_streamers.data_capture import Streamers

DreamStream: IntegrationFrontBack = IntegrationFrontBack()


DreamStream.capture_and_insert_remote_data(Streamers.BIGFOREST)
