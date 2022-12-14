#include <stdio.h>
#include <stdlib.h>

int main()
{
    char s[]="004010020035056083116155198244292341390439488537586635684733";
    int n; scanf("%d", &n);
    n *= 3; s[n] = '\0';
    printf("%d", atoi(s + n - 3));
}