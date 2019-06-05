package problem1_15;

public class  {

	public static void main(String[] args) {
		for(int i = 1, num = 0, count = 0;;i++) {
			for(int k = 1; k < i;k++) {
				num+=k;
			}
			int temp = 0;
			if(num  % 2 == 0) {
				for(int k = 3; k <= num/2; k++) {
					if(num % k == 0) {
						temp = num / k;
						break;
					}
				}
				for(int k = 2; k <= temp; k++) {
					if (num % k == 0) {
						count++;
					}
				}
			}else {
				for(int k = 3; k <= num/3; k+=2) {
					if(num % k == 0) {
						temp = num / k;
						break;
					}
				}
				for(int k = 3; k <= temp; k+=2) {
					if (num % k == 0) {
							count++;
					}
				}
			}
			if(count >= 500) {
				System.out.println(num);
				break;
			}
			System.out.println(num+" "+count);
			count = 2;
			num = 0;
		}
		

	}

}
