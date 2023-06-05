We are goin to make a Chess game that two players could potentially play
Things the Game should have
1. A board
1.1 A picture of a board that I can calculate the pixels and then divide into 64 squares +
1.2 +

0,0 W; 0,1 B; 0,2 W; 0,3 B;
1,0 B; 1,1 W; 1,2 B; 1,3 W; 
2,0 W; 2,1 B; 2,2 W; 2,3 B;
3,0 B; 3,1 W; 3,2 B; 3,3 W; 
4,0 W; 4,1 B; 4,2 W; 4,3 B;
5,0 B; 5,1 W; 5,2 B; 5,3 W; 
6,0 W; 6,1 B; 6,2 W; 6,3 B;
7,0 B; 7,1 W; 7,2 B; 7,3 W; 


2. Pieces
Each piece should have a set of moves that they can do 
and only those moves can be played. When piece is pressed
it will show the possible squares that piece can reach
2.1 Pons
2.2 Knights
2.3 Bishops
2.4 Queen
2.5 King

4. Game Starts
    1. State start = 0 // white is even // black is odd
    2. Logic to tell if odd or even to determine who's turn it is. 
    3. Each player should have 2 clicks that will be calculated
        1. White(For Example) First Click: 
            1. See what is on the square that was presssed first (Black or White Owner)
            2. If Black: 
                1. tell it to pick a white piecel don't add square pressed to list
            3. If None: 
                1. tell it to picka  white piece; don't add square pressed to list
            4. If White: 
                1. Call the moves function with the corresponding piece that was pressed and see what squares are legal
                2. Color all of those squares in the list an opaque green
        2. White: Second Click:
            1. See if the square that was clicked second is in our list of legal moves that we created with First Click
            2. If not:
                1. Don't select that move to be put into our list. 
                2. Do not register that that move has been played. 
                3. Allow player to retry the second move
            3. If so:
                1. add that second square to the list of moves made 
                2. remove what was on the square for First Click and add the piece that was on the square square from First Click to square for Second Click
                3. start = start + 1
        3. After the first sequence, black will have a turn // First Click:
            1. See what is on the square that was presssed first (Black or White Owner)
            2. If White: 
                1. tell it to pick a white piecel don't add square pressed to list
            3. If None: 
                1. tell it to picka  white piece; don't add square pressed to list
            4. If Black: 
                1. Call the moves function with the corresponding piece that was pressed and see what squares are legal
                2. Color all of those squares in the list an opaque green
        4. See if the square that was clicked second is in our list of legal moves that we created with First Click
            1. add that second square to the list of moves made 
            2. If not:
                1. Don't select that move to be put into our list. 
                2. Do not register that that move has been played. 
                3. Allow player to retry the second move
            3. If so:
                1. add that second square to the list of moves made 
                2. remove what was on the square for First Click and add the piece that was on the square square from First Click to square for Second Click
                3. start = start + 1



