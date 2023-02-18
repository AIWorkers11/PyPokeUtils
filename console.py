from pokeutils import *

pokemon_list = [0]

def addPokemon(p: pokeutils.Pokemon):
    p2 = pokeutils.Pokemon()
    print(type(p2))
    if type(p) != pokeutils.Pokemon:
        return -1
    if pokemon_list[0] <= 6: 
        pokemon_list.append(p)
        pokemon_list[0] += 1
        print("ポケモンを設定しました。")
    else:
        print("6匹以上を指定することはできません。")

def StartUpprint():
    print("ポケットモンスター向けバトル開発用コンソール v0.1")
    print("Welcome the battle system console for Pokemon!")
    print("version 0.1")

def StartUpMenu():
    StartUpprint()
    while 1:
        command = input(ConsoleMes("コマンドを入力してください。:"))
        if command == "exit":
            print(ConsoleMes("終了します。"))
            break
        elif command =="set":
            SelectPokemonMenu()
        elif command == "start":
            Battle()
        else:
            print(ConsoleMes("存在しないコマンドです。","error"))

def ConsoleMes(mes,mtype="info"):
    if mtype == "info":
        return "[INFO]:"+mes
    elif mtype == "error":
        return "[ERROR]:"+mes
    elif mtype == "warning":
        return "[WARNING]:"+mes

def SelectPokemonMenu():
    print(ConsoleMes("ポケモン選択画面です。"))
    index_num = input(ConsoleMes("ポケモンの全国図鑑番号を入力してください。（半角数字）:"))
    try:
        index_num = int(index_num)
        print(index_num)
        pokemon_name = "ピカチュウ"
        while 1:
            yn = input(ConsoleMes(pokemon_name + "でよろしいですか?(y/n)"))
            if yn in ["y","Y"]:
                n = pokeutils.Pokemon(0,pokemon_name)
                addPokemon(n)
                break
            elif yn in ["n","N"]:
                print(ConsoleMes("操作が取り消されました。"))
                break
            else:
                print(ConsoleMes("値が不正です。再入力してください。","error"))

    except ValueError as v:
        print(v)
        print("[ERROR]:不正な値です。")

def BattleSetup():
    print(ConsoleMes("バトルのセットアップを開始します。"))
    print(ConsoleMes("使用するポケモンを6匹選択してください。"))
    pass

def Battle():
    print(ConsoleMes("バトル開始！"))
    print(ConsoleMes("バトル終了！"))

def ShowPokemon():
    pass
def CheckPokemon():
    pass
def Configure():
    pass

if __name__ == "__main__":
    StartUpMenu()