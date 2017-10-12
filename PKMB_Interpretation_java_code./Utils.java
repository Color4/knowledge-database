import java.io.*;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;

public class Utils {

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
}
