class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = query[1]
        if self.type == "add":
            self.name = query[2]

    def __repr__(self):
        suffix = ")" if not hasattr(self, "name") else f", name={self.name!r})"
        return (
            f"{type(self).__name__}(type={self.type!r}, number={self.number!r}" + suffix
        )


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def process_queries(queries):
    result = []
    phone_db = {}
    for query in queries:
        if query.type == "add":
            phone_db[query.number] = query.name
        elif query.type == "del":
            # remove this element silently
            phone_db.pop(query.number, None)
        else:
            result.append(phone_db.get(query.number, "not found"))
    return result


if __name__ == "__main__":
    for r in process_queries(read_queries()):
        print(r)
