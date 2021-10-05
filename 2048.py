# 2048.py

import logic

# Driver code
if __name__ == '__main__':
mat = logic.start_game()

while(True):

	# taking the user input
	# for next step
	x = input("Press the command : ")

	# we have to move up
	if(x ==3):

		# call the move_up function
		mat, flag = logic.move_up(mat)

		# get the current state and print it
		status = logic.get_current_state(mat)
		print(status)

		# if game not ove then continue
		# and add a new two
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)

		# else break the loop
		else:
			break

	# moves

	# to move down
	elif(x == 4):
		mat, flag = logic.move_down(mat)
		status = logic.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		else:
			break

	# to move left
	elif(x == 1):
		mat, flag = logic.move_left(mat)
		status = logic.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		else:
			break

	# to move right
	elif(x == 2):
		mat, flag = logic.move_right(mat)
		status = logic.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		else:
			break
	else:
		print("Invalid Key Pressed")

	# print the matrix
	print(mat)
