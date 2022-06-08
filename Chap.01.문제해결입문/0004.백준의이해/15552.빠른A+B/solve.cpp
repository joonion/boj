#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    int T, A, B;
    cin >> T;
    while (T-- > 0) {
        cin >> A >> B;
        cout << A + B << "\n";
    }
}