#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @HD: A pointer the head of the linked list.
 * @num: The number to insert.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **HD, int num)
{
	listint_t *nd = *HD, *nw;

	nw = malloc(sizeof(listint_t));
	if (nw == NULL)
		return (NULL);
	nw->n = num;

	if (nd == NULL || nd->n >= num)
	{
		nw->next = nd;
		*HD = nw;
		return (nw);
	}

	while (nd && nd->next && nd->next->n < num)
		nd = nd->next;

	nw->next = nd->next;
	nd->next = nw;

	return (nw);
}
