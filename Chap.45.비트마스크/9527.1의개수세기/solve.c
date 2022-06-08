#include <stdio.h>

int main() {
    int n, m, i, s = 0;
    scanf("%d %d", &n, &m);
    for (int i = n; i <= m; i++) {
        int j = i;
        while (j > 0) {
            s += j & 1;
            j >>= 1;
        }
    }
    printf("%d", s);
}