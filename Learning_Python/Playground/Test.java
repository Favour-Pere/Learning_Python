package Playground;
import java.util.ArrayList;
import java.util.Scanner;
public class Test {
    public static void main(String[] args) 
    {
        ArrayList<String> ineligble = new ArrayList<String>();

        ineligble.add("router");
        ineligble.add("broadplans");
        ineligble.add("companyplans");

        Scanner scan = new Scanner(System.in);

        System.out.println("Enter your plan: ");
        String plan = scan.next();

        if(ineligble.contains(plan))
        {
            System.out.println("You are not eligible ");
        }
        else
        {
            System.out.println("You are eligible ");
        }

        scan.close();
    }
}
