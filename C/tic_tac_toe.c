#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#define SIZE 3
#define EMPTY ' '
#define PLAYER_X 'X'
#define PLAYER_O 'O'

char players[] = { PLAYER_X, PLAYER_O };
char tic_tac_toe[SIZE][SIZE] = {
    {'1', '2', '3'},
    {'4', '5', '6'},
    {'7', '8', '9'}
};

void print_char(char c) {
    printf("%c", c);
}

void print_whitespace(int count) {
    for (int i = 0; i < count; i++) {
        print_char(' ');
    }
}

void print_row(int row) {
    for (int col = 0; col < SIZE; col++) {
        print_whitespace(2);
        printf("%c", tic_tac_toe[row][col]);
        print_whitespace(2);
        if (col < SIZE - 1) {
            print_char('|');
        }
    }
    print_char('\n');
}

void print_underline() {
    for (int i = 0; i < SIZE; i++) {
        print_whitespace(5);
        if (i < SIZE - 1) {
            print_char('|');
        }
    }
    print_char('\n');
}

void print_board() {
    for (int row = 0; row < SIZE; row++) {
        print_row(row);
        if (row < SIZE - 1) {
            print_underline();
        }
    }
}

bool update_board(int position, char player) {
    int row = (position - 1) / SIZE;
    int col = (position - 1) % SIZE;
    if (tic_tac_toe[row][col] == 'X' || tic_tac_toe[row][col] == 'O') {
        return false;  // Position already filled
    }
    tic_tac_toe[row][col] = player;
    return true;
}

bool check_winner(char line[SIZE]) {
    return (line[0] == line[1] && line[1] == line[2]);
}

char check_all_cases() {
    char line[SIZE];

    // Check rows and columns
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            line[j] = tic_tac_toe[i][j];
        }
        if (check_winner(line)) {
            return line[0]; // Return winner
        }
        
        for (int j = 0; j < SIZE; j++) {
            line[j] = tic_tac_toe[j][i];
        }
        if (check_winner(line)) {
            return line[0]; // Return winner
        }
    }

    // Check diagonals
    for (int i = 0; i < SIZE; i++) {
        line[i] = tic_tac_toe[i][i];
    }
    if (check_winner(line)) {
        return line[0]; // Return winner
    }

    for (int i = 0; i < SIZE; i++) {
        line[i] = tic_tac_toe[i][SIZE - 1 - i];
    }
    if (check_winner(line)) {
        return line[0]; // Return winner
    }

    return '0'; // No winner
}

void clear_screen() {
    system("cls||clear");
}

void play_game() {
    clear_screen();
    print_board();

    int round = 0;
    int input;
    char current_player = players[rand() % 2];

    while (true) {
        if (round == 9) {
            printf("Match has been drawn.\n");
            break;
        }

        printf("Player %c, enter a number (1-9): ", current_player);
        scanf("%d", &input);

        if (input < 1 || input > 9) {
            printf("Invalid input. Please enter a number between 1 and 9.\n");
            continue;
        }

        clear_screen();
        if (update_board(input, current_player)) {
            round++;
            char winner = check_all_cases();
            if (winner != '0') {
                print_board();
                printf("Player %c is the winner!\n", winner);
                break;
            }
            current_player = (current_player == PLAYER_X) ? PLAYER_O : PLAYER_X; // Switch player
        } else {
            printf("Position already filled. Try again.\n");
        }

        print_board();
    }
}

int main() {
    srand(time(NULL)); // Seed the random number generator
    play_game();
    return 0;
}
