from flask import Blueprint, request
from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    arg_keys = request.args.keys()
    id = request.args.get("id",default=None)
    name =  request.args.get("name",default=None)
    age =  request.args.get("age",default=None,type=int)
    occupation = request.args.get("occupation",default=None)
    result = []
    if  id and name and age and occupation :                
        result = [val for val in USERS if val["id"] == id or name in val["name"] or val["name"].find(name) or val["age"] == age or occupation in val["occupation"]]  
    elif name:  
         result = [val for val in USERS if  name in val["name"]]
    elif id and name:  
         result = [val for val in USERS if val["id"] == id or name in val["name"] ]  
    elif age:        
        result = [val for val in USERS if (val["age"] -1 ) == age or (val["age"] +1 ) == age or (val["age"]) == age  ]  
    elif occupation:        
        result = [val for val in USERS if occupation in val["occupation"]]  
    elif id:
        result = [val for val in USERS if val["id"] == id]  
    

    final_result = []
    for val in result:
        temp_data ={};  
        temp_other_data = {}
        for key in val:
            for keys in arg_keys:                   
                if key == keys:
                    temp_data[keys] = val[keys]
                else:
                    temp_other_data[key] = val[key]
        temp_data.update(temp_other_data)
        

        final_result.append(temp_data)
    return final_result
