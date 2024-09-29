package ADSA.Lab;

public class linkedList {
    public static void main(String[] args) {
        Node head = new Node(10);

        head.insert(5);
        head.insert(15);
        head.insert(8);
        head.insert(3);
        head.insert(7);
        head.insert(12);
        head.insert(18);

        head.print();
        System.out.println();

        if (head.contains(8)) {
            System.out.println("Element Found!!!");
        } else {
            System.out.println("Element not Found!!!");
        }

        head.printTraversal(8);
        System.out.println();

        head.delete(8);
        head.print();
        System.out.println();

        head.reverse();
        head.print();
        System.out.println();

        head.reverseRecursively();
        head.print();
        System.out.println();

        head.reverseKNodes(3);
        head.print();
        System.out.println();
    }
}

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }

    void insert(int value) {
        if (next == null) {
            next = new Node(value);
        } else {
            next.insert(value);
        }
    }

    boolean contains(int value) {
        if (value == data) {
            return true;
        } else {
            if (next == null) {
                return false;
            } else {
                return next.contains(value);
            }
        }
    }

    void printTraversal(int value) {
        if (value == data) {
            System.out.print(data);
        } else {
            if (next == null) {
                System.out.println("Element not Found!!!");
            } else {
                System.out.print(data + " -> ");
                next.printTraversal(value);
            }
        }
    }

    void print() {
        System.out.print(data + " -> ");
        if (next != null) {
            next.print();
        }
    }

    void delete(int value) {
        if (next == null) {
            return;
        }
        if (next.data == value) {
            next = next.next;
        } else {
            next.delete(value);
        }
    }

    void reverse() {
        if (next == null) {
            return;
        }
        Node prev = null;
        Node current = this;
        Node next = null;
        while (current != null) {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        this.next = prev;
    }

    void reverseRecursively(Node current, Node prev) {
        if (current == null) {
            return;
        }
        if (current.next == null) {
            current.next = prev;
            return;
        }
        Node next = current.next;
        current.next = prev;
        reverseRecursively(next, current);
    }

    void reverseRecursively() {
        reverseRecursively(this, null);
    }

    void reverseKNodes(int k) {
        Node prev = null;
        Node current = this;
        Node next = null;
        int count = 0;
        while (current != null && count < k) {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
            count++;
        }
        if (next != null) {
            next.reverseKNodes(k);
        }
        this.next = prev;
    }
}