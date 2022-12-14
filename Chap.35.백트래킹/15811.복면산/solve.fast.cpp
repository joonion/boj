#include <bits/stdc++.h>
using namespace std;

string s1, s2, s3;
int n;

void backtrack(int i) {

}

int main() {
    cin >> s1 >> s2 >> s3;
    reverse(s1.begin(), s1.end());
    reverse(s2.begin(), s2.end());
    reverse(s3.begin(), s3.end());
    backtrack(0);
}