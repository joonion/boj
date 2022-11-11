#include <stdio.h>

int counter;

int is_lucky(int n) {
    if (counter > n)
        return 1;
    if (n % counter == 0)
        return 0;

    int next_position = n - (n / counter);

    counter++;
    return is_lucky(next_position);
}

int main()
{
    int n, m;
    scanf("%d", &n);
    while (n--) {
        scanf("%d", &m);
        counter = 2;
        if (is_lucky(m))
            printf("lucky\n");
        else
            printf("unlucky\n");
    }
}