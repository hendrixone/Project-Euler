package problem1_15;

public class Problem3 {

	public static void main(String[] args) {
		/*
		 * The prime factors of 13195 are 5, 7, 13 and 29.
		 * What is the largest prime factor of the number 600851475143 ?
		 */
		long number = 600851475143L;
		int i;
		
		for(i = 1; number > 1;) {
			i++;
			if(number % i == 0)
				number /= i;
			
		}
		System.out.println(i);
	}

}
