package ADSA.Lab;

public class linkedList {
    public static void main(String[] args) {
        Node head = new Node(10);

        head.addNode(20);
        head.addNode(30);
        head.addNode(40);
        head.addNode(50);

        head.printList();
    }
}

class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }

    public void addNode(int value) {
        if (this.next == null) {
            this.next = new Node(value);
        } else {
            this.next.addNode(value);
        }
    }

    public void printList() {
        System.out.print(this.data + " -> ");
        if (this.next != null) {
            this.next.printList();
        }
    }
}