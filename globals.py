import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class Globals(object):
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Globals.__instance == None:
            Globals()
        return Globals.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Globals.__instance != None:
            raise Exception("This class is a singleton!")
            # pass
        else:
            cred = credentials.Certificate(
                "big-brother-df0a9-firebase-adminsdk-fv0o6-90519d1867.json")
            # firebase_admin.initialize_app(cred)
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://big-brother-df0a9.firebaseio.com'})
            Globals.__instance = self


# class Globals(object):
    # """ A python singleton """

    # class __impl:
    #     """ Implementation of the singleton interface """

    #     def init(self):
    #         cred = credentials.Certificate(
    #             "big-brother-df0a9-firebase-adminsdk-fv0o6-90519d1867.json")
    #         # firebase_admin.initialize_app(cred)
    #         firebase_admin.initialize_app(cred, {
    #             'databaseURL': 'https://big-brother-df0a9.firebaseio.com'})

    # # storage for the instance reference
    # __instance = None

    # def __init__(self):
    #     """ Create singleton instance """
    #     # Check whether we already have an instance
    #     if Globals.__instance is None:
    #         # Create and remember instance
    #         Globals.__instance = Globals.__impl()

    #     # Store instance reference as the only member in the handle
    #     self.__dict__['_Globals__instance'] = Globals.__instance

    # def __getattr__(self, attr):
    #     """ Delegate access to implementation """
    #     return getattr(self.__instance, attr)

    # def __setattr__(self, attr, value):
    #     """ Delegate access to implementation """
    #     return setattr(self.__instance, attr, value)
