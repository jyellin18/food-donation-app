import java.util.Scanner;

public class Test{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);

        int max = s.nextInt();
        int cur = s.nextInt();
        s.nextLine(); // Clear the newline left in the buffer
        String address = s.nextLine();
        String name = s.nextLine();
        Shelter shelter = new Shelter(max, cur, address, name);
        
        System.out.println(shelter.getName()+" needs " + (shelter.getMaximumCapacity()-shelter.getcurrentCapacity())+" at "+shelter.getAddress());

        s.close();
    }
}