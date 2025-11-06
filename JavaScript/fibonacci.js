/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */

function main(){
    let fib = 0
    for (let i = 0 ; i  != 50 ; i++){

        if (fib != 50){
            fib = fib + i
        }
        else
            return fib
    }
}

main()
