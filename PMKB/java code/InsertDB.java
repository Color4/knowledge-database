import java.util.ArrayList;
import java.util.Iterator;
import java.io.*;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.FileInputStream;

import org.apache.poi.xssf.usermodel.XSSFWorkbook; 
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Cell;
import com.mysql.jdbc.jdbc2.optional.MysqlDataSource;
import java.sql.Connection;
import java.sql.Statement;
import java.sql.PreparedStatement;
import java.sql.ResultSet; 
import java.sql.SQLException;



public class InsertDB {
    public static class PMKB_Interpretation {
        String Gene;
        String Tumor;
        String Tissue;
        String Variants;
        int Tier;
        String Interpretation;
        String Citations;
      
        public PMKB_Interpretation(){}

    }
    static ArrayList<PMKB_Interpretation> pmkb_ints = new ArrayList<PMKB_Interpretation>();

    public static void main(String[] args) throws FileNotFoundException, IOException, SQLException {


        // read pmid files and get all the Citations for each interpreation

        ArrayList<String> citations = new ArrayList<String>();
        for (int i = 0; i < 402; i++) {
           
            String strLine = null;
            StringBuilder sb = new StringBuilder();
            int j = i+1;
            FileInputStream fstream = new FileInputStream("output/out"+j);
            BufferedReader br = new BufferedReader(new InputStreamReader(fstream));

            try {

                 while ((strLine = br.readLine()) != null) {
                        sb.append(strLine);
                        sb.append(" ");
                 }
                 System.out.println("citation [" + sb +"]");
                 citations.add(sb.toString());
                 
     
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                fstream.close();
            }
            
        }
 
        System.out.println("cnt " + citations.size());

        // read excel file which contains tutor, tiusse, variant, and interpretatio fields
        try {

            FileInputStream file = new FileInputStream(new File("PMKB_Interpretation.xlsx"));

            //Create Workbook instance holding reference to .xlsx file
            XSSFWorkbook workbook = new XSSFWorkbook(file);

            //Get first/desired sheet from the workbook
            XSSFSheet sheet = workbook.getSheetAt(0);

            //Iterate through each rows one by one
            Iterator<Row> rowIterator = sheet.iterator();
            int cnt = 1;
            while (rowIterator.hasNext())
            {
                Row row = rowIterator.next();
                //For each row, iterate through all the columns
                Iterator<Cell> cellIterator = row.cellIterator();

                System.out.println(" cnt " + cnt);
                //static ArrayList<PMKB_Interpretation> pmkb_ints = new ArrayList<PMKB_Interpretation>();
                PMKB_Interpretation interpretation = new PMKB_Interpretation();
                int k = 0;
                while (cellIterator.hasNext()) 
                {
                    Cell cell = cellIterator.next();
                    //Check the cell type and format accordingly
                    switch (cell.getCellTypeEnum()) 
                    {
                        case NUMERIC:
                            System.out.print(cell.getNumericCellValue()+ "\t");
                            if (cnt > 1) {
                               if (k == 4) {
                        
                                interpretation.Tier = (int) cell.getNumericCellValue(); 
                               }
                            }
                            break;
                        case STRING:
                            String str = cell.getStringCellValue();
                            //System.out.println(cell.getStringCellValue() + "\t");
                            System.out.println(str + "\t");
System.out.println("-------------------------------------K " + k);
 
                    if (cnt > 1) {
                        if (k == 0) {
                           interpretation.Gene = str;
                        }
                        if (k == 1) {
                           interpretation.Tumor = str;
System.out.println( str + "size " + pmkb_ints.size());
                        } 

                        if (k == 2) {
                            interpretation.Tissue = str;
System.out.println( str + "size " + pmkb_ints.size());
                        }

                        if (k == 3) {
                            interpretation.Variants = str;
System.out.println( str + "size " + pmkb_ints.size());
                        }

                        if (k == 5) {
                            interpretation.Interpretation = str.replace("'","''");
                           // interpretation.Interpretation = str; 
                            interpretation.Citations = citations.get(cnt-2);
                           pmkb_ints.add(interpretation);
System.out.println( str + "size " + pmkb_ints.size());
                        }
                     }
                            break;
                    }

                    k++;
                }
                cnt ++;
                System.out.println("********************************");
            }
            file.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println("???????????????????????????????");
        for (PMKB_Interpretation pm : pmkb_ints) {
            System.out.println(pm.Gene);
            System.out.println(pm.Tumor);
            System.out.println(pm.Tissue);
            System.out.println(pm.Variants);
            System.out.println(pm.Tier);
            System.out.println(pm.Interpretation);
            System.out.println(pm.Citations);
        System.out.println("------------------------------------------");
         }

        // connection to DB and insert data into it.
        MysqlDataSource dataSource = new MysqlDataSource();
        dataSource.setUser("hand10");
        dataSource.setPassword("486321A!abc");
        dataSource.setServerName("db1.hpc.mssm.edu");
        dataSource.setDatabaseName("kb_CancerVariant_Curation");
        PreparedStatement stmt = null;
        Connection conn = null;
        try {
              conn = dataSource.getConnection();
            
            for (PMKB_Interpretation pm : pmkb_ints) {
            System.out.println(pm.Gene);
            System.out.println(pm.Tumor);
            System.out.println(pm.Tissue);
            System.out.println(pm.Variants);
            System.out.println(pm.Tier);
            System.out.println(pm.Interpretation);
            System.out.println(pm.Citations);
            stmt  = conn.prepareStatement("INSERT INTO PMKB_Han_20170425" +
                    "VALUES('"+pm.Gene+"', '"+pm.Tumor+"', '"+pm.Tissue+"', '"+pm.Variants+"', '"+pm.Tier+"', '"+pm.Interpretation+"', '"+pm.Citations+"')");
            //  stmt.executeUpdate();

            }
       } catch (SQLException e) {
           System.out.println(e);
       } finally {
            if (stmt != null) { 
                stmt.close();
            }
       }
        
    }
}
