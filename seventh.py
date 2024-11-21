from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        self.__position = new_position

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position
        direction = 1 if self.color == 'white' else -1
        moves = [(row + direction, col)]  # Pohyb vpřed

        # Pěšák může mít možnost pohybu o dva políčka, pokud je na startovní pozici
        if (self.color == 'white' and row == 2) or (self.color == 'black' and row == 7):
            moves.append((row + 2 * direction, col))

        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = [move for move in moves if self.is_position_on_board(move)]
        return final_moves
    
    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = [move for move in moves if self.is_position_on_board(move)]
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        # Diagonální pohyby
        for d in range(1, 8):
            moves.append((row + d, col + d))  # doprava dolů
            moves.append((row + d, col - d))  # doleva dolů
            moves.append((row - d, col + d))  # doprava nahoru
            moves.append((row - d, col - d))  # doleva nahoru

        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = [move for move in moves if self.is_position_on_board(move)]
        return final_moves
    
    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        # Horizontální a vertikální pohyby
        for d in range(1, 8):
            moves.append((row + d, col))  # dolů
            moves.append((row - d, col))  # nahoru
            moves.append((row, col + d))  # doprava
            moves.append((row, col - d))  # doleva

        #Filtruje tahy, které jsou mimo šachovnici
        final_moves = [move for move in moves if self.is_position_on_board(move)]
        return final_moves
    
    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        
        # Diagonální pohyby (jako dáma)
        for d in range(1, 8):
            moves.append((row + d, col + d))  # doprava dolů
            moves.append((row + d, col - d))  # doleva dolů
            moves.append((row - d, col + d))  # doprava nahoru
            moves.append((row - d, col - d))  # doleva nahoru

        # Horizontální a vertikální pohyby (jako věž)
        for d in range(1, 8):
            moves.append((row + d, col))  # dolů
            moves.append((row - d, col))  # nahoru
            moves.append((row, col + d))  # doprava
            moves.append((row, col - d))  # doleva

        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = [move for move in moves if self.is_position_on_board(move)]
        return final_moves
    
    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 1, col), (row - 1, col),  # nahoru a dolů
            (row, col + 1), (row, col - 1),  # doprava a doleva
            (row + 1, col + 1), (row + 1, col - 1),  # diagonální pohyby
            (row - 1, col + 1), (row - 1, col - 1)
        ]
        
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = [move for move in moves if self.is_position_on_board(move)]
        return final_moves
    
    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    # Testování figur
    pieces = [
        Knight("black", (1, 2)),
        Pawn("white", (2, 2)),
        Bishop("black", (3, 3)),    
        Rook("white", (1, 1)),
        Queen("black", (4, 4)),
        King("white", (5, 5))
    ]
    
    for piece in pieces:
        print(piece)
        print(f'Possible moves: {piece.possible_moves()}')