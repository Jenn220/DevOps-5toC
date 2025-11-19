public class CalculatorTest {
    
    private static Calculator calc;
    private static int aprobadas = 0;
    private static int fallidas = 0;
    
    public static void main(String[] args) {
        calc = new Calculator();
        
        System.out.println("Ejecutando pruebas automatizadas");
        System.out.println("-----------------------------------");
        
        probarSuma();
        probarResta();
        probarMultiplicacion();
        probarDivision();
        probarDivisionCero();
        
        System.out.println("-----------------------------------");
        System.out.println("Pruebas aprobadas: " + aprobadas);
        System.out.println("Pruebas fallidas: " + fallidas);
        
        if (fallidas > 0) {
            System.exit(1);
        }
        System.out.println("Todas las pruebas pasaron correctamente");
    }
    
    private static void probarSuma() {
        int resultado = calc.sumar(5, 3);
        if (resultado == 8) {
            System.out.println("PASS - Prueba de suma");
            aprobadas++;
        } else {
            System.out.println("FAIL - Prueba de suma (esperado: 8, obtenido: " + resultado + ")");
            fallidas++;
        }
    }
    
    private static void probarResta() {
        int resultado = calc.restar(10, 4);
        if (resultado == 6) {
            System.out.println("PASS - Prueba de resta");
            aprobadas++;
        } else {
            System.out.println("FAIL - Prueba de resta (esperado: 6, obtenido: " + resultado + ")");
            fallidas++;
        }
    }
    
    private static void probarMultiplicacion() {
        int resultado = calc.multiplicar(7, 6);
        if (resultado == 42) {
            System.out.println("PASS - Prueba de multiplicacion");
            aprobadas++;
        } else {
            System.out.println("FAIL - Prueba de multiplicacion (esperado: 42, obtenido: " + resultado + ")");
            fallidas++;
        }
    }
    
    private static void probarDivision() {
        double resultado = calc.dividir(15, 3);
        if (resultado == 5.0) {
            System.out.println("PASS - Prueba de division");
            aprobadas++;
        } else {
            System.out.println("FAIL - Prueba de division (esperado: 5.0, obtenido: " + resultado + ")");
            fallidas++;
        }
    }
    
    private static void probarDivisionCero() {
        try {
            calc.dividir(10, 0);
            System.out.println("FAIL - Prueba de division por cero (deberia lanzar excepcion)");
            fallidas++;
        } catch (ArithmeticException e) {
            System.out.println("PASS - Prueba de division por cero");
            aprobadas++;
        }
    }
}