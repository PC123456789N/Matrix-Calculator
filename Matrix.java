// Codigo que calcula automaticamente matrizes em java
// autores: Brasilicio H e Kaio H
//     (Os Henriques)

import java.util.Scanner;

public class Matrix {

    // criar funcao que le os valores de uma matriz aqui

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Escolha sua operação: \n" +
                                "1. Soma (+) \n" +
                                "2. Subtracao (-) \n" +
                                "3. Multiplicacao (*) \n" +
                                "0. Sair (s)");
            String operacao = scanner.nextLine();

            System.out.println(operacao);

            scanner.close();

            break;
        }
    }
}