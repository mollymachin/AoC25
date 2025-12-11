#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int check_access(const vector<string>& board, int r, int c);

int main() {
    ifstream file("day4.txt");
    vector<string> board;
    string line;

    while (getline(file, line)) {
        board.push_back(line);
    }
    file.close();

    int rolls = 0;
    int board_rows = board.size();

    for (int r = 0; r < board_rows; r++) {
        int board_cols = board[r].size();
        for (int c = 0; c < board_cols; c++) {
            rolls += check_access(board, r, c);
       }
    }
    cout << "Number of rolls accessible is " << rolls << endl;
    return 0;
}


int check_access(const vector<string>& board, int r, int c) {
    if (board[r][c] != '@') {
        return 0; }

    int rows = board.size();
    int cols = board[0].size();
    int count = 0;

    for (int row = -1; row <= 1; row++) {
        for (int col = -1; col <= 1; col++) {
            if (row == 0 && col == 0) continue;

            int adj_row = r + row;
            int adj_col = c + col;

            if (adj_row >= 0 && adj_row < rows && adj_col >= 0 && adj_col < cols) {
                if (board[adj_row][adj_col] == '@') {
                    count++;
                }
            }
        }
    }
    return (count < 4) ? 1 : 0;
}
