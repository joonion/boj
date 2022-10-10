#include <stdio.h>
#define MAX 20000

int search(int m, int B[], int k) {
    int low = 0, high = m - 1;
    while (low < high) {
        int mid = (low + high) / 2;
        if (k <= B[mid])
            low = mid + 1;
        else
            high = mid - 1;
    }
    return low;
}

int solve(int n, int m, int A[], int B[]) {
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        int j = search(m, B, A[i]);
        cnt += j;
        printf("%d %d %d\n", i, j, cnt);
    }
    return cnt;
}

void sort(int m, int B[]) {
    
}

int main()
{
    int T, n, m, A[MAX], B[MAX];
    scanf("%d", &T);
    while (T-- > 0) {
        // printf("%d\n", T);
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; i++)
            scanf("%d", &A[i]);
        for (int i = 0; i < m; i++)
            scanf("%d", &B[i]);
        sort(m, B);
        printf("%d\n", solve(n, m, A, B));
    }
}