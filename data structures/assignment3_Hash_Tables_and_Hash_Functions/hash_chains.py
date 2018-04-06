# python3
from itertools import chain
class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]
class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007
    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.elems = {}
    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return (ans % self.bucket_count + self.bucket_count) % self.bucket_count
    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')
    def write_chain(self, chain):
        print(' '.join(chain))
    def read_query(self):
        return Query(input().split())
    def process_query(self, query):
        if query.type == "check":
            if query.ind in self.elems:
                self.write_chain(cur for cur in reversed(self.elems[query.ind]))
            else:
                print(' ')
        else:
            hash_key = self._hash_func(query.s)
            ind = hash_key in self.elems
            if query.type == 'find':
                self.write_search_result(ind and query.s in self.elems[hash_key])
            elif query.type == 'add':
                if not ind:
                    self.elems[hash_key] = [query.s]
                else:
                    if not query.s in self.elems[hash_key]:
                        self.elems[hash_key].append(query.s)
            else:
                if ind and query.s in self.elems[hash_key]:
                    self.elems[hash_key].remove(query.s)
    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())
if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()