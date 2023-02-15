class Pokemon():
	def __init__(self,\
	index_num=0,nn="",level=0,nature="",\
	race_value=[0 for i in range(6)],\
	indivisual_value=[0 for x in range(6)],\
	effort_value=[0 for i in range(6)],held_item=""):
		self.__index_num = index_num		#図鑑番号
		self.__nn = nn				#ニックネーム
		self.__level = level 			#レベル
		self.__nature = nature
		self.__race_value = race_value		#種族値
		self.__indivisual_value = indivisual_value 		#個体値
		self.__effort_value = effort_value	#努力値
		self.__held_item = held_item		#もちもの
		self.__exp = level ** 3		#経験値（バトルシステム自体には不要。ここでは100万タイプ・端数切捨て）
	def getPokemonData(self):
		return [
            self.__index_num,
            self.__nn,
            self.__level,
            self.__nature,
            self.__race_value,
            self.__indivisual_value,
            self.__effort_value,
            self.__held_item,
            self.__exp
        ]

def getNatureCorrection(nature):
    nature_list = [
        ["さみしがり",1,2],["いじっぱり",1,3],["やんちゃ",1,4],["ゆうかん",1,5],
        ["ずぶとい",2,1],["わんぱく",2,3],["のうてんき",2,4],["のんき",2,5],
        ["ひかえめ",3,1],["おっとり",3,2],["うっかりや",3,4],["れいせい",3,5],
        ["おだやか",4,1],["おとなしい",4,2],["しんちょう",4,3],["なまいき",4,5],
        ["おくびょう",5,1],["せっかち",5,2],["ようき",5,3],["むじゃき",5,4],
        ["てれや",0,0],["がんばりや",0,0],["すなお",0,0],["きまぐれ",0,0],["まじめ",0,0],
    ]

    id = [x[0] for x in nature_list].index(nature)
    result = [1.0 for x in range(5)]
    if nature_list[id][1] == 0:
        pass
    else:
        result[nature_list[id][1]-1] = 1.1
        result[nature_list[id][2]-1] = 0.9

    return result

def getPokemonStatus(
    level,              #レベル
    race_value,         #種族値（６個のステータスを含むリスト型）
    indivisual_value,   #個体値（６個のステータスを含むリスト型）
    effort_value,       #努力値（６個のステータスを含むリスト型）
    nature):            #せいかく（文字列型）

    status=[
        	int((race_value[0] * 2 + indivisual_value[0] + int(effort_value[0] / 4.0)) * level / 100) + level + 20,
			int(int(int(race_value[1] * 2 + indivisual_value[1] + (effort_value[1] / 4.0)) * level / 100 + 5) * getNatureCorrection(nature)[0]),
			int(int(int(race_value[2] * 2 + indivisual_value[2] + (effort_value[2] / 4.0)) * level / 100 + 5) * getNatureCorrection(nature)[1]),
			int(int(int(race_value[3] * 2 + indivisual_value[3] + (effort_value[3] / 4.0)) * level / 100 + 5) * getNatureCorrection(nature)[2]),
			int(int(int(race_value[4] * 2 + indivisual_value[4] + (effort_value[4] / 4.0)) * level / 100 + 5) * getNatureCorrection(nature)[3]),
			int(int(int(race_value[5] * 2 + indivisual_value[5] + (effort_value[5] / 4.0)) * level / 100 + 5) * getNatureCorrection(nature)[4]),
    ]
    return status

def getTypeCorrection(attack_type,defence_type):
    type_table=["ノーマル","ほのお","みず","でんき","くさ","こおり","かくとう","どく","じめん","ひこう","エスパー","むし","いわ","ゴースト","ドラゴン","あく","はがね","フェアリー",]
    value_table=[
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-2, 0, 0,-1, 0, ],
        [ 0,-1,-1, 0, 1, 1, 0, 0, 0, 0, 0, 1,-1, 0,-1, 0, 1, 0, ],
        [ 0, 1,-1, 0,-1, 0, 0, 0, 1, 0, 0, 0, 1, 0,-1, 0, 0, 0, ],
        [ 0, 0, 1,-1,-1, 0, 0, 0,-2, 1, 0, 0, 0, 0,-1, 0, 0, 0, ],
        [ 0,-1, 1, 0,-1, 0, 0,-1, 1,-1, 0,-1, 1, 0,-1, 0,-1, 0, ],
        [ 0,-1,-1, 0, 1,-1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0,-1, 0, ],
        [ 1, 0, 0, 0, 0, 1, 0,-1, 0,-1,-1,-1, 1,-2, 0, 1, 1,-1, ],
        [ 0, 0, 0, 0, 1, 0, 0,-1,-1, 0, 0, 0,-1,-1, 0, 0,-2, 1, ],
        [ 0, 1, 0, 1,-1, 0, 0, 1, 0,-2, 0,-1, 1, 0, 0, 0, 1, 0, ],
        [ 0, 0, 0,-1, 1, 0, 1, 0, 0, 0, 0, 1,-1, 0, 0, 0,-1, 0, ],
        [ 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,-1, 0, 0, 0, 0,-2,-1, 0, ],
        [ 0,-1, 0, 0, 1, 0,-1,-1, 0,-1, 1, 0, 0,-1, 0, 1,-1,-1, ],
        [ 0, 1, 0, 0, 0, 1,-1, 0,-1, 1, 0, 1, 0, 0, 0, 0,-1, 0, ],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,-1, 0, 0, ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,-1,-2, ],
        [ 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 1, 0, 0, 1, 0,-1, 0,-1, ],
        [ 0,-1,-1,-1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,-1, 1, ],
        [ 0,-1, 0, 0, 0, 0, 1,-1, 0, 0, 0, 0, 0, 0, 1, 1,-1, 0, ],
    ]
    a_type_point = type_table.index(attack_type)
    d_type_point = type_table.index(defence_type)
    print(a_type_point,d_type_point)
    rank = value_table[a_type_point][d_type_point]
    if rank == 1:
        return 2.0
    elif rank == -1:
        return 0.5
    elif rank == -2:
        return 0.0
    else:
        return 1.0

def getRankCorrection(rank,is_critical=False):
    if rank < -7 or rank > 7:
        return -1   #エラー
    if is_critical == True and rank < 0:
        return 1
    elif rank < 0:
        return 2.0 / ( 2.0 + abs(rank))
    else:
        return 1.0 + abs(rank) / 2.0

if __name__ == "__main__":
    print(getTypeCorrection("かくとう","ゴースト"))