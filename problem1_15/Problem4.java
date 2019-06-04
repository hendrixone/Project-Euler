package problem1_15;
public class Problem4 {

	public static void main(String[] args) {
		/*
		 * A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
		 * Find the largest palindrome made from the product of two 3-digit numbers.
		 */
		
		for(int i = 1, k = 1 ,temp = 0; i < 1000;k++) {
			int product = i * k;
			String number = String.valueOf(product);
			int length = number.length();
			for(int i1 = 0; i1 < (length / 2); i1 ++) {
				if (number.charAt(i1) == number.charAt(length - 1 - i1)) {
					if(i1 == (length / 2 - 1)) {
						if(product > temp) {
							temp = product;
							System.out.println(product);
						}
						break;
					}
				}
				else
					break;
			}
			if(k == 999) {
				k = 0;
				i++;
			}
		}
	}
}

