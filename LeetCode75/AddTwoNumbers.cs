using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//https://leetcode.com/problems/add-two-numbers/
//Medium
namespace AddTwoNumbers
{

    public class AddTwoNumbers
    {
        public static void Main(string[] args)
        {
            int[] list1 = new int[3];
            int[] list2 = new int[3];

            list1[0] = 2;
            list1[1] = 4;
            list2[2] = 3;

            list2[0] = 5;
            list2[1] = 6;
            list2[2] = 4;

            ListNode l1 = new ListNode();
            ListNode l2 = new ListNode();
            
            for(int i=0; i< 3; i++)
            {
                l1.val = list1[i];
                l2.val = list2[i];

                l1.next = new ListNode();
                l2.next = new ListNode();

                if(i < 3)
                {
                    l1 = l1.next;
                    l2 = l2.next;
                }
            }


            
            solution(l1, l2);
        }


        public static ListNode solution(ListNode l1, ListNode l2)
        {
            int figure = 1;

            int number1 = 0;
            int number2 = 0;

            while(l1 != null || l2 != null)
            {
                if(l1 != null)
                {
                    number1 += l1.val*(figure);
                    l1 = l1.next;
                }

                if(l2 != null)
                {
                    number2 += l2.val*(figure);
                    l2 = l2.next;
                }

                figure *= 10;
            }

            return null;

        }

    }

    public class ListNode
    {
         public int val;
         public ListNode next;
         public ListNode(int val = 0, ListNode next = null)
        {
            this.val = val;
            this.next = next;
        }
    }





}
