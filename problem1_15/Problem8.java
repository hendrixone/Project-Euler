package problem1_15;

public class Problem8 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		long tStart = System.currentTimeMillis();
		
		int upperBound = 1000000;
		
		//初始化一个大小为upperBound的布尔数组，除0,1,双数以外全部标为true;
		boolean list[] = new boolean[upperBound + 1];
		list[2] = true;
		for(int i = 2; i < upperBound + 1; i++)
			if(i % 2 != 0)
				list[i] = true;
		
		for(int i = 3; i < Math.sqrt(upperBound); i++) {
			if(list[i] == false)
				continue;
			for(int k = 2; i*k < upperBound; k++) {
				list[i*k] = false;
			}
		}
		for(int i = 0, k = 1; i < upperBound; i++) {
			if(list[i] == true)
				System.out.println(i+" "+ k++);
			if(k > 10001)
				break;
		}
		
		System.out.println("Done!\ntook " + (System.currentTimeMillis() - tStart) + "ms");
	}
	
}
