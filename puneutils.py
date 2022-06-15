import pickle
import json
import numpy as np
import math
import warnings
warnings.filterwarnings("ignore")

def get_estimatedprice(seller_type,bedroom,layout_type,property_type,locality,area,furnish_type,bathroom):
    try:
        loc_index1 = __data_columns.index(seller_type.lower())
        loc_index2 = __data_columns.index(layout_type.lower())
        loc_index3 = __data_columns.index(property_type.lower())
        loc_index4 = __data_columns.index(locality.lower())
        loc_index5 = __data_columns.index(furnish_type.lower())
    except:
        loc_index1 = -1
        loc_index2 = -1
        loc_index3 = -1
        loc_index4 = -1
        loc_index5 = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = bedroom
    x[1] = area
    x[2] = bathroom
    if loc_index1 >= 0:
        x[loc_index1] = 1
    if loc_index2 >= 0:
        x[loc_index2] = 1
    if loc_index3 >= 0:
        x[loc_index3] = 1
    if loc_index4 >= 0:
        x[loc_index4] = 1
    if loc_index5 >= 0:
        x[loc_index5] = 1   

    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations

def get_seller_details():
    return __seller

def get_nature():
    return __nature

def get_typeofstay():
    return __typeofstay

def get_furniture():
    return __furniture


def loading():
    print("Loading Datas......")
    global __data_columns
    global __locations
    global __seller
    global __nature
    global __typeofstay
    global __furniture

    with open("PuneColumns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:129]
        __seller = __data_columns[129:132]
        __nature = __data_columns[132:134]
        __typeofstay = __data_columns[134:140]
        __furniture = __data_columns[140:143]

    global __model
    with open("Pune_Accomodation_Rent_Price_Prediction_Model.pkl",'rb') as f:
        __model = pickle.load(f)
    print("Loading Model.....")


def starting(seller_type,bedroom,layout_type,property_type,locality,area,furnish_type,bathroom):
    loading()
    return get_estimatedprice(seller_type,bedroom,layout_type,property_type,locality,area,furnish_type,bathroom)

if __name__ == '__main__':
    loading()
    print(get_estimatedprice('agent',2, 'bhk', 'independent house','birati',2600,'furnished',2))
