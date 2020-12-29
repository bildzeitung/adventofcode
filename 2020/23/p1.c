/**
  Day 23
 */
#include <stdio.h>

typedef struct _clist {
  int cup;
  struct _clist* next;
  struct _clist* prev;
} clist;

const int CUPNUM = 9;

void print_cups(clist* current, clist* cups) {
  clist* i = cups[0].next;
  if (&cups[0] == current) {
    printf("(%i)", cups[0].cup);
  } else {
    printf("%i", cups[0].cup);
  }
  while (i != &cups[0]) {
    if (i == current) {
      printf(" (%i)", i->cup);
    } else {
      printf(" %i", i->cup);
    }
    i = i->next;
  }
  printf("\n");
}


clist* tick(clist* current, clist* cups) {
    // grab the sub-list
  clist* select_start = current->next ;
  clist* select_end = current->next->next->next;

  // remove it
  current->next = select_end->next;
  select_end->next->prev = current;

  int dest = current->cup - 1;
  if (dest == 0) dest = CUPNUM;
  while ((dest == select_start->cup) ||
     (dest == select_start->next->cup) ||
     (dest == select_end->cup)) {
       dest -= 1;
       if (dest == 0) dest = CUPNUM; // sigh; data
     }
  printf("destination: %i\n", dest);
  clist *i = current->next;
  while (i->cup != dest) {
    i = i->next;
  }
  select_end->next  = i->next;
  i->next->prev = select_end;
  i->next = select_start;
  select_start->prev = i;

  return current->next;
}


void print_final(clist* current, clist* cups) {
  while (current->cup != 1) {
    current = current->next;
  }
  printf("--> ");
  current = current->next;
  while (current->cup != 1) {
    printf("%i", current->cup);
    current = current->next;
  }
  printf("\n");
}

int main() {
  //int initial_cups[] = {3,8,9,1,2,5,4,6,7};  // test data
  int initial_cups[] = {6,1,4,7,5,2,8,3,9};  // my input
  clist cups[CUPNUM];

  /** Given set of initial cup values, initialise the linked list
   */
  for (int i=0; i < CUPNUM-1; i++) {
    cups[i].cup = initial_cups[i];
    cups[i].next = &cups[i+1];
    cups[i+1].prev = &cups[i];
  }
  // fix up the last one
  cups[CUPNUM-1].cup = initial_cups[CUPNUM-1];
  cups[CUPNUM-1].next = &cups[0];
  // fix up the first one
  cups[0].prev= &cups[CUPNUM-1];

  // okey doke; now move'em
  clist* current = &cups[0];

  for (int moves = 1; moves < 101; moves++) {
    printf("-- move %i --\n", moves);
    print_cups(current, cups);
    current = tick(current, cups);
    printf("\n");
  }
  printf("-- final --\n");
  print_cups(current, cups);

  print_final(current, cups);

  return 0;
}