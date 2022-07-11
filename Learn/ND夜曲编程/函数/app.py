# 函数 function
# 使用def 关键字，函数名后面要加小括号，小括号里可以不填，也可一写上参数

def customer(name: str,id: int):
    print(f'你好，您的账号成功注册,用户名是:{name},用户id是:{id}，感谢您的使用。')

customer("Tony",1121112)

def gameModeSelect(mode="survive", name="Steve", kill="True"):
    game = {
        mode: mode,
        name: name,
        kill: kill
    }
    return game

print(gameModeSelect())