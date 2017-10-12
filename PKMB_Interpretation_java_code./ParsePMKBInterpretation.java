/*********************************************************************/
/** Class Name:    ParsePMKBInterpretation                          **/
/** Description:   We parse file and extract info from the web      **/ 
/**                pages on PMKB Interpretation                     **/
/**                                                                 **/
/** Author:        Dianwei Han                                      **/
/**                Department of Genetics&Genomic Sci, Mount Sinai  **/
/** Copyright:     2017, Mount Sinai, Medicine School               **/
/*********************************************************************/

//package parsepmkb;
import java.io.*;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import org.apache.commons.lang3.StringUtils;

public class ParsePMKBInterpretation {
     

    public static class Interpretation {

        String Tumor;
        String Tissue;
        String Variants;
        String Interpretation;

        public Interpretation () {}
    }       

    static ArrayList<String> interpretation_fieldNames = new ArrayList<String>();
    static ArrayList<Interpretation> interpretations = new ArrayList<Interpretation>();

    public ParsePMKBInterpretation(){}

    public static String readFile(String inf) throws IOException, FileNotFoundException {
         
        String strLine = null;
        StringBuilder sb = new StringBuilder();
        FileInputStream fstream = new FileInputStream(inf);
        BufferedReader br = new BufferedReader(new InputStreamReader(fstream));

        try {

            //Read File Line By Line
            while ((strLine = br.readLine()) != null)   {
                sb.append(strLine);
            }
        }
        catch (Exception e){
            System.err.println(e.getMessage());
        }
        return sb.toString();

    }

    public static ArrayList<String> extractStringBetween(String str, String start, String end) {
   
        ArrayList<String> result = new ArrayList<String>();
        String[] firstStr = str.split("\\"+end);
        for (String fstr : firstStr) {
            String[] secondStr = fstr.split("\\"+start);
            result.add(secondStr[1]);
        } 

        return result;
        
    }


    public static void parseData(String str) {
     
        /* extract field names */
 
        Pattern pattern = Pattern.compile("<thead>(.+)</thead>");
        Matcher matcher = pattern.matcher(str);
        matcher.find();
        String header = matcher.group(1);
        String thead = StringUtils.substringBetween(header, "<tr>", "</tr>");
        
        interpretation_fieldNames = extractStringBetween(thead, "<th>", "</th>"); 
        System.out.println("--------------------------------------------------------------------");
        System.out.println("Field names");
        System.out.println(interpretation_fieldNames);
        System.out.println("--------------------------------------------------------------------");

        /* extract interpretation info */ 

        String tbody = StringUtils.substringBetween(str, "<tbody>", "</tbody>");
        String[] trStr= tbody.split("\\"+"</tr>");
 System.out.println("NUM " + trStr.length);


        for (int i = 0; i < trStr.length ; i ++) {
            Interpretation rcd = new Interpretation();
            String[] intrStr = trStr[i].split("\\<td>"); 

System.out.println("num of fields "+ intrStr.length);

            // handle each element one by one
for (int j=0; j<5; j++) {
System.out.println("-----------------");
System.out.println(intrStr[j]);
System.out.println("-----------------");
}
            String[] temp = intrStr[1].split("\\</span></td>");
            
            if (temp.length == 1) {
                 rcd.Tumor = temp[0];
            }
            else {
                 rcd.Tumor = "";
            }
System.out.println(rcd.Tumor);
            temp = intrStr[2].split("\\</span></td>");
            if (temp.length == 1) {
                 rcd.Tissue = temp[0];
            }
            else {
                 rcd.Tissue = "";
            }
System.out.println(rcd.Tissue);

            temp = intrStr[3].split("\\</span></td>");
            if (temp.length == 1) {
                 rcd.Variants = temp[0];
            }
            else {
                 rcd.Variants = "";
            }
System.out.println(rcd.Variants);
            temp = intrStr[4].split("\\</span></td>");
            if (temp.length == 1) {
                 rcd.Interpretation = temp[0];
            }
            else {
                 rcd.Interpretation ="";
            }
System.out.println(rcd.Interpretation);
            interpretations.add(rcd);
        
        }
        // print out the content of interpretation file
        System.out.println("content of interpretations");
        System.out.println();
        for (int k = 0 ; k < interpretations.size(); k++) {
            System.out.println(k +" " + interpretations.get(k).Tumor + " " + interpretations.get(k).Tissue 
                                      + " " + interpretations.get(k).Variants + " " + interpretations.get(k).Interpretation);
        }

        
        
    }

    public static void main(String[] args) throws IOException {
     
        String rawData = readFile(args[0]);
        //System.out.println(rawData);
        parseData(rawData);
    }
}
