/*********************************************************************/
/** Class Name:    ParsePMKBData                                    **/
/** Description:   We parse file and extract info from the web      **/ 
/**                pages on PMKB                                    **/
/**                                                                 **/
/** Author:        Dianwei Han                                      **/
/**                Department of Genetics&Genomic Sci, Mount Sinai  **/
/** Copyright:     2017, Mount Sinai, Medicine School               **/
/*********************************************************************/

import java.io.*;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import org.apache.commons.lang3.StringUtils;
       

public class ParsePMKBData {
     

    public static class Record {

        String Gene;
        String Type;
        String Description;
        String Cosmic_ID;
        String DNA_change;
        String Exon;

        public Record () {}
    }       

    static ArrayList<String> fieldNames = new ArrayList<String>();
    static ArrayList<Record> records = new ArrayList<Record>();

    public ParsePMKBData(){}

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
        
        fieldNames = extractStringBetween(thead, "<th>", "</th>"); 
        System.out.println("--------------------------------------------------------------------");
        System.out.println("Field names");
        System.out.println(fieldNames);
        System.out.println("--------------------------------------------------------------------");

        /* extract record info */ 
        String tbody = StringUtils.substringBetween(str, "<tbody>", "</tbody>");
        String[] trStr= tbody.split("\\"+"</tr>");
        for (int i = 0; i < trStr.length ; i ++) {
            Record rcd = new Record();
            String[] intrStr = trStr[i].split("\\<td><span>"); 

            // handle each element one by one
            String[] temp = intrStr[1].split("\\</span></td>");
            
            if (temp.length == 1) {
                 rcd.Gene = temp[0];
            }
            else {
                 rcd.Gene = "";
            }
            temp = intrStr[2].split("\\</span></td>");
            if (temp.length == 1) {
                 rcd.Type = temp[0];
            }
            else {
                 rcd.Type = "";
            }

            temp = intrStr[3].split("\\</span></td>");
            if (temp.length == 1) {
                 rcd.Description = temp[0];
            }
            else {
                 rcd.Description = "";
            }
            temp = intrStr[4].split("\\</span></td>");
            if (temp.length == 1) {
                 rcd.Cosmic_ID = temp[0];
            }
            else {
                 rcd.Cosmic_ID ="";
            }
            temp = intrStr[5].split("\\</span></td>");
            if (temp.length == 1) {
                 rcd.DNA_change = temp[0];
            } else {
                 rcd.DNA_change = "";
            }
            temp = intrStr[6].split("\\</span></td>");
            if (temp.length == 1) {
                 rcd.Exon = temp[0];
            } else {
                 rcd.Exon = "";
            }
            records.add(rcd);
        
        }
        // print out the content of variant file
        System.out.println("content of records");
        System.out.println();
        for (int k = 0 ; k < records.size(); k++) {
            System.out.println(k +" " + records.get(k).Gene + " " + records.get(k).Type + " " + records.get(k).Description 
                                      + " " + records.get(k).Cosmic_ID + " " + records.get(k).DNA_change + " " + records.get(k).Exon);
        }
        
        
    }

    public static void main(String[] args) throws IOException {
     
        String rawData = readFile(args[0]);
        parseData(rawData);
    }
}
