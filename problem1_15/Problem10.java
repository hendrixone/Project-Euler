package problem1_15;

public class  {
	
	public static void main(String[] args) {
		/*
		 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
		 * Find the sum of all the primes below two million.
		 */
		
		// 素数计算器
		
		long tStart = System.currentTimeMillis();
		
		int upperBound = 2000000;		//素数最大值
		int count = 2000000;				//最大个数
		
		//初始化一个大小为upperBound的布尔数组，除0,1,双数以外全部标为true;
		boolean list[] = new boolean[upperBound + 1];
		list[2] = true;
		for(int i = 2; i < upperBound + 1; i++)
			if(i % 2 != 0)
				list[i] = true;
		
		//从i开始，讲往后所有i的倍数标为false，然后找到下一个数并重复，直至i等于upperBound的平方根，此时该列表内所有true为素数
		for(int i = 3; i < Math.sqrt(upperBound); i++) {
			if(list[i] == false)
				continue;
			for(int k = 2; i*k < upperBound; k++) {
				list[i*k] = false;
			}
		}
		
		//输出所有非零数，并计数
		long sum = 0;
		
		for(int i = 0, k = 1; i < upperBound; i++) {
			if(list[i] == true) {
				//System.out.println(i+" "+ k++);
				sum += i;
			}
			if(k > count)
				break;
		}
		
		System.out.println(sum);
		
		System.out.println("Done!\ntook " + (System.currentTimeMillis() - tStart) + "ms");
	}

}
