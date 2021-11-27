#include "lists.h"

/**
 * check_cycle - checks if a list has a cycle.
 *
 * @list: pointer to head of list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *fir_p = list, *sec_p = list;

	while (fir_p && sec_p && sec_p->next)
	{
		fir_p = fir_p->next;
		sec_p = sec_p->next->next;
		if (fir_p == sec_p)
			return (1);
	}
	return (0);
}
