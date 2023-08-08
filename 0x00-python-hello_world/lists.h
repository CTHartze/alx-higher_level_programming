#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list function
 * @n: integer pointer
 * @next: pointer to next node
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);
listint_t *add_nodeint(listint_t **head, const int n);

#endif /* LISTS_H */
