#include "lists.h"

/**
 * check_cycle - check for loop in LL
 * @list: head of linked list
 *
 * Description - check for loops in LL
 * Return: 1 if cycled, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *slw, *fst;

	if (!list)
	{
		return (0);
	}
	slw = list;
	fst = list->next;
	while (fst && slw && fst->next)
	{
		if (slw == fst)
		{
			return (1);
		}
		slw = slw->next;
		fst = fst->next->next;
	}
	return (0);
}
