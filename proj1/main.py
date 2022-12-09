# # P4 S12
# from data import teams
#
# def parsData(team):
# 	win = 0
# 	draw = 0
# 	lose = 0
# 	for tem in team['result']:
# 		if tem == 'w':
# 			win += 1
# 		if tem == 'l':
# 			draw += 1
# 		if tem == 'd':
# 			lose += 1
#
# 	return {
# 		'name': team['name'],
# 		'win': win,
# 		'draw': draw,
# 		'lose': lose,
# 		'score': (win * 3) + draw,
# 	}
#
# tmp_score_board = list(map(parsData, teams))
#
# passed_teams = list(
# 	filter(
# 		lambda t: t['score'] >= 50, tmp_score_board
# 		)
# 	)
#
# for index, team in enumerate(tmp_score_board):
# 	print(index+1, team)

