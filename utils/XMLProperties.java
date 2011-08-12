import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.util.Date;
import java.util.Properties;

public class XMLProperties {
  public static void main(String args[]) throws Exception {
    Properties p = new Properties();

    p.put("Today", new Date().toString());
    p.put("User", "Incognito");

    FileOutputStream out = new FileOutputStream("user.props");
    p.storeToXML(out, "updated");

    FileInputStream in = new FileInputStream("user.props");

    p.loadFromXML(in);
    p.list(System.out);
  }
}