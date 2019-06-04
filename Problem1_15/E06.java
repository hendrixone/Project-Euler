package pu1_10;

public class E06 {
	public static void main(String[] args) {
		/*
		The sum of the squares of the first ten natural numbers is,

		1^2 + 2^2 + ... + 10^2 = 385
		The square of the sum of the first ten natural numbers is,

		(1 + 2 + ... + 10)^2 = 55^2 = 3025
		Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

		Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
		 */
		
		long tStart = System.currentTimeMillis();
		
		long sum = 0;
		long sumOfSquare = 0;
		for(int i = 1; i <= 100; i++) {
			sum += i;
			sumOfSquare += (i * i);
		}
		
		System.out.println(sum * sum);
		System.out.println(sumOfSquare);
		System.out.println((sum*sum) - sumOfSquare);
		
		System.out.println(System.currentTimeMillis() - tStart);
	}

}
