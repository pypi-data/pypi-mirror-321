# def callback(a, b):
#     print('Sum = {0}'.format(a+b))
#
# def main(a,b,f=None):
#     print('Add any two digits.')
#     if f is not None:
#         f(a,b)
#
# main(1, 2, callback)



from langchain_text_splitters import RecursiveJsonSplitter

json_data = {
    "complex_key": {
        "nested_key": [
            {"item1": "value1"},
            {"item2": "value2"},
            {"item3": "value3"}
        ]
    },
    "another_key": "some_value"
}

splitter = RecursiveJsonSplitter(max_chunk_size=5)
json_chunks = splitter.split_json(json_data)

print(json_chunks)