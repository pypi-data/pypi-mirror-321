"""
utopia_pipeline_tools: a set of modules to streamline the process of converting
raw IFCB data to CNN-classified and validated datasets. 
"""

# a bit of metadata
__version__ = '0.3.15'
__author__ = 'Claire Berschauer'
__credits__ = 'Applied Physics Laboratory - UW'

# global attributes
label_dict = {'Chloro': 0,
              'Cilliate': 1,
              'Crypto': 2,
              'Diatom': 3,
              'Dictyo': 4,
              'Dinoflagellate': 5,
              'Eugleno': 6,
              'Other': 7,
              'Prymnesio': 8,
              'Null': 9
             }

label_list = list(label_dict.keys())

aphiaID_dict = {0: ['Chlorophyta', 801],
                1: ['Ciliophora', 11],
                2: ['Cryptophyceae', 17639],
                3: ['Bacillariophyceae', 148899],
                4: ['Dictyochophyceae', 157256],
                5: ['Dinophyceae', 19542],
                6: ['Euglenoidea', 582177],
                7: ['Biota', 1],
                8: ['Prymnesiophyceae', 115057],
                9: ['Null', -9999]
                }

calibration_ratio = 2.7488  # pixels/um (feature extraction v4 value)
# or 3.4 if using the feature extraction v2

config_info = {"blob_storage_name": None,
               "connection_string": None,
               "server": None,
               "database": None,
               "db_user": None,
               "db_password": None,
               'subscription_id': None,
               'resource_group': None,
               'workspace_name': None,
               'experiment_name': None,
               'api_key': None,
               'model_name': None,
               'endpoint_name': None,
               'deployment_name': None,
               }

default_investigators = {"Firstname_Lastname": ['Organization', 'email@org.com'],
                         "Firstname_Lastname": ['Organization', 'email@org.com'],
                         }