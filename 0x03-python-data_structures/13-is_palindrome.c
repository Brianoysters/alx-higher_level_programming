#include "lists.h"
#include <stddef.h>

/**
 * reverse_listint - this function reverses a linked list.
 * @head: first parameter
 *
 * Return: ptr address
 */

void reverse_listint(listint_t **head)
{
  listint_t *initial = NULL;
  listint_t *current = *head;
  listint_t *next = NULL;

  while (current)
    {
      next = current->next;
      current->next = initial;
      initial = current;
      current = next;
    }

  *head = initial;
}

/**
 * is_palindrome - this function checks if a linked list is palindrome
 * @head: first parameter
 *
 * Return: 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
  listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

  if (*head == NULL || (*head)->next == NULL)
    return (1);

  while (1)
    {
      fast = fast->next->next;
      if (!fast)
	{
	  dup = slow->next;
	  break;
	}
      if (!fast->next)
	{
	  dup = slow->next->next;
	  break;
	}
      slow = slow->next;
    }

  reverse_listint(&dup);

  while (dup && temp)
    {
      if (temp->n == dup->n)
	{
	  dup = dup->next;
	  temp = temp->next;
	}
      else
	return (0);
    }

  if (!dup)
    return (1);

  return (0);
}
