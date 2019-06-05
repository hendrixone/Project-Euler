package problem1_15;

public class Problem9 {

	public static void main(String[] args) {
		/*
		 * A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
		 * a^2 + b^2 = c^2
		 * There exists exactly one Pythagorean triplet for which a + b + c = 1000.
		 * Find the product abc.
		 */
		
		long tStart = System.currentTimeMillis();
		
		int a;
		int b;
		int c;
		
		for(a = 1, b = 1, c = 0; a < 400; b++) {
			c = (int)Math.sqrt((a*a) + (b*b));
				if(a + b + c == 1000) {
					System.out.println(a*b*c + "  ");
					System.out.println(Math.sqrt(a*a + b*b));
				}
				if(a + b + c > 1000 || b > 400) {
					c = 0;
					a++;
					b = a;
				}
		}
		
		System.out.println("Done!\ntook " + (System.currentTimeMillis() - tStart) + "ms");
	}

}
