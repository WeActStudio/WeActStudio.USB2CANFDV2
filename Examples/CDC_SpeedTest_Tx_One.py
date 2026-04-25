import serial

aux_device_ser = serial.Serial('COM45', 1152000, 8, 'N', 1,timeout=1)

aux_device_ser.write("S8\r".encode('utf-8'))
aux_device_ser.write("Y5\r".encode('utf-8'))
aux_device_ser.write("O\r".encode('utf-8'))
print('port_open ',aux_device_ser.port,aux_device_ser.read_until())

text_frame = "b000F"+"aabb"*32+"\r"
#text_frame = "t0000\r"
text_frame = text_frame*100
test_write = text_frame.encode('utf-8')
aux_device_ser.write(test_write)
print(aux_device_ser.read_until())

aux_device_ser.write("C\r".encode('utf-8'))
aux_device_ser.read_until(expected='\r'.encode('utf-8'))
aux_device_ser.close()