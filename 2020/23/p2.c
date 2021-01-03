/**
  Day 23
 */
#include <stdio.h>
#include <stdlib.h>

// Circular single link list
typedef struct _clist {
  int cup;
  struct _clist* next;
} clist;
typedef clist* plist;

const int CUPNUM = 1000000;
const int MOVES = 10000000;


clist* tick(clist* current, clist* cups) {
    // grab the sub-list
  clist* select_start = current->next ;
  clist* select_end = current->next->next->next;

  // remove it
  current->next = select_end->next;

  /* This is the main problem -- how to grab the destination cup.

     In a typical linked-list, the nodes are not necessarily allocated in
     a contiguous block of memory. In this case, we know how many nodes we
     need, so we make them all up front. This means we know where each numbered
     cup is -- it's offset from the start of the array. This means we have an
     index into all of the cups and can look one up in the array instead, an
     O(1) operation.

     We're using the array to act as an index or hash table while storing
     forward pointers in the circular list. This maintains the game, but lets
     us avoid having to search for the destination cup.
  */
  int dest = current->cup - 1;
  if (dest == 0) dest = CUPNUM;
  // no loop -- just check each of the 3 in the sublist
  while ((dest == select_start->cup) ||
    (dest == select_start->next->cup) ||
    (dest == select_end->cup))
      if (--dest == 0) dest = CUPNUM; // sigh; data
  clist* destcup = cups + dest;
  select_end->next  = destcup->next;
  destcup->next = select_start;

  return current->next;
}


int main() {
  int initial_cups[] = {3,8,9,1,2,5,4,6,7};  // test data
  //int initial_cups[] = {6,1,4,7,5,2,8,3,9};  // my input
  
  // n.b. this can still be static, ie:
  //   clist cups[CUPNUM+1+1];
  //      if you're willing to, like: ulimit -s <16000032>
  //
  clist *cups = (clist*)malloc(sizeof(clist) * (CUPNUM+1+1));

  // initialise the links for the initial set of cups
  for (int i=0; i < sizeof(initial_cups) / sizeof(int); i++) {
    cups[initial_cups[i]].next = cups + initial_cups[i+1];
    cups[initial_cups[i]].cup = initial_cups[i];
  }
  // link the initial set to the remaining nearly 1 million cups
  cups[initial_cups[sizeof(initial_cups) / sizeof(int)-1]].next = cups + 10;
  // create the links for all remaining cups in sequence
  for (int i=10; i < CUPNUM+1; i++) {
    cups[i].cup = i;
    cups[i].next = cups + i + 1;
  }

  // create the circular part of the list
  cups[CUPNUM].next = cups + initial_cups[0];

  // first current cup is the first in the initial set
  clist* current = cups + initial_cups[0];

  // core game loop
  for (int moves = 1; moves < MOVES+1; moves++)
    current = tick(current, cups);

  printf("-- final --\n");
  long long out = (long long)cups[1].next->cup * (long long)cups[1].next->next->cup;
  printf("Final cups -> %i %i %lld\n", cups[1].next->cup, cups[1].next->next->cup, out);

  return 0;
}
