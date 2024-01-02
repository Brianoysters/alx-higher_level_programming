#include "lists.h"

/**
 * check_cycle - a function that checks presence
 * of a cycle in a linked list
 * @list: list parameter
 *
 * Return: 1 if cycle exist, 0 if non-existent
 */

int check_cycle(listint_t *list)
{
	listint_t *mode_sp = list;
	listint_t *max_sp = list;

	if (!list)
		return (0);

	while (mode_sp && max_sp && max_sp->next)
	{
		mode_sp = mode_sp->next;
		max_sp = max_sp->next->next;
		if (mode_sp == max_sp)
			return (1);
	}
	return (0);
}
