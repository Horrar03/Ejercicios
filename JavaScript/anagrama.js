/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */

function esAnagrama(palabra1, palabra2) {
    /*console.log(palabra1.toLowerCase());
    console.log(palabra2.toLowerCase());
    console.log(ordenada1, ordenada2);
    */
   
    ordenada1 = palabra1.toLowerCase().split('').sort();
    ordenada2 = palabra2.toLowerCase().split('').sort();

    //console.log(ordenada1, ordenada2);
    //console.log(ordenada1.length, ordenada2.length);

    
    for (let i = 0 ; i < ordenada1.length ; i++) {
        //console.log(i);
        //console.log(ordenada1[i], ordenada2[i]);
    
        if (ordenada1[i] != ordenada2[i]) {
            return false;
        }
    }
    
    return true;
}


console.log(esAnagrama("Poder", "Pedro"));
console.log(esAnagrama("Hola", "Adios"));
console.log(esAnagrama("Roma", "Amor"));