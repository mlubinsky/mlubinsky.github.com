import java.util.List;
import java.util.Map;
import java.util.Iterator;
import java.io.FileInputStream;
import java.io.DataInputStream;
import java.io.IOException;
//http://www.ibm.com/developerworks/library/x-javaxpathapi/index.html 
public class XMLDriver {

 public static void main(String args[]) throws IOException {
  try{
       if (args.length == 0 ) {
          System.err.println("Please provide input XML file");
          System.exit(0);
       }
       String fname=args[0];
       DataInputStream dis = new DataInputStream((new FileInputStream(fname)));
       List<Map<String,String>> ls = XMLReader.getAll(dis,"book");
       Iterator it=ls.iterator();
       while(it.hasNext())        {
          Map mm=(Map)it.next();
          System.out.println("we got : "+mm);
       } 
      dis.close();
          
      dis = new DataInputStream((new FileInputStream(fname)));
      String query ="//book[author='Neal Stephenson']/title/text()";  //find the book title by author
      System.out.println("query ="+ query  );
      String s = XMLReader.getAttrFromXML(dis,query);
      if (s.isEmpty()){
                System.err.println("This query returns nothing");
      } else {
                System.out.println("Result: "+ s  );
      }
      dis.close(); 
       
      System.exit(0);
   } catch (Exception e){
       System.err.println(e);
       e.printStackTrace(System.err); 
       throw new RuntimeException("Exception in XMLDriver");
   }
 } // end of main
}

