class Board:
    """
    A class to represent a tic-tac-toe board. It holds the spots.
    """

    def __init__(self):
        self.spots = [["" for i in range(3)] for j in range(3)]


    def is_over(self):
        """
        Checks if the game is over and outputs who has won.
        :return: X if X won, O if O won, T if it is a tie, and None if the game is still going on
        """

        is_tie = True
        for i in range(3):
            for j in range(3):
                if self.spots[i][j] == "":
                    is_tie = False

        if is_tie:
            return "T"




        # We need to go through both players and check for a winner for either
        for mark in ["O", "X"]:

            # Now we need to check for three in a rows

            # We only need to check a limited number of things for a three in a row. Namely, we will define the start
            # indices as the spots on the left and top border (any index with a 0 in it). Then we will check for three
            # in a row from those starting points
            for start_index in [[i, j] for i in range(3) for j in range(3) if (i == 0 or j == 0)]:

                # From every start index we want to check to the right, to the bottom right, and down
                # Note that we only need to check to the right if the last index is 0, we only need to check down
                # if the first index is 0, and we only need to check diagonal if it is only 3 and or 0 in the indices

                # Checking to the right
                if start_index[1] == 0:

                    for i in range(3):
                        if self.spots[i][start_index[1]] != mark:
                            break

                    else:
                        return mark

                if start_index[0] == 0:

                    for i in range(3):
                        if self.spots[start_index[0]][i] != mark:
                            break

                    else:
                        return mark

                if 1 not in start_index and 2 not in start_index:

                    if start_index == [0, 0]:

                        for i in range(3):
                            if self.spots[start_index[0] + i][start_index[1] + i] != mark:
                                break

                        else:
                            return mark

                    elif start_index == [0, 2]:

                        for i in range(3):
                            if self.spots[start_index[0] + i][start_index[1] - i] != mark:
                                break

                        else:
                            return mark


        # If we got through all that it's a tie
        return None


    def place_mark(self, mark, i, j):
        """
        Place a mark on the board at self.spots[i][j]
        :param mark: Either X or O
        :param i: the row we want
        :param j: the column we want
        """
        self.spots[i][j] = mark





