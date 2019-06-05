package problem16_30;

public class Problem16 {

	public static void main(String[] args) {
		//创建容器以放置2的1000次方，101位数
		int list[] = new int[310];
		list[0] = 1;
		for(int i = 0; i < 200; i++) {								//重复200次
			for(int index = 0; index < list.length; index++) {
				list[index] *= 32;									//每次每位乘以2的5次方，200*5得1000
			}
			for(int k = 0;k < list.length;k++) {					//满十进一
				if(list[k] >= 10) {
					list[k + 1] += (list[k]/10);
					list[k] %= 10;
				}
				else
					continue;
			}
		}
		int sum = 0;
		for(int i = 0; i < list.length; i++)						//输出
			sum+= list[i];
		System.out.println(sum);
	}

}
