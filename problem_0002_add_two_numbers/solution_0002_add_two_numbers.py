# First solution
#  long solution, trying to get the logic of the problem and how linked list works
# Execution time = 3ms, Memory size = 19.3mb
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #creates a dummy node, an initial dummy node say 0
        # below will create 0 -> None
        #this contain the sum
        dummy_head = ListNode(0)

        #this is pointer to dummy node
        # for visualization, 0 -> None
        #                    |
        #                 current
        current = dummy_head

        #current_1 and current_2, like current, is a pointer
        # for visualization say l1 is 2 -> 4 -> 3,
        #       2 -> 4 -> 3 -> None
        #       |
        #   current_1
        # for visualization say l2 is 5 -> 6 -> 4,
        #       5 -> 6 -> 4 -> None
        #       |
        #   current_2
        current_1 = l1
        current_2 = l2
        
        #this will handle the tens digit of sub_total if total is greater than 10
        carry = 0

        #my first thinking is to iterate through l1 first until its end
        while current_1:
            #check if the pointer current_2 is not at the end of l2
            if current_2:
                #get the sum of the nodes of l1 and l2 and carry
                total = current_1.val + current_2.val + carry
                #sets carry to 0 or 1 depending if total is greater than 10 or not
                carry = total // 10
                #gets the ones digit of total
                sub_solution = total % 10

                #initial new_node variable with ListNode class and sub_solution
                # as parameter
                #example, the first sum is 7. new_node will become 7 -> None
                new_node = ListNode(sub_solution)
                #now, calling current.next = new_node will resul to
                #   0 -> 7 -> None
                current.next = new_node
                #current = new_node will move the current pointer to new_node
                # which is 7
                #   0 -> 7 -> None
                #        |
                #     current
                current = new_node

                #move the pointers to next node, it can result to a None value
                # like current_1 = None if the pointer reaches the end of linked list
                current_1 = current_1.next
                current_2 = current_2.next
            #this handles when l2 reached its end, current_2 == None
            else:
                total = current_1.val + carry
                carry = total // 10
                sub_solution = total % 10

                new_node = ListNode(sub_solution)
                current.next = new_node
                current = new_node

                current_1 = current_1.next

        #this handles the condition where l2 is longer than l1
        while current_2:
            total = current_2.val + carry
            carry = total // 10
            sub_solution = total % 10

            new_node = ListNode(sub_solution)
            current.next = new_node
            current = new_node

            current_2 = current_2.next

        #handles the addition of carry to last node or tail node of sum linked list
        if carry == 1:
            new_node = ListNode(carry)
            current.next = new_node
            current = new_node

        #the reason dummy_head.next is returned here is to disregard the dummy node
        # set at the beginning. For example, after going through l1 and l2,
        # dummy_head linked list is equal to
        #       0 -> 7 -> 0 -> 8 -> None
        # where 0, the head, is the dummy node.
        # so, returning dummy_head.next will only return 7 -> 0 -> 8 -> None
        # which is the correct sum
        return dummy_head.next


# Second solution
#  factored code of first solution
# Execution time = 3ms, Memory size = 19.4mb
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #initialized dummy node of 0, 0 -> None
        dummy_head = ListNode(0)

        #set pointer to initialized dummy node
        current = dummy_head

        #get the value of first node of given ListNode
        current_1 = l1
        current_2 = l2
        carry = 0

        #check simultaneously three condition to have a single loop, loop will not
        # terminate as long as there is node from l1 or l2 and also checks for
        # trailing carry at the end
        while (current_1 or current_2 or carry == 1):
            if current_1:
                #if current_1 points to node that is not None, set its value to
                # num_1 and point the current_1 pointer to next node
                num_1 = current_1.val
                current_1 = current_1.next
            else:
                #this will handle the addition if node value is None
                num_1 = 0

            if current_2:
                #if current_2 points to node that is not None, set its value to
                # num_2 and point the current_2 pointer to next Node
                num_2 = current_2.val
                current_2 = current_2.next
            else:
                #this will handle the addition if node value is None
                num_2 = 0

            total = num_1 + num_2 + carry
            carry = total // 10
            sub_total = total % 10

            #initialized sub_total to a ListNode class
            new_node = ListNode(sub_total)
            #connect current node to new_node
            current.next = new_node
            #move pointer to new_node
            current = new_node

        return dummy_head.next