public class Shelter{
    private int MAXIMUM_CAPACITY;
    private int currentCapacity;
    private String address;
    private String name;

    public Shelter(int max, int cur, String add, String n){
        MAXIMUM_CAPACITY = max;
        currentCapacity = cur;
        address = add;
        name = n;
    }

    public int getMaximumCapacity(){
        return MAXIMUM_CAPACITY;

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
