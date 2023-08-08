#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *runing;
    unsigned int nds; /* number of nodes */

    runing = h;
    nds = 0;
    while (runing != NULL)
    {
        printf("%i\n", runing->n);
        runing = runing->next;
        nds++;
    }

    return (nds);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *nw;

    nw = malloc(sizeof(listint_t));
    if (nw == NULL)
        return (NULL);

    nw->n = n;
    nw->next = *head;
    *head = nw;

    return (nw);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *runing;

    while (head != NULL)
    {
        runing = head;
        head = head->next;
        free(runing);
    }
}
