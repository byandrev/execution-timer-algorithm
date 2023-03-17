<?php
$line = explode(" ", trim(fgets(STDIN)));
$a = $line[0];
$b = $line[1];


$p = array(); // Crea matriz
for ($i = 0; $i < $a; $i++) {
    
    $row = explode(" ", trim(fgets(STDIN)));
    
      for ($j = 0; $j < $b; $j++) {
        $x = intval($row[$j]); // Lee números que conforman la matriz
        
        $p[$i][$j] = $x; // Guarda el número en la matriz
        
        if ($i % 2 == 0) { // Si i es número par le suma 1
          $p[$i][$j] += 1;
        }
        if ($j % 2 == 0) { // Si j es un número par le suma 2
          $p[$i][$j] += 2;
        }
        if ($i % 2 != 0 && $j % 2 != 0) { // Si i y j son números impares le resta 3
          $p[$i][$j] -= 3;
        }
      }
}
// Imprime la matriz loca resultante
for ($i = 0; $i < $a; $i++) {
  for ($j = 0; $j < $b; $j++) {
    echo $p[$i][$j];
    if ($j < $b - 1) {
      echo " ";
    }
  }
  echo PHP_EOL;
}
?>

