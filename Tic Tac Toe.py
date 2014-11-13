
def print_board():
    for i in range(0,3):
        for j in range(0,3):
            print map[2-i][j],
            if j != 2:
                print "|",
        print ""


def check_done():
    for i in range(0,3):
        if map[i][0] == map[i][1] == map[i][2] != " " \
        or map[0][i] == map[1][i] == map[2][i] != " ":
            print turn, "won!!!"
            return True
    
    if map[0][0] == map[1][1] == map[2][2] != " " \
    or map[0][2] == map[1][1] == map[2][0] != " ":
        print turn, "won!!!"
        return True
    
    if " " not in map[0] and " " not in map[1] and " " not in map[2]:
        print "Draw"
        return True
    
    
    return False

def check_first():
    if turn_computer == "X":
        return turn_computer
    if turn_player == "X":
        return turn_player

def computer_play():
    moved = False
    done = False
    while moved != True:
        for i in range(0,3):
            if map[i][0] == map[i][1] == turn_computer != " ":
                if map[i][2] ==" ":
                    map[i][2] = turn_computer
                    moved = True
                    done = check_done()
                    if done == False:
            			return turn == turn_player
                    else:
                        return
            elif map[0][i] == map[1][i] == turn_computer != " ":
				if map[2][i] ==" ":
					map[2][i] = turn_computer
					moved = True
					done = check_done()
					if done == False:
						return turn == turn_player
					else:
						return

            elif map[i][0] == map[i][2] == turn_computer != " ":
                if map[i][1] ==" ":
                    map[i][1] = turn_computer
                    moved = True
                    done = check_done()
                    if done == False:
            			return turn == turn_player
                    else:
                        return
            elif map[0][i] == map[2][i] == turn_computer != " ":
				if map[1][i] ==" ":
					map[1][i] = turn_computer
					moved = True
					done = check_done()
					if done == False:
						return turn == turn_player
					else:
						return
            elif map[1][i] == map[2][i] == turn_computer != " ":
                if map[0][i] == " ":
                    map[0][i] = turn_computer
                    moved = True
                    done = check_done()
                    if done == False:
            			return turn == turn_player
                    else:
                        return
            elif map[i][1] == map[i][2] == turn_computer != " ":
                if map[i][0] ==" ":
                    map[i][0] = turn_computer
                    moved = True
                    done = check_done()
                    if done == False:
            			return turn == turn_player
                    else:
                        return
        if map[0][0] == map[1][1] == turn_computer != " ":
            if map[2][2] == " ":
                map[2][2] = turn_computer
                moved = True
                done = check_done()
                if done == False:
            		return turn == turn_player
                else:
                    return
        elif map[0][0] == map[2][2] == turn_computer != " ":
            if map[1][1] == " ":
                map[1][1] = turn_computer
                moved = True
                done = check_done()
                if done == False:
            		return turn == turn_player
                else:
                    return
        elif map[1][1] == map[2][2] == turn_computer != " ":
            if map[0][0] == " ":
                map[0][0] = turn_computer
                moved = True
                done = check_done()
                if done == False:
            		return turn == turn_player
                else:
                    return
        elif map[0][2] == map[1][1] == turn_computer != " ":
            if map[2][0] == " ":
                map[2][0] = turn_computer
                moved = True
                done = check_done()
                if done == False:
            		return turn == turn_player
                else:
                    return
        elif map[0][2] == map[2][0] == turn_computer != " ":
            if map[1][1] == " ":
                map[1][1] = turn_computer
                moved = True
                done = check_done()
                if done == False:
            		return turn == turn_player
                else:
                    return
        elif map[1][1] == map[2][0] == turn_computer != " ":
            if map[0][2] == " ":
                map[0][2] = turn_computer
                moved = True
                done = check_done()
                if done == False:
            		return turn == turn_player
                else:
                    return

        for i in range(0,3):
            if map[i][0] == map[i][1] == turn_player != " ":
                if map[i][2] ==" ":
                    map[i][2] = turn_computer
                    moved = True
                    done = check_done()
                    if done == False:
            			return turn == turn_player
                    else:
                        return
            elif map[0][i] == map[1][i] == turn_player != " ":
				if map[2][i] ==" ":
					map[2][i] = turn_computer
					moved = True
					done = check_done()
					if done == False:
						return turn == turn_player
					else:
						return
            elif map[i][0] == map[i][2] == turn_player != " ":
                if map[i][1] ==" ":
                    map[i][1] = turn_computer
                    moved = True
                    done = check_done()
                    if done == False:
            			return turn == turn_player
                    else:
                        return
            elif map[0][i] == map[2][i] == turn_player != " ":
				if map[1][i] ==" ":
					map[1][i] = turn_computer
					moved = True
					done = check_done()
					if done == False:
						return turn == turn_player
					else:
						return
            elif map[1][i] == map[2][i] == turn_player != " ":
                if map[0][i] == " ":
                    map[0][i] = turn_computer
                    moved = True
                    done = check_done()
                    if done == False:
            			return turn == turn_player
                    else:
                        return
            elif map[i][1] == map[i][2] == turn_player != " ":
                if map[i][0] == " ":
                    map[i][0] = turn_computer
                    moved = True
                    done = check_done()
                    if done == False:
            			return turn == turn_player
                    else:
                        return
        if map[0][0] == map[1][1] == turn_player != " ":
            if map[2][2] == " ":
                map[2][2] = turn_computer
                moved = True
                done = check_done()
                if done == False:
            		return turn == turn_player
                else:
                    return
        elif map[0][0] == map[2][2] == turn_player != " ":
            if map[1][1] == " ":
                map[1][1] = turn_computer
                moved = True
                done = check_done()
                if done == False:
            		return turn == turn_player
                else:
                    return
        elif map[1][1] == map[2][2] == turn_player != " ":
            if map[0][0] == " ":
                map[0][0] = turn_computer
                moved = True
                done = check_done()
                if done == False:
            		return turn == turn_player
            	else:
                    return

        elif map[0][2] == map[1][1] == turn_player != " ":
            if map[2][0] == " ":
                map[2][0] = turn_computer
                moved = True
                done = check_done()
                if done == False:
            		return turn == turn_player
            	else:
            		return
   
        elif map[0][2] == map[2][0] == turn_player != " ":
            if map[1][1] == " ":
                map[1][1] = turn_computer
                moved = True
                done = check_done()
                if done == False:
            		return turn == turn_player
            	else:
            		return
   
        elif map[1][1] == map[2][0] == turn_player != " ":
            if map[0][2] == " ":
                map[0][2] = turn_computer
                moved = True
                done = check_done()
                if done == False:
            		return turn == turn_player
            	else:
            		return

        if map[0][2] ==" ":
            map[0][2] = turn_computer
            moved = True
            done = check_done()
            if done == False:
            	return turn == turn_player
            else:
            	return
        elif map[2][2] ==" ":
            map[2][2] = turn_computer
            moved = True
            done = check_done()
            if done == False:
            	return turn == turn_player
            else:
            	return
        elif map[0][0] ==" ":
            map[0][0] = turn_computer
            moved = True
            done = check_done()
            if done == False:
            	return turn == turn_player
            else:
            	return
        elif map[2][0] ==" ":
            map[2][0] = turn_computer
            moved = True
            done = check_done()
            if done == False:
            	return turn == turn_player
            else:
            	return
        elif map[1][1] ==" ":
            map[1][1] = turn_computer
            moved = True
            done = check_done()
            if done == False:
            	return turn == turn_player
            else:
            	return
        elif map[0][1] ==" ":
            map[0][1] = turn_computer
            moved = True
            done = check_done()
            if done == False:
            	return turn == turn_player
            else:
            	return	
        elif map[2][1] ==" ":
            map[2][1] = turn_computer
            moved = True
            done = check_done()
            if done == False:
            	return turn == turn_player
            else:
            	return
        elif map[1][0] ==" ":
            map[1][0] = turn_computer
            moved = True
            done = check_done()
            if done == False:
            	return turn == turn_player
            else:
            	return
        elif map[1][2] ==" ":
            map[1][2] = turn_computer
            moved = True
            done = check_done()
            if done == False:
            	return turn == turn_player
            else:
            	return

turn_player = raw_input("Select a player X or O: ")
map = [[" "," "," "],
       [" "," "," "],
       [" "," "," "]]
done = False

if turn_player == "O":
    turn_computer = "X"
else:
    turn_computer = "O"

turn = check_first()

while done != True:
    
    if turn == turn_player:

        print turn, "'s turn"
        print
        moved = False
        while moved != True:
        	print "Please select position by typing in a number between 1 and 9, see below for which number that is which position..."
        	print "7|8|9"
        	print "4|5|6"
        	print "1|2|3"
        	print

        	try:
        		pos = input("Select: ")
        		if pos <=9 and pos >=1:
        			Y = pos/3
        			X = pos%3
        			if X != 0:
        				X -=1
        			else:
        				X = 2
        				Y -=1
                    
                	if map[Y][X] == " ":
                		map[Y][X] = turn
                    	moved = True
                    	done = check_done()

                    	if done == False:
                        	turn = turn_computer
                
            
        	except:
        		print "You need to add a numeric value"

    if turn == turn_computer:
    
    	print turn, "'s turn"
        print
        moved = False
        done = check_done()
    	computer_play()
        done = check_done()
        print_board()
    	if done == False:
			turn = turn_player