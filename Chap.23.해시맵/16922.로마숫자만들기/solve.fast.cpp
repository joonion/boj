#include <bits/stdc++.h>
int main() {
    char s[]="004010020035056083116155198244292341390439488537586635684733";
    int n; std::cin >> n; n *= 3; s[n] = 0;
    std::cout << atoi(s+n-3);
}