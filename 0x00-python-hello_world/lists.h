#ifndef _LISTS_H_
#define _LISTS_H_

#include <stdlib.h>

/**
 * struct lstint_s - singly linked list
 * @a: integer
 * @nxt: points to the nxt node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct lstint_s
{
	int a;
	struct lstint_s *nxt;
} lstint_t;

size_t print_listint(const lstint_t *hh);
lstint_t *add_nodeint(lstint_t **head, const int a);
void free_listint(lstint_t *head);
int check_cycle(lstint_t *list);

#endif /* LISTS_H */
