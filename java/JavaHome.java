import java.io.File;
import java.io.IOException;
public class JavaHome{
 
    public static void main(String args[]) throws IOException {
        System.out.println(getJDKDir());
    }
 
    public static String getJDKDir() {
        File javaHome = new File( System.getProperty( "java.home" ) ).getParentFile();
        File jdkDirectory = null;
        if( javaHome.getName().contains( "jdk" ) ) {
            //happens in IntelliJ
            jdkDirectory = javaHome;
        } else {
            //General Scenario - eclipse / command line
            File[] childDirs = javaHome.listFiles();
            for(File file : childDirs) {
                if(file.getName().contains("jdk")) {
                    jdkDirectory = file;
                    break;
                }
            }
             
        }
        return jdkDirectory.getAbsolutePath();
    }
 
}
