#include "lists.h"

/**
 * check_cycle - check if link has a cycle
 * @list: pointer to the list
 * Return: 0 if has cycle or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *p;
	listint_t *plst;

	p = list;
	plst = list;
	while (list && p && p->next)
	{
		list = list->next;
		p = p->next->next;

		if (list == p)
		{
			list = plst;
			plst = p;
			while (1)
			{
				p = plst;
				while (p->next != list && p->next != plst)
					p = p->next;
				if (p->next == list)
					break;
				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
