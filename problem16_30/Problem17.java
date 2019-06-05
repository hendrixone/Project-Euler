package problem16_30;

public class Problem17 {

	public static void main(String[] args) {
		//one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety 
		int sum = 0;
		for(int i = 1; i <= 1000; i++) {
			sum += getOnes(i);
		}
		System.out.println(sum);
	}
	static int getOnes(int num) {
		if(num < 10) {
			switch(num) {
			case 1: return 3;
			case 2: return 3;	
			case 3: return 5;	
			case 4: return 4;	
			case 5: return 4;	
			case 6: return 3;	
			case 7: return 5;
			case 8: return 5;
			case 9: return 4;
			default: return 0;
			}
		}else {
			return get10s(num);
		}
	}
	static int get10s(int num) {
		if(num < 20) {
			switch(num) {
			case 11: return 6;
			case 12: return 6;	
			case 13: return 8;	
			case 14: return 8;	
			case 15: return 7;	
			case 16: return 7;	
			case 17: return 9;
			case 18: return 8;
			case 19: return 8;
			default: return 3;
			}
		}else {
			return get20s(num);
		}
	}
	static int get20s(int num) {
		if(num < 100) {
			switch(num/10) {
			case 2: return 6 + getOnes(num%10);
			case 3:	return 6 + getOnes(num%10);
			case 4:	return 5 + getOnes(num%10);
			case 5:	return 5 + getOnes(num%10);
			case 6:	return 5 + getOnes(num%10);
			case 7:	return 7 + getOnes(num%10);
			case 8:	return 6 + getOnes(num%10);
			case 9:	return 6 + getOnes(num%10);
			}
		}else {
			return get100s(num);
		}
		return 0;
	}
	static int get100s(int num) {
		if(num % 100 == 0) {
			return getOnes(num/100) + 7;
		}else {
			switch(num/100) {
			case 1: return 10 + getOnes(num%100) + 3;
			case 2: return 10 + getOnes(num%100) + 3;	
			case 3: return 12 + getOnes(num%100) + 3;	
			case 4: return 11 + getOnes(num%100) + 3;	
			case 5: return 11 + getOnes(num%100) + 3;	
			case 6: return 10 + getOnes(num%100) + 3;	
			case 7: return 12 + getOnes(num%100) + 3;
			case 8: return 12 + getOnes(num%100) + 3;
			case 9: return 11 + getOnes(num%100) + 3;
			default: return 11;
			}
		}
	}

}
