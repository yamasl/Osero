import board

#main関数
def main():
    boards=board.Board()
    while boards.c != 60:
        print(*boards.boards,sep='\n')
        val=input()
        if val=='finish':
            return 0
        xy=[int(k) for k in val.split(',')]
        if boards.CheckBoards(xy[0],xy[1]):
            boards.TurnStones(xy[0],xy[1])
        else:
            print('Please retype:')
    boards.Resurt

if __name__=="__main__":
    main()