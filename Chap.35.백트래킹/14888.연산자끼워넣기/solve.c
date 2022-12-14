#include <stdio.h>

int n, a[11], b[4], op[10];
int max = 0x80000000, min = 0x7FFFFFFF;

int calculate() {
    int v = a[0];
    for (int i = 0; i < n - 1; i++) {
        switch(op[i]) {
            case 0: v += a[i+1]; break;
            case 1: v -= a[i+1]; break;
            case 2: v *= a[i+1]; break;
            case 3: v /= a[i+1]; break;
        }
    }
    return v;
}

void swap(int i, int j) {
    int t = op[i]; op[i] = op[j]; op[j] = t;
}

void perm(int i) {
    if (i == n - 1) {
        int v = calculate();
        max = (v > max) ? v : max;
        min = (v < min) ? v : min;
    }
    else {
        for (int j = i; j < n - 1; j++) {
            swap(i, j);
            perm(i + 1);
            swap(i, j);
        }
    }
}

void solve() {
    int k = 0;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < b[i]; j++)
            op[k++] = i;
    perm(0);
}

int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d", &a[i]);
    for (int i = 0; i < 4; i++)
        scanf("%d", &b[i]);
    solve();
    printf("%d\n", max);
    printf("%d\n", min);
}