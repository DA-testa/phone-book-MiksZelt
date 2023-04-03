# python3
# Miks Zeltiņš  13.Grupa  221RDB123

class Query:
    def __init__(self, query):
        query_list = query.split()
        self.type = query_list[0]
        self.number = int(query_list[1])
        if self.type == 'add':
            self.name = query_list[2]

def read_queries():
    n = int(input())
    return [Query(input()) for i in range(n)]

def write_responses(responses):
    print('\n'.join(resposnes))

def process_queries(queries):
    responses = []
    contacts = {}
    
    for query in queries:
        if query.type == "add":
            contacts[query.number] = query.name
        elif query.type == "del":
            contacts.pop(query.number, None)
        elif query.type == "find":
            response = contacts.get(query.number, "not found")
            responses.append(response)
    return responses

if __name__ == '__main__':
    queries = read_queries()
    responses = process_queries(queries)