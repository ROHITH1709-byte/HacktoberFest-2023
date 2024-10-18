public class Wrapper {
    public static void main(String[] args) {
        Wrapper x = new Wrapper();
        Wrapper b = new Wrapper();
        
        // Setting references to null to make them eligible for garbage collection
        x = null;
        b = null;
        
        // Creating another instance
        new Wrapper();
        
        // Suggesting to the JVM to perform garbage collection
        System.gc(); // Note: This is just a request
    }

    @Override
    protected void finalize() throws Throwable {
        try {
            System.out.println("This is GC");
        } finally {
            super.finalize(); // Call to the superclass's finalize method
        }
    }
}
