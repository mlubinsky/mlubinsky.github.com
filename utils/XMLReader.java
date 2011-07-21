import java.io.InputStream;

import java.util.List;
import java.util.LinkedList;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.ArrayList;

import org.w3c.dom.Document;
import org.w3c.dom.*;

import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;

import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathFactory;

import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;
import org.xml.sax.InputSource;

class XMLReader{
// http://www.javabeat.net/tips/182-how-to-query-xml-using-xpath.html
// http://www.ibm.com/developerworks/library/x-javaxpathapi/index.html
 public static String getAttrFromXML(InputStream stream, String attribute) throws Exception {
        XPathFactory xpf = XPathFactory.newInstance();
        XPath xpath = xpf.newXPath();
        XPathExpression xpe = xpath.compile(attribute);
        InputSource xml = new InputSource(stream);
        String result = xpe.evaluate(xml);
        return result;

 }
//   returns the list of maps
 public static List<Map <String,String>> getAll(InputStream is,String key_name){
    List <Map<String,String>> ls = new ArrayList<Map<String, String>>();
    try {
            DocumentBuilderFactory docBuilderFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder docBuilder = docBuilderFactory.newDocumentBuilder();
            Document   doc = docBuilder.parse (is); 

            doc.getDocumentElement().normalize();
            NodeList listOfCounters = doc.getElementsByTagName(key_name); // e.g.: property
            int totalCounters = listOfCounters.getLength();
            String key;
            String value;

            for(int s=0; s<listOfCounters.getLength() ; s++){

                Node node = listOfCounters.item(s);
                if(node.getNodeType() == Node.ELEMENT_NODE){

                  Element e = (Element)node;

                  NodeList keyList = e.getElementsByTagName("*"); // get all
                  int len =  keyList.getLength();   

                  Map <String,String> map = new LinkedHashMap<String, String>();
       
                  for ( int kk = 0; kk < len; kk++){
                     key = keyList.item(kk).getNodeName();
                     Element keyElement = (Element)keyList.item(kk);
                     NodeList textKeyList = keyElement.getChildNodes();
                     value = ((Node)textKeyList.item(0)).getNodeValue().trim(); 
                     map.put(key,value);
                 }
                 ls.add(map);
               }     // end of if(node.getNodeType() == Node.ELEMENT_NODE)
             }   // end of for(int s=0; s<listOfCounters.getLength() ; s++){

           //  status = true;

        }catch (SAXParseException err) {
          System.out.println ("** Parsing error" + ", line " + err.getLineNumber () + ", uri " + err.getSystemId ());
          System.out.println(" " + err.getMessage ());
        }catch (SAXException e) {
          Exception x = e.getException ();
          ((x == null) ? e : x).printStackTrace ();
        }catch (Throwable t) {
          t.printStackTrace ();
        }

        return ls;
  }
}
