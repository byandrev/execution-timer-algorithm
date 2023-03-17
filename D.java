import java.util.Scanner;

public class D
{
    public static void main(String []args){// 23n^3 + 11n + 2
        Scanner sc = new Scanner(System.in);//1

        byte A = sc.nextByte();//1
        byte B = sc.nextByte();//1
        byte matriz[][] = new byte[A][B];//1
        //1
        for(byte i=0; i<A; i++){//2+1+3n->6n*n -> 6n^2
            //1
            for(byte j=0; j<B; j++){//2+1 -> 3*n -> 3n
                matriz[i][j] = sc.nextByte();//1
            }
        }
        procesarMatriz(matriz);//1+17n^+1 -> 17n^2 + 2
        imp(matriz);//1+9n^2+1 -> 9n^2 +2
    }

    public static void procesarMatriz(byte matriz [][]){// 17n^2 + 1
        //1
        for(byte i=0; i<matriz.length; i++){//2+1+14n -> 17n*n -> 17n^2
            //1
            for(byte j=0; j<matriz[i].length; j++){//2+2+2+2+2+2 ->14*n -> 14n
                if(i%2==0){//2
                    matriz[i][j] += 1;//2
                }
                if(j%2==0){//2
                    matriz[i][j] += 2;//2
                }
                if(i%2!=0 && j%2!=0){//2
                    matriz[i][j] -= 3;//2
                }
            }
        }
    }

    public static void imp(byte matriz [][]){// 9n^2 + 1
        //1
        for(byte i=0; i<matriz.length; i++){//2+1+6n->9n*n -> 9n^2
            //1
            for(byte j=0; j<matriz[i].length; j++){//2+4*n->6n
                System.out.print(""+matriz[i][j]+(j<matriz[i].length-1?" ":"\n"));//4
            }
        }
    }
}