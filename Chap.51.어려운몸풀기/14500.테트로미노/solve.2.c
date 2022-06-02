#include <stdio.h>
int a[2][3] = {
    {
    {1, 2, 3}, 
    {4, 5, 6}
    }
};

int main() {
    int i, j, k;
    for (i = 0; i < 1; i++)
        for (j = 0; j < 2; j++)
           for (k = 0; k < 3; k++)
                printf("%d", a[i][j][k]);
}