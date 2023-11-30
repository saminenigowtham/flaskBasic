import pymongo


#step 1
conn_str="mongodb+srv://gouthamsamineni:goutham25704@cluster0.qq257ti.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(conn_str)
#step 2 create database
my_Db = client['LOR']
print("Data BAse created")
#step 3 create collection
my_Collection = my_Db['jobs']
print("colelction build")
# my_Db['jobs'].drop()
data_to_insert = [
    {   "id": 1,
        "title": "Software Engineer",
        "salary": 90000,
        "location": "San Francisco, CA",
        "experience": "2 years"
    },
    {   "id": 2,
        "title": "Data Scientist",
        "salary": 95000,
        "location": "New York, NY",
        "experience": "3 years"
    },
    {   "id": 3,
        "title": "UX/UI Designer",
        "salary": 80000,
        "location": "Los Angeles, CA",
        "experience": "2 years"
    },
    {  
      "id": 4,
      "title": "Project Manager",
      "salary": 100000,
      "location": "Chicago, IL",
      "experience": "5 years"
    },
    {  
      "id": 5,
      "title": "Network Administrator",
      "salary": 85000,
      "location": "Dallas, TX",
      "experience": "4 years"
    }
    # Add more documents as needed
]
# my_Collection.insert_many(data_to_insert)

# cursor =  my_Collection.find_one({"id": 1})
# if cursor:
#     print(cursor)
def get_all_jobs():
  cursor = my_Collection.find()
  
  # Collect data into a list of dictionaries
  job_data_list = []
  for document in cursor:
      job_data = {
          "id": document.get("id"),
          "title": document.get("title"),
          "salary": document.get("salary"),
          "location": document.get("location"),
          "experience": document.get("experience")
      }
      job_data_list.append(job_data)
  return job_data_list

# Print each document in the collection
# for document in Collected_Data:
#     print(document)
# print(client.list_database_names())
# print(my_Collection.find_one())