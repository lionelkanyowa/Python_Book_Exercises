# Q.8 Explain why the code below prints different values on lines 3 and 4?

text = "It's probably pining for the fjords!"

# for the fjords
print(text[21:35].rfind('f')) # 8

# "It's probably pining for the fjords!"
print(text.rfind('f', 21, 35)) # 29


