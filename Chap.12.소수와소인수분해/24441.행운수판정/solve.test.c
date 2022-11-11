#include <stdio.h>

int counter = 2;

int is_lucky(int n) {
    if (counter > n)
        return 1;
    if (n % counter == 0)
        return 0;
    n = n - (n / counter);
    counter++;
    return is_lucky(n);
}

int main()
{
    int m;
    scanf("%d", &m);
    if (is_lucky(m))
        printf("lucky\n");
    else
        printf("unlucky\n");
}