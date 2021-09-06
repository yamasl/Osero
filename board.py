class Board():
    EMPTY=0
    BLACK=-1
    WHITE=1
    WALL=2

    WIDTH=8
    HEIGHT=8
    #初期化
    def __init__(self):
        #先手の色を黒で初期化
        self.CurrentColor=self.BLACK
        #盤面の生成
        self.boards=[[0]*(self.WIDTH+2) for i in range(self.HEIGHT+2)]
        #壁の生成
        for i in range(self.WIDTH+2):
            self.boards[i][0]=self.WALL
            self.boards[i][-1]=self.WALL
        for i in range(self.HEIGHT+2):
            self.boards[0][i]=self.WALL
            self.boards[-1][i]=self.WALL
        #盤面の初期化
        self.boards[4][4]=self.WHITE
        self.boards[5][5]=self.WHITE
        self.boards[4][5]=self.BLACK
        self.boards[5][4]=self.BLACK

        #カウンタ
        self.c=0

        #テスト
        #self.boards[4][3]=self.WHITE

    #石が置けるかチェック
    def CheckBoards(self,x,y):
        stone=self.CurrentColor
        #石が置かれていないか,範囲外ではないか確認
        if self.boards[x][y]!=0:
            return False
        #隣接する相手の石があるか確認
        for i in range(-1,2):
            for j in range(-1,2):
                if  self.boards[x+i][y+j]==-stone:
                    kx=x+i
                    ky=y+j
                    #相手の石があれば挟めるかどうか確認
                    while self.boards[kx][ky]!=0 and self.boards[kx][ky]!=2:
                        if self.boards[kx+i][ky+j]==stone:
                            return True
                        else:
                            kx+=i
                            ky+=j
                else:
                    pass
        return False
                    
    #石をひっくり返す
    def TurnStones(self,x,y):
        stone=self.CurrentColor
        self.boards[x][y]=stone
        self.c+=1
        for i in range(-1,2):
            for j in range(-1,2):
                if  self.boards[x+i][y+j]==-stone:
                    kx=x+i
                    ky=y+j
                    #相手の石をひっくり返す
                    while self.boards[kx][ky]!=0 and self.boards[kx][ky]!=2:
                        if self.boards[kx+i][ky+j]==stone:
                            while kx!=x or ky!=y:
                                   self.boards[kx][ky]=stone
                                   kx-=i
                                   ky-=j
                            break
                        else:
                            kx+=i
                            ky+=j
                else:
                    pass
        self.CurrentColor*=-1

    def Resurt(self):
        if sum(map(sum,self.boards)) < 72:
            print('BLACK WINS')
        elif sum(map(sum,self.boards)) > 72:
            print('WHITE WINS')
        else:
            print('DRAW')