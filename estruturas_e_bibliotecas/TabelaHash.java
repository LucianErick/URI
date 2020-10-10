import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * problem: tabelas hash, hash tables
 * number: #1256
 */

public class Main {
    private static List<Integer>[] chainedHashTable;
    private static Scanner sc = new Scanner(System.in);
    private static int qntEnderecos;
    private static List<String> outputList;

    public static void main(String[] args) throws IOException {

        outputList = new ArrayList<>();

        int numberOfTests = sc.nextInt();
        for(int i = 0; i < numberOfTests; i++){

            qntEnderecos = sc.nextInt();

            int qntChaves = sc.nextInt();
            chainedHashTable = (ArrayList<Integer>[]) new ArrayList[qntEnderecos];

            for(int j = 0; j < qntChaves; j++){
                int value = sc.nextInt();
                insertIntoHashTable(value);
            }
            saveOutput();
        }

        printOutput();
    }

    public static void insertIntoHashTable(int keyValue){
        int hash = getHash(keyValue);
        if(chainedHashTable[hash] == null)
            chainedHashTable[hash] = new ArrayList<>();

        chainedHashTable[hash].add(keyValue);
    }

    public static int getHash(int element){
        return element % qntEnderecos;
    }


    public static void saveOutput(){
        String output = generateOutputString();
        outputList.add(output);
    }

    public static String generateOutputString(){
        String output = "";
        for(int i = 0; i < chainedHashTable.length; i ++){
            List<Integer> key = chainedHashTable[i];
            output += i + " -> ";
            if(key != null){
                for(int element : key){
                    output += element + " -> ";
                }
            }
            output += "\\\n";
        }
        return output;
    }

    public static void printOutput(){
        for(int i = 0; i < outputList.size(); i ++){
            if(i == outputList.size()-1)
                System.out.print(outputList.get(i));
            else
                System.out.println(outputList.get(i));
        }

    }

}