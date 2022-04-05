from elasticsearch import Elasticsearch,helpers
import json
def create_index(name,mapping,es):
    index = name
    with open(f'C:/Users/pop24/Desktop/source_code/python/elasticsearch/mapping/{mapping}.json','r') as f: #미리 mapping type을 json으로 저장해서 사용
        mapping = json.load(f)
    es.index(index=index,body=mapping)

def search_template(es,templates):
    with open(f'C:/Users/pop24/Desktop/source_code/python/elasticsearch/mapping/{templates}.json','r') as f: #미리 search_template을 json으로 저장해서 사용
        body = json.load(f)
    es.put_script(id='search_template', body=body)
    return body



def get_info(floor,addr,cate,site,name):
    body = {
    "id" : "search_template",
    "params" : {
      "floor_level" : floor,
      "address" : addr,
      "address_operator" : "or",
      "category" : cate,
      "category_operator" : "or",
      "site_name" : site,
      "store_name" : name
        }
    }
    return body
 

def search_data(es,name):
    floor = input("층");addr = input("주소");cate = input("분류");site = input("지점");name = input("상호")
    body = get_info(floor,addr,cate,site,name)
    results = es.search_template(index=name, body = body)
    print(results)
    


