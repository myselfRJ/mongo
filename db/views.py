from pymongo import MongoClient
from django.http import HttpResponse ,JsonResponse


MONGODB_URL = "mongodb+srv://indra012:indra211@dummy.wrlvvb3.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGODB_URL)
db = client.djongo
collection = db.users


def Details(request,id,name,gender,age,isActive):
    details = {
        "_id": id,
        "Name": name,
        "Gender": gender,
        "Age":age,
        "isActive": isActive
    }
    res=collection.insert_one(details)

    return HttpResponse("data inserted sucessfully")


def Get_by_id(request, id):
    query = {"_id": id}
    result = collection.find_one(query)
    if result is not None:
        return JsonResponse(result)
    else:
        return HttpResponse("Document not found")

    
def Update_by_id(request,id,name,gender,age,isActive):
    query = {"_id":id}
    update = {"$set":{"Name":name,"Gender":gender,"Age":age,"isActive":isActive}}
    res = collection.update_one(query,update)
    updated = collection.find_one(query)
    response_data = {
            "message": "Updated Successfully",
            "result": updated
        }
    return JsonResponse(response_data,safe=False)
    
def Delete_by_id(request,id):
    data = []
    query = {"_id":id}
    collection.delete_one(query)
    all_data = collection.find()
    for cur in all_data:
        data.append(cur)
    responsed_data = {
        "message":"The Selected One Deleted then remaining data wiil be here",
        "res":data
    }
    return JsonResponse(responsed_data,safe=False)





