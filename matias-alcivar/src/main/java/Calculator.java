public class Calculator {
    
    public int sumar(int a, int b) {
        return a + b;
    }
    
    public int restar(int a, int b) {
        return a - b;
    }
    
    public int multiplicar(int a, int b) {
        return a * b;
    }
    
    public double dividir(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("Division por cero no permitida");
        }
        return (double) a / b;
    }
    
    public static void main(String[] args) {
        Calculator calculadora = new Calculator();
        System.out.println("Aplicacion iniciada correctamente");
        System.out.println("Suma: 5 + 3 = " + calculadora.sumar(5, 3));
        System.out.println("Resta: 5 - 3 = " + calculadora.restar(5, 3));
        System.out.println("Multiplicacion: 5 x 3 = " + calculadora.multiplicar(5, 3));
        System.out.println("Division: 6 / 3 = " + calculadora.dividir(6, 3));
    }
}