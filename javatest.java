import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

class program
{
    public static void main(String[] args)
    {
        LocalDate myObj = LocalDate.now();
        //System.out.println(myObj);

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd MM yyyy");
        String formattedString = myObj.format(formatter);


        if (formattedString[0] == "0")
        {

        }

        System.out.println(formattedString);
    }
}