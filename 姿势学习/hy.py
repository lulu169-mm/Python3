byte_data = [
    b'102', b'108', b'97', b'103', b'123', b'100',
    b'51', b'52', b'49', b'102', b'52', b'50',
    b'55', b'101', b'55', b'57', b'55', b'52',
    b'98', b'51', b'51', b'97', b'56', b'102',
    b'100', b'98', b'56', b'100', b'51', b'56',
    b'54', b'100', b'97', b'56', b'55', b'56',
    b'102', b'125'
]

# 将字节还原为ASCII字符
decoded_chars = [chr(int(byte)) for byte in byte_data]
result = ''.join(decoded_chars)

print(result)
