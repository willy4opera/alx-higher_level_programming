#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a lstint_t list
 * @hh: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const lstint_t *hh)
{
	const lstint_t *current_l;
	unsigned int a;

	current_l = hh;
	a = 0;
	while (current_l != NULL)
	{
		printf("%i\n", current_l->a);
		current_l = current_l->nxt;
		a++;
	}
	return (a);
}

/**
 * add_nodeint - adds a new node at the beginning of a lstint_t list
 * @head: pointer to a pointer of the start of the list
 * @a: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
lstint_t *add_nodeint(lstint_t **head, const int a)
{
	lstint_t *new_l;

	new_l = malloc(sizeof(lstint_t));
	if (new_l == NULL)
	{
		return (NULL);
	}
	new_l->a = a;
	new_l->nxt = *head;
	*head = new_l;
	return (new_l);
}

/**
 * free_listint - frees a lstint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(lstint_t *head)
{
	lstint_t *current_l;

	while (head != NULL)
	{
		current_l = head;
		head = head->nxt;
		free(current_l);
	}
}
