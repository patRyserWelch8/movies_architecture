from front_back_integration.communicate import IntegrationFrontBack
from integration_streamers.data_capture import Streamers


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def runProgram():
    stream_dream : IntegrationFrontBack = IntegrationFrontBack()
    print("Demonstration of User interaction with a human:")
    stream_dream.capture_and_insert_users()

    print("Demonstration of remote integration:")
    stream_dream.capture_and_insert_remote_data(Strea2mers.BIGFOREST)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    runProgram()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
