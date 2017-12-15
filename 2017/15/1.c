#include <stdio.h>

#define MAXPAIRS 40000000

int main(void) {
    int ga_factor = 16807;
    int gb_factor = 48271;
    int modulus = 2147483647;

    long prev_a, prev_b;
    scanf("%ld %ld", &prev_a, &prev_b);

    printf("Starting with %ld %ld\n", prev_a, prev_b);

    int count = 0;
    int match = 0;
    for (int i = 0; i < MAXPAIRS; i++) {
        prev_a = (prev_a * ga_factor) % modulus;
        prev_b = (prev_b * gb_factor) % modulus;
        if ((prev_a & 0xffff) == (prev_b & 0xffff)) match++;
    }
    printf("MATCHES: %d\n", match);
}
