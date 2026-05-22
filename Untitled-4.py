
namespace FactorialDeSeis
{
    class Program
    {
        static void Main(string[] args)
        {
            int numero = 6;
            int factorial = 1;

            for (int i = 1; i <= numero; i++)
            {
                factorial *= i;
            }

            Console.WriteLine("El factorial de 6 es: " + factorial);
            Console.ReadKey();
        }
    }
}
