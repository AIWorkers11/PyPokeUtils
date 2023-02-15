# PyPokeUtils

PyPokeUtilsでは、ポケモンの戦闘システムをPython上でプログラミングするときに便利な関数・クラスを提供します。

現在以下の関数をサポートしています。


## getNarureCorrection関数
 - 引数：性格（str,すべてひらがな）
 - 返り値：A-Sまでの補正値（list:float）

性格による補正値を得られます。

## getRankCorrection関数
 - 引数：ランク（int,-6～6）
 - 返り値：補正値（float）
 - 範囲外の数値は-1を出力
  
ランク変化による補正値を得られます。

## getPokemonStatus関数
 - 引数１：レベル(int)
 - 引数２：種族値（H～Sまでの値を含むlist:int）
 - 引数３：個体値（H～Sまでの値を含むlist:int）
 - 引数４：努力値（H～Sまでの値を含むlist:int）
 - 引数３：性格（str,すべてひらがな）
 - 返り値：H～Sまでのステータス（list:int）

レベル、種族値、個体値、努力値、性格からステータスを得られます。
