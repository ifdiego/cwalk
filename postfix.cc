#include "parser.h"
#include <iostream>

using namespace std;

int main() {
    Parser tradutor;
    try {
        tradutor.Start();
    } catch (SyntaxError) {
        std::cout << "^\n";
        std::cout << "Erro de Sistemas";
    }
    std::cout << std::endl;
}
