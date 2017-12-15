#include <stdio.h>

#define MAXPAIRS 5000000

long generator(long prev, int factor, int multiple_of) {
    int modulus = 2147483647;
    do {
        prev = (prev * factor) % modulus;
    } while (prev % multiple_of);

    return prev;
}


int main(void) {
    int ga_factor = 16807;
    int gb_factor = 48271;

    long prev_a, prev_b;
    scanf("%ld %ld", &prev_a, &prev_b);

    printf("Starting with %ld %ld\n", prev_a, prev_b);

    int count = 0;
    int match = 0;
    for (int i = 0; i < MAXPAIRS; i++) {
        prev_a = generator(prev_a, ga_factor, 4);
        prev_b = generator(prev_b, gb_factor, 8);

        // printf("%ld %ld\n", prev_a, prev_b);

        if ((prev_a & (long)0xffff) == (prev_b & (long)0xffff)) match++;
    }
    printf("MATCHES: %d\n", match);
}
