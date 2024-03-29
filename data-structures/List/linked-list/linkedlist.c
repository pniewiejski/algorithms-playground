/*
 * A very simple implementation of a singly linked list
 *
 * ISSUES:
 *     - Mind that in the code below I did not bother with any kind of error handling.
 *       It was meant to be a basic idea, not a viable solution.
 */

#include <stdio.h>
#include <stdlib.h>

struct node {
    int value;
    struct node* next;
};

typedef struct node node_t;

node_t* create_node(const int value, node_t* next_node) {
    node_t* node = (node_t*)malloc(sizeof(node_t));
    if (node == NULL) {
        printf("Error: could not allocate memory for a new node");
        exit(EXIT_FAILURE);
    }

    node->next = next_node;
    node->value = value;

    return node;
}

void prepend(node_t** head, const int value) {
    node_t* new_head = create_node(value, *head);
    *head = new_head;
}

void append(node_t* head, const int value) {
    node_t* cursor = head;
    while (cursor->next != NULL) cursor = cursor->next;

    node_t* new_node = create_node(value, NULL);
    cursor->next = new_node;
}

const int pop(node_t* head) {
    node_t* current = head;
    node_t* previous = NULL;

    while (current->next != NULL) {
        previous = current;
        current = current->next;
    }

    previous->next = NULL;
    const int poped_value = current->value;
    free(current);

    return poped_value;
}

const int pop_front(node_t** head) {  // We want to modify head
    if (*head == NULL) {
        printf("Error: Cannot pop from an empty list!");
        exit(EXIT_FAILURE);
    }

    node_t* new_head = (*head)->next;
    const int popped_value = (*head)->value;
    free(*head);
    *head = new_head;

    return popped_value;
}

node_t* reverse(node_t** head) {
    node_t* previous = NULL;
    node_t* current = *head;

    while (current != NULL) {
        node_t* tmp = current->next;
        current->next = previous;
        previous = current;
        current = tmp;
    }

    *head = previous;

    return *head;
}

node_t* search(node_t* head, int searched_value) {
    node_t* cursor = head;
    while (cursor != NULL) {
        if (cursor->value == searched_value) {
            return cursor;
        }
        cursor = cursor->next;
    }

    return NULL;
}

int remove_entry(node_t** head, node_t* entry) {
    node_t** cursor = head;

    while ((*cursor) != entry) {
        cursor = &(*cursor)->next;
    }

    free(*cursor);
    (*cursor) = entry->next;

    return 0;
}

int remove_kth_entry(node_t** head, int k) {
    node_t** cursor = head;
    int index = 0;
    while (index != k) {
        cursor = &(*cursor)->next;
        if (!(*cursor)) {
            printf("Argument out of range\n");
            return -1;
        }
        index++;
    }

    node_t* tmp = (*cursor)->next;
    free(*cursor);
    (*cursor) = tmp;

    return 0;
}

void print(const node_t* head) {
    const node_t* cursor = head;
    printf("--> Printing linked list. Starting from: %p\n", head);
    while (cursor != NULL) {
        printf("\tElement at %p; value: %d\n", cursor, cursor->value);
        cursor = cursor->next;
    }
    printf("<-- Printing linked list done\n");
}

int main() {
    printf("[TRACER] Create a head of a linked list");
    node_t* head = create_node(1, NULL);
    append(head, 2);
    append(head, 3);
    print(head);
    prepend(&head, 0);
    pop(head);
    print(head);
    reverse(&head);
    print(head);
    pop_front(&head);
    print(head);

    printf("[TRACER] Test searching for elements");
    append(head, 5);
    print(head);
    node_t* searched = search(head, 2);
    printf("Searched value found at: %p, with value: %d\n", searched,
           (searched ? searched->value : 0));
    searched = search(head, 5);
    printf("Searched value found at: %p, with value: %d\n", searched,
           (searched ? searched->value : 0));

    printf("[TRACER] Test removing entries by element's value");
    print(head);
    remove_entry(&head, searched);
    print(head);
    remove_entry(&head, head);  // This is a case where we can see why passing &head is important!
    print(head);

    printf("[TRACER] Test removing the k-th element\n");
    append(head, 6);
    append(head, 7);
    print(head);
    remove_kth_entry(&head, 2);
    print(head);
    return 0;
}