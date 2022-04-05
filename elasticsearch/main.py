from re import search
from functions import *
es = Elasticsearch("localhost:9200")
# create_index(es,"template","mapping")
# search_template(es,"search_template")
search_data(es,"index_test")
