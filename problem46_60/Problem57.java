package projectEuler;

import tools.PrimeGenerator;
/**
 * Solution for ProjectEuler problem 57 Spiral primes
 * @author Administrator
 *
 */
public class Problem57 {
	/*
	 * In this problem, we only need to deal with the numbers on the diagonal line of the spiral
	 * It's the pattern of the number on the diagonal is obvious, all number on the bottom right
	 * diagonal line are the square of the width of the spiral, follow the spiral to next number
	 * which is at the bottom left diagonal, it is length - 1 + the previous diagonal number
	 * apply same pattern to the rest 2 diagonal, it is easy to find all number on the diagonal
	 */
	public static void main(String[] args) {
		//set upper bound for the algorithm
		int length = 100000;
		
		//Initialize 4 arrays to store all numbers on the diagonal line
		int[] botLeft = new int[length];
		int[] topLeft = new int[length];
		int[] topRight = new int[length];
		int[] botRight = new int[length];
		
		//Initial spiral size
		int spiralSize = 3;
		
		//Apply the pattern, start from bottom right
		for(int i = 0; i < length; i++) {
			botRight[i] = spiralSize*spiralSize;
			botLeft[i] = botRight[i] - spiralSize + 1;
			topLeft[i] = botLeft[i] - spiralSize + 1;
			topRight[i] = topLeft[i] - spiralSize + 1;
			spiralSize += 2;
		}
		
		//Combine into on array for easier access
		int[][] allNums = {botRight, botLeft, topLeft, topRight};
		
		int total = 1;
		int primes = 0;
		
		//Go through spirals and count the primes
		for(int i = 0; i < length; i++) {
			for(int k = 0; k < allNums.length; k++) {
				if(PrimeGenerator.isPrime(allNums[k][i])) {
					primes++;
				}
				total++;
			}
			System.out.println((i+1)*2+1 +" "+ primes + "  " + total);
			//If the ratio is below 0.1, terminate
			if((double)primes / (double)total <= 0.1) {
				System.out.println((i+1)*2+1);
				return;
			}
		}
	}
}
