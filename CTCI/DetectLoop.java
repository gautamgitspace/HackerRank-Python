/**
 * Created by Gautam on 7/3/16.
 */
public class CTCI2_6
{
    private static LinkedListNode FindBeginning(LinkedListNode head)
    {
        LinkedListNode slow = head;
        LinkedListNode fast = head;

        //while fast.next!=null #GoodShit
        while (fast != null && fast.next != null)
        {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast)
            {
                System.out.println("HERE WE MEET AT " + slow.data);
                break;
            }
        }
        //Check if no loop exists
        if (fast == null || fast.next == null)
        {
            return null;
        }

        slow = head;
        while (slow != fast)
        {
            slow = slow.next;
            fast = fast.next;
        }
        // At this point slow=fast=starting of the loop
        return fast;
    }

    public static void main(String[] args)
    {
        int list_length = 100;
        int k = 45;
        //Generate List
        LinkedListNode[] nodes = new LinkedListNode[list_length];
        for (int i = 0; i < list_length; i++)
        {
            nodes[i] = new LinkedListNode(i, null, i > 0 ? nodes[i - 1] : null);
        }

        //Force loop
        nodes[list_length - 1].next = nodes[list_length - k];

        LinkedListNode loop = FindBeginning(nodes[0]);
        if (loop == null)
        {
            System.out.println("Lucky to survive. No loop found");
        }
        else
        {
            System.out.println("Starting point of loop: " + loop.data);
        }
    }
}
