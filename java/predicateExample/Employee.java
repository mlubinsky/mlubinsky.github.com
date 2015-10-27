package predicateExample;

public class Employee {

   public Employee(Integer id, Integer age, String gender, String fName, String lName){
       this.id = id;
       this.age = age;
       this.gender = gender;
       this.firstName = fName;
       this.lastName = lName;
   }

   private Integer id;
   private Integer age;
   private String gender;
   private String firstName;
   private String lastName;

   public String getGender(){ return gender;}
   public int getAge(){ return age;}

   //Please generate Getter and Setters
   @Override
   public String toString() {
           return this.id.toString()+" - "+this.age.toString();
   }
}
