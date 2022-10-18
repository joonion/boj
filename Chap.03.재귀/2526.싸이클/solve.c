#include <stdio.h>

int n, p;
int list[1001];

int solve() {
    int cnt = n * n % p;
    int res_cnt = 1;
    while (list[cnt] == 0) {
        list[cnt] = res_cnt++;
        cnt = cnt * n % p;
    }
    return res_cnt - list[cnt];
}


int main()
{
    scanf("%d %d", &n, &p);
    printf("%d", solve());
}