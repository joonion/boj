#include <stdio.h>
#define MAX 10000

int heap[MAX];
int size = 0;

void heap_push(int heap[], int j) {
    int i = ++size;
    while (i != 1 && j > heap[i/2]) {
        heap[i] = heap[i/2];
        i /= 2;
    }
    heap[i] = j;
}

int heap_pop(int heap[]) {
    int top = heap[1];
    int item = heap[size--];
    int parent = 1, child = 2;
    while (child <= size) {
        if (child < size && heap[child] < heap[child+1])
            child++;
        if (item >= heap[child])
            break;
        heap[parent] = heap[child];
        parent = child;
        child *= 2;
    }
    heap[parent] = item;
    return top;
}

int solve(int n) {
    int cnt = 0;
    while (1) {
        cnt++;
        int m = heap[1] / 2;
        if (m == 0) break;
        // printf("%d\n", m);
        heap_pop(heap);
        heap_push(heap, m);
    }
    return cnt;
}

int main()
{
    int n; scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int j; scanf("%d", &j);
        if (size <= (n - 1) / 2)
            heap_push(heap, j);
        else if (j < heap[1]) {
            heap_pop(heap);
            heap_push(heap, j);
        }
    }
    // while (size > 0) {
    //     int top = heap_pop(heap);
    //     printf("%d ", top);
    // }
    printf("%d\n", solve(n));
}