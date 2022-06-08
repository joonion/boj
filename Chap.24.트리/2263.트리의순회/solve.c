#include <stdio.h>

#define MAX 100000

int inorder[MAX], postorder[MAX];

void solve(int inlow, int inhigh, int polow, int pohigh) {
    // printf("%d %d %d %d\n", inlow, inhigh, polow, pohigh);
    if (inlow > inhigh)
        return;
    else if (inlow == inhigh)
        printf("%d ", inorder[inlow]);
    else {
        int i, size, root = postorder[pohigh];
        for (i = inlow; i <= inhigh; i++)
            if (root == inorder[i]) break;
        size = i - inlow;
        printf("%d ", root);
        solve(inlow, i - 1, polow, polow + size - 1);
        solve(i + 1, inhigh, polow + size, pohigh - 1);
    }
}

int main() {
    int n, i;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
        scanf("%d", &inorder[i]);
    for (i = 0; i < n; i++)
        scanf("%d", &postorder[i]);
    solve(0, n - 1, 0, n - 1);
}