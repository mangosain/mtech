
public class test {
    public static void main(String[] args) {
        // a code that counts the number of occurances of the current character that are
        // to the right of it and adds it to an array

        int[] arr = countOccurances("abaab");

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }

    }

    public static int[] countOccurances(String str) {
        int[] arr = new int[str.length()];
        for (int i = 0; i < str.length(); i++) {
            int count = 0;
            for (int j = i + 1; j < str.length(); j++) {
                if (str.charAt(i) == str.charAt(j)) {
                    count++;
                }
            }
            arr[i] = count;
        }
        return arr;
    }
}