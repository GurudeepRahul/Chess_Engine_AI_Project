import chessEngine as chessEngine
import chess as chess

class Main:

    def __init__(self, board=chess.Board):
        self.board=board

    def playHumanMove(self):
        try:
            print(self.board.legal_moves)
            print("""To undo your last move, type "undo".""")

            play = input("Your move: ")
            if (play=="undo"):
                self.board.pop()
                self.board.pop()
                self.playHumanMove()
                return
            self.board.push_san(play)
        except:
            self.playHumanMove()

    def playEngineMove(self, maxDepth, color):
        engine = chessEngine.Engine(self.board, maxDepth, color)
        self.board.push(engine.getBestMove())

    def startGame(self):
        color=None
        while(color!="b" and color!="w"):
            color = input("""Play as (type "b" or "w"): """)
        maxDepth=None
        while(isinstance(maxDepth, int)==False):
            maxDepth = int(input("""Choose depth: """))
        if color=="b":
            while (self.board.is_checkmate()==False):
                print("The engine is thinking...")
                self.playEngineMove(maxDepth, chess.WHITE)
                print(self.board)
                self.playHumanMove()
                print(self.board)
            print(self.board)
            print(self.board.outcome())    
        elif color=="w":
            while (self.board.is_checkmate()==False):
                print(self.board)
                self.playHumanMove()
                print(self.board)
                print("The engine is thinking...")
                self.playEngineMove(maxDepth, chess.BLACK)
            print(self.board)
            print(self.board.outcome())
        self.board.reset
        self.startGame()

newBoard= chess.Board()
game = Main(newBoard)
bruh = game.startGame()
