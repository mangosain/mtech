package ADSA.Lab;

import java.io.*;

public class binarySearchTree {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Node root = new Node(10);

        root.insert(5);
        root.insert(15);
        root.insert(8);
        root.insert(3);
        root.insert(7);
        root.insert(12);
        root.insert(18);

        System.out.print("Enter the element to be searched: ");
        int value = Integer.parseInt(br.readLine());

        if (root.contains(value)) {
            System.out.println("Element Found!!!");
        } else {
            System.out.println("Element not Found!!!");
        }

        System.out.print("Enter the element to be printed: ");
        value = Integer.parseInt(br.readLine());
        root.printTraversal(value);

        System.out.print("\nInOrder Traversal:");
        root.printInOrder();

        System.out.print("\nPreOrder Traversal:");
        root.printPreOrder();

        System.out.print("\nPostOrder Traversal:");
        root.printPostOrder();
    }
}

class Node {
    int data;
    Node left;
    Node right;

    Node(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }

    void insert(int value) {
        if (value <= data) {
            if (left == null) {
                left = new Node(value);
            } else {
                left.insert(value);
            }
        } else {
            if (right == null) {
                right = new Node(value);
            } else {
                right.insert(value);
            }
        }
    }

    boolean contains(int value) {
        if (value == data) {
            return true;
        } else if (value < data) {
            if (left == null) {
                return false;
            } else {
                return left.contains(value);
            }
        } else {
            if (right == null) {
                return false;
            } else {
                return right.contains(value);
            }
        }
    }

    void printTraversal(int value) {
        if (value == data) {
            System.out.print(data);
        } else if (value < data) {
            if (left == null) {
                System.out.println("Element not Found!!!");
            } else {
                System.out.print(data + " -> ");
                left.printTraversal(value);
            }
        } else {
            if (right == null) {
                System.out.println("Element not Found!!!");
            } else {
                System.out.print(data + " -> ");
                right.printTraversal(value);
            }
        }
    }

    void printInOrder() {
        if (left != null) {
            left.printInOrder();
        }
        System.out.print(data + " ");
        if (right != null) {
            right.printInOrder();
        }
    }

    void printPreOrder() {
        System.out.print(data + " ");
        if (left != null) {
            left.printPreOrder();
        }
        if (right != null) {
            right.printPreOrder();
        }
    }

    void printPostOrder() {
        if (left != null) {
            left.printPostOrder();
        }
        if (right != null) {
            right.printPostOrder();
        }
        System.out.print(data + "");
    }
}