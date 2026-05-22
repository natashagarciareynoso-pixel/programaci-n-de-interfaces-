
using system;
 using sytem. collections.generic

class program 
{  
  // 1. definimos que es un "estudiante"
  (el molde)
  class estudiante 
 { 
     public string nombre;
     public int edad;

 }
 static void main()
 {
    // 2.creamos la lista donde guardamos a los alumnos 
        list<estudiante> lista = new
   list<estudiante>();

      // 3. agregamos 5 estudiantes de forma manual y clara
       // estudiante 1
       estudiante e1 = new estudiante();
       e1.nombre = "rhys larsen";
       e1.edad = 28;
       lista.add(e1);

       //estudiante 2
       estudiante e2 = new estudiante();
       e2.nombre = "damian";
       e2.edad = 18;
       lista.add(e2);


        // Estudiante 3

        Estudiante e3 = new Estudiante();

        e3.nombre = "Mario";

        e3.edad = 19;

        lista.Add(e3);

        // Estudiante 4

        Estudiante e4 = new Estudiante();

        e4.nombre = "Elena";

        e4.edad = 21;

        lista.Add(e4);

        // Estudiante 5

        Estudiante e5 = new Estudiante();

        e5.nombre = "Beatriz";

        e5.edad = 22;

        lista.Add(e5);

        // 4. Ordenar la lista por nombre (A-Z)

        // Usamos Sort con una comparación simple entre nombres

        lista.Sort((x, y) => x.nombre.CompareTo(y.nombre));

        // 5. Mostrar los resultados en la pantalla

        Console.WriteLine("--- Estudiantes ordenados por nombre ---");

        foreach (Estudiante est en lista)

        {

            Console.WriteLine("Nombre: " + est.nombre + " | Edad: " + est.edad);

        }

        // Esto evita que la ventana se cierre sola

        Console.WriteLine("\nPresiona cualquier tecla para salir...");

        Console.ReadKey();

    }

}
 

 