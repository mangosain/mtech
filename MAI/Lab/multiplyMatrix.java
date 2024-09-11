import java.io.*;

public class multiplyMatrix {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Enter the number of rows for the first matrix: ");
        int n1 = Integer.parseInt(br.readLine());

        System.out.print("Enter the number of columns for the first matrix: ");
        int m1 = Integer.parseInt(br.readLine());

        System.out.print("Enter the number of rows for the second matrix: ");
        int n2 = Integer.parseInt(br.readLine());

        System.out.print("Enter the number of columns for the second matrix: ");
        int m2 = Integer.parseInt(br.readLine());

        if (m1 != n2) {
            System.out.println("The matrices cannot be multiplied with each other.");
            return;
        }

        int[][] matrix1 = new int[n1][m1];
        int[][] matrix2 = new int[n2][m2];
        int[][] result = new int[n1][m2];

        System.out.println("Enter the elements of the first matrix: ");
        for (int i = 0; i < n1; i++) {
            for (int j = 0; j < m1; j++) {
                matrix1[i][j] = Integer.parseInt(br.readLine());
            }
        }

        System.out.println("Enter the elements of the second matrix: ");
        for (int i = 0; i < n2; i++) {
            for (int j = 0; j < m2; j++) {
                matrix2[i][j] = Integer.parseInt(br.readLine());
            }
        }

        for (int i = 0; i < n1; i++) {
            for (int j = 0; j < m2; j++) {
                for (int k = 0; k < m1; k++) {
                    result[i][j] += matrix1[i][k] * matrix2[k][j];
                }
            }
        }

        System.out.println("The first matrix is: ");
        for (int i = 0; i < n1; i++) {
            for (int j = 0; j < m1; j++) {
                System.out.print(matrix1[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println();

        System.out.println("The second matrix is: ");
        for (int i = 0; i < n2; i++) {
            for (int j = 0; j < m2; j++) {
                System.out.print(matrix2[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println("The result of the multiplication of the two matrices is: ");
        for (int i = 0; i < n1; i++) {
            for (int j = 0; j < m2; j++) {
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }
    }
}
