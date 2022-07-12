from ClassII import volume
length = int(input("请输入长:"))
width = int(input("请输入宽:"))
height = int(input("请输入高:"))

print(f"体积是：{volume(length, width, height).get_result()}")