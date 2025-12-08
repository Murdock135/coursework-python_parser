from antlr4 import InputStream

input_stream = InputStream("abc")
print(input_stream.LA(1))  # What character?
print(input_stream.LA(2))  # What character?
print(input_stream.LA(3))  # What character?