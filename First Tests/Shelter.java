public class Shelter{
    private int maximum_capacity;
    private int currentCapacity;
    private String address;
    private String name;

    public Shelter(int max, int cur, String add, String n){
        maximum_capacity = max;
        currentCapacity = cur;
        address = add;
        name = n;
    }

    public int getMaximumCapacity(){
        return maximum_capacity;

    }
    public int getcurrentCapacity(){
        return currentCapacity;

    }
    public String getAddress(){
        return address;

    }
    public String getName(){
        return name;

    }
}
