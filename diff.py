from out import questions_list
from mongo import mongo_db_connect
from kafka import KafkaProducer
from datetime import datetime
import json

#initiate mongodb connection
mongo_db = mongo_db_connect()

# print(questions_list)
for i in questions_list:
    print("i",i)
    collection = mongo_db['learning_objects']
    documents = collection.find(
        {
            'id': int(i),
            'type': 'Question'
        },
        {
            '_id': 0,
        }
    )
    if documents is None:
        query1 = None
    else:
        query1 = [i for i in documents]
    for i in query1:
        for j in i.keys():
            if isinstance(i[j],datetime):
                i[j] = str(i[j])
    producer = KafkaProducer(bootstrap_servers='10.144.20.35:9092',
                             value_serializer=lambda m: json.dumps(m).encode('ascii'))
    producer.send('CG_LEARNING_OBJECTS', query1)
    producer.flush()
    # timestr = datetime.now()
    # timestampStr = timestr.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    # with open('dsl_logging.txt', 'a') as f:
    #     for item in questions_list:
    #         f.write("%s--%s\n" % (item,timestampStr))
    # f.close()
print("completed")



