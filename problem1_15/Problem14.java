package problem1_15;

public class Problem14 {

	public static void main(String[] args) {
		long max = 0;
		for(long i = 13, count = 2, temp = 0; i < 1000000; i++) {
			temp = i;
			while(true) {
				if(temp % 2 == 0) {
					if(temp / 2 == 1)
						break;
					temp /= 2;
				}
				else
					temp = (temp * 3) + 1;
				count++;
			}
			if(count > max) {
				max = count;
				System.out.print(i + " ");
				System.out.println(max);
			}
			count = 2;
		}

	}

}
