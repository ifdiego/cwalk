#include "parser.h"
#include <iostream>
#include <cctype>

void Parser::Expr() {
    // expression -> term operator
    Term();
    while (true) {
        // operator -> + term { print(+) } operator
        if (lookahead == '+') {
            Match('+');
            Term();
            std::cout << '+';
        }
        // operator -> - term { print(-) } operator
        else if (lookahead == '-') {
            Match('-');
            Term();
            std::cout << '-';
        }
        // empty
        else return;
    }
}

void Parser::Term() {
    if (isdigit(lookahead)) {
        std::cout << lookahead;
        Match(lookahead);
    } else {
        throw SyntaxError{};
    }
}

void Parser::Match(char t) {
    if (t == lookahead) {
        lookahead = std::cin.get();
    } else {
        throw SyntaxError{};
    }
}

Parser::Parser() {
    lookahead = 0;
}

void Parser::Start() {
    lookahead = std::cin.get();
    Expr();
    if (lookahead != '\n') {
        throw SyntaxError{};
    }
}
