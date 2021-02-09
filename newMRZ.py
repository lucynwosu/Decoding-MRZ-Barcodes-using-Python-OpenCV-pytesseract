from passporteye import read_mrz
import json
import sys
import datetime


def normalize_date ( mrz_date ) :
    dd = datetime.datetime.strptime ( mrz_date , '%y%m%d' ).strftime ( '%m/%d/%Y' )
    year = int ( str ( str ( dd ) [ -4 : ] ) [ -4 : ] )
    current_datetime = datetime.datetime.now ( )
    current_year = (format ( current_datetime.year ))
    if year > int ( current_year ) :
        dd = "".join ( (dd [ :4 ] , str ( year - 100 )) )
    return dd;


def get_given_name(name_split):
    try :
        first_name , middle_name = ' ', ' '
        first = name_split[ 0 ]
        try :
            middle = name_split[ 1 ]
        except (IndexError , UnboundLocalError) :
            print ( ' ' )
        else :
            middle_name = middle
    except (IndexError , UnboundLocalError) :
        print ( ' ' )
    else :
        first_name = first
        return first_name , middle_name;


def get_idType ( id ) :
    if id [ 0 ] == 'P' :
        id_type = 'Passport'
    elif id [ 0 ] == 'C' :
        id_type = 'Residency Card'
    elif id [ 0 ] == 'V' :
        id_type = 'Visa'
    elif id [ 0 :2 ] == 'IP' :
        id_type = 'US Passport Card'
    elif id [ 0 :2 ] == 'ID' :
        id_type = 'Non US Passport Card'
    else :
        id_type = 'Other'
    return id_type;


def process_passport(mrz):
    def process_passport(filename):
        mrz = read_mrz(filename, 1)
        if mrz is None:
            return "MRZ Barcode not found! Check your image and try again!"

        mrz_data = mrz.to_dict()
        dob = mrz_data['date_of_birth']
        doe = mrz_data['expiration_date']

    mrz_data = mrz.to_dict ( )
    date_of_birth = mrz_data [ 'date_of_birth' ]
    date_of_expiration = mrz_data [ 'expiration_date' ]
    id_type = mrz_data [ 'type' ]
    name = mrz_data [ 'names' ]
    name_split = name.split ( )
    first_name,  middle_name = get_given_name(name_split)

    data = {

        "first Name" : first_name,
        "Middle Name" : middle_name,
        "Surname" : mrz_data['surname'],
        "Date of Birth" : normalize_date(date_of_birth),
        "Gender" : mrz_data [ 'sex' ] ,
        "ID Type" : get_idType ( id_type ) ,
        "ID Number" : mrz_data [ 'number' ] ,
        "Date of Expiration" : normalize_date ( date_of_expiration ) ,
        "Nationality" : mrz_data [ 'nationality' ] ,

    }

    return data

mrz = read_mrz('C:\\Users\\User\Anaconda3\mrz\roi.jpg', 1)
data1 = process_passport(mrz)
print(data1)
#process_passport(mrz)