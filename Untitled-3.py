
{
    class Program
    {
        static void Main(string[] args)
        {
            int contador = 0;

            for (int i = 1; i <= 50; i++)
            {
                if (i % 2 == 0)
                {
                    contador++;
                }
            }

            Console.WriteLine("Cantidad de números pares entre 1 y 50: " + contador);
            Console.ReadKey();
        }
    }
}
