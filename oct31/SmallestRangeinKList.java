import java.util.Scanner;

class SmallestRangeinKList 
{ 
    static class Node  
    { 
        int ele; // The element to be stored 
        int i;     // index of the list from which the element is taken 
        int j;     // index of the next element  to be picked from list 
  
        Node(int a, int b, int c) { 
            this.ele = a; 
            this.i = b; 
            this.j = c; 
        } 
    } 
   
    static class MinHeap 
    { 
        Node[] harr; // array of elements in heap 
        int size;     // size of min heap 
   
        MinHeap(Node[] arr, int size) {   //creates a min heap  of given size 
            this.harr = arr; 
            this.size = size; 
            int i = (size - 1) / 2; 
            while (i >= 0)  { 
                MinHeapify(i); 
                i--; 
            } 
        } 
  
        int left(int i)  { 
            return 2 * i + 1; 
        } 
   
        int right(int i)  { 
            return 2 * i + 2; 
        } 
  
        // to heapify a subtree with root at given index 
        void MinHeapify(int i)  
        { 
            int l = left(i); 
            int r = right(i); 
            int small = i; 
            if (l < size && harr[l].ele < harr[i].ele) 
                small = l; 
            if (r < size && harr[r].ele < harr[small].ele) 
                small = r; 
            if (small != i) { 
                swap(small, i); 
                MinHeapify(small); 
            } 
        } 
  
        void swap(int i, int j) 
        { 
            Node temp = harr[i]; 
            harr[i] = harr[j]; 
            harr[j] = temp; 
        } 
  
        // to get the root 
        Node getMin() { 
            return harr[0]; 
        } 
  
        // to replace root with new node x and heapify() new root 
        void replaceMin(Node x) 
        { 
            harr[0] = x; 
            MinHeapify(0); 
        } 
    } 
  
    static void findSmallestRange(int[][] arr, int k)  
    { 
        int range = Integer.MAX_VALUE; 
        int min = Integer.MAX_VALUE; 
        int max = Integer.MIN_VALUE; 
        int start = -1, end = -1; 
  
        int n = arr[0].length; 
  
        // Create a min heap with k heap nodes.  Every heap node has first element of an list 
        Node[] arr1 = new Node[k]; 
        for (int i = 0; i < k; i++)  
        { 
            Node node = new Node(arr[i][0], i, 1); 
            arr1[i] = node; 
            // store max element 
            max = Math.max(max, node.ele); 
        } 
  
        // Create the heap 
        MinHeap mh = new MinHeap(arr1, k); 
        while (true) { 
            Node root = mh.getMin();  
            min = root.ele; // update min
            // update range 
            if (range > max - min + 1) { 
                range = max - min + 1; 
                start = min; 
                end = max; 
            } 
  
            // Find the next element that will replace current root of heap.  
            if (root.j < n) { 
                root.ele = arr[root.i][root.j]; 
                root.j++; 
  
                // update max element 
                if (root.ele > max) 
                    max = root.ele; 
            } else
                break;    // end of any list 
  
            // Replace root with next element of list 
            mh.replaceMin(root); 
        } 
        System.out.print("The smallest range is [" + start + " " + end + "]"); 
    } 

    public static void main(String[] args)  
    { 
        int arr[][];
        Scanner s = new Scanner(System.in);
        System.out.print("Enter no of lists: ");
        int row = s.nextInt();
        System.out.print("Enter length of each lists: ");
        int len = s.nextInt();
        arr = new int[row][len]; 
        System.out.println("Enter the elements of each list line by line: ");
        for(int i=0; i<row; i++)
            for(int j=0; j<len; j++)
                arr[i][j] = s.nextInt();

        len = arr.length;
        findSmallestRange(arr, len); 
    } 
} 

/*
OUTPUT

Enter no of lists: 4
Enter length of each lists: 4
Enter the elements of each list line by line:
2 6 15 19
1 4 8 12
5 9 17 21
7 10 20 30
The smallest range is [4 7]
*/