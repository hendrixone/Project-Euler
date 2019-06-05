package problem1_15;

public class Problem5 {

	public static void main(String[] args) {
		/*
		 * 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
		 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
		 */
		long tStart = System.currentTimeMillis();
		
		boolean breakout = true;
		for(int number = 6; breakout; number += 6) {
			for(int i = 1; i <= 20; i++) {
				if(number % i == 0) {
					if(i == 20) {
						System.out.println(number);
						breakout = false;
					}
					continue;
				}
				else
					break;
			}
		}
		
		System.out.println(System.currentTimeMillis() - tStart);
	}

}
