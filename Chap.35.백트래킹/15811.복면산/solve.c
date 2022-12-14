#include <stdio.h>
#include <stdlib.h>

char w[3][19];
int cnt, a[26], b[10], c[10];

int f(char *w) {
	int x = 0;
	for (int i = 0; w[i]; i++)
		x = x * 10 + c[a[w[i] - 65]-1];
	return x;
}

int dfs(int i) {
	if (i == cnt) {
		if (f(w[0]) + f(w[1]) == f(w[2])) {
			puts("YES");
			exit(0);
		}
	}
	for (int j = 0; j < 10; j++) {
		if (b[j]) continue;
		c[i] = j;
		b[j] = i;
		dfs(i + 1);
		b[j] = 0;
	}
}

int main() 
{
	for (int i = 0; i < 3; i++)
    	scanf("%s", w[i]);
	for (int i = 0; i < 3; i++)
		for (int j = 0; w[i][j]; j++)
			if (!a[w[i][j] - 'A'])
				a[w[i][j] - 'A'] = ++cnt;
    if (cnt <= 10) dfs(0);
	puts("NO");
}