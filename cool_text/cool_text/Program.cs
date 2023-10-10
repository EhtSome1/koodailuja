namespace program
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Give a word (english and only letters and numbers)");
            
            readline:
            string? word = Console.ReadLine();

            if (word == null)
            {
                Console.Clear();
                Console.WriteLine("Give a word:");
                goto readline;
            }
            char[] splitword = word.ToCharArray();

            char[] smallLetters = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
            char[] bigLetters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
            char[] numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
            char[] compWord = new char[word.Length];

            Console.Clear();

            for(int i = 0; i < splitword.Length; i++)
            {
                int n = 0;
                do
                {
                    if (smallLetters.Contains(splitword[i]))
                    {
                        compWord[i] = smallLetters[n];
                    }
                    if (bigLetters.Contains(splitword[i]))
                    {
                        compWord[i] = bigLetters[n];
                    }
                    if (numbers.Contains(splitword[i]))
                    {
                        compWord[i] = numbers[n];
                    }
                    if (!smallLetters.Contains(splitword[i]) && !bigLetters.Contains(splitword[i]) && !numbers.Contains(splitword[i]))
                    {
                        compWord[i] = splitword[i];
                    }

                    string str = new string(compWord);

                    Console.Clear();

                    Console.WriteLine(str);
                    n++;

                    Thread.Sleep(20);

                } while (compWord[i] != splitword[i]);
            }
        }
    }
}



