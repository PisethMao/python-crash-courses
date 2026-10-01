data = b"Hello, World!"
test = bytes([72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33])
byte_array = bytearray(b"Hello, World!")
byte_array[7] = 119  # Change 'W' to 'w'
byte_array.append(33)  # Append '!' to the end of the bytearray
byte_array.extend(b" How are you?")  # Extend the bytearray with more bytes
view = memoryview(byte_array)  # Create a memory view of the bytearray
text = "កម្ពុជា"
text_bytes = text.encode("utf-8")  # Encode the string to bytes using UTF-8
hello = "សួស្តី"
hello_bytes = hello.encode("utf-8")  # Encode the string to bytes using UTF-8
print(data)        # Output: b'Hello, World!'
print(type(data))  # Output: <class 'bytes'>
print(test)        # Output: b'Hello, World!'
print(byte_array)  # Output: bytearray(b'Hello, World!')
print(view)       # Output: <memory at 0x...>
print(text_bytes)  # Output: b'\xe1\x9e\x80\xe1\x9e\x9f\xe1\x9e\x94\xe1\x9e\x9a\xe1\x9e\x8f'
print(hello_bytes.decode("utf-8"))  # Output: សួស្តី