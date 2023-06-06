#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>


typedef struct listint_s
{
	int node;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);

#endif /* LISTS_H */
