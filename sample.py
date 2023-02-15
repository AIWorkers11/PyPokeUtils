import pokeutils as pu		#pokeutiles.pyをソースファイルと同じディレクトリに入れて実行してください

if __name__ == "__main__":
	pikachu = pu.Pokemon(25,"ピカチュウ",50,"ひかえめ",[35,55,40,50,50,90],[31,31,31,31,31,31],held_item="でんきだま")
	
	print(pikachu.getPokemonData()[1])
	print(pu.getNatureCorrection(pikachu.getPokemonData()[3]))
	(
		level,
		race_value,
		indivisual_value,
		effort_value,
		nature
	) = (
		pikachu.getPokemonData()[2],
		pikachu.getPokemonData()[4],
		pikachu.getPokemonData()[5],
		pikachu.getPokemonData()[6],
		pikachu.getPokemonData()[3]
	)

	print(pu.getPokemonStatus(level,race_value,indivisual_value,effort_value,nature))
	#実行結果：ピカチュウ