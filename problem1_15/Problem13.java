package problem1_15;
import java.io.*;
public class Probelm13 {

	public static void main(String[] args) {
		File f = new File("C:/Users/77431/Desktop/workspace/Project Euler/bin/resource/E13.txt");
		
		//读取文件
		char input[] = new char[(int)f.length()];
		try(FileReader fr = new FileReader(f)){
			fr.read(input);
		} catch(IOException e) {
			e.printStackTrace();
		}
		//将input里每一行数字字符转换成int类型放入list
		int[][] list = new int[100][50];
		for(int i = 0, k = 0, count = 0; i < 100;) {
			while( count < input.length && input[count] != '\r') {
				list[i][k] = input[count] - 48;
				count++;
				k++;
			}
			count+=2;
			i++;
			k=0;
		}
		//将每一位相加，移动到新的数组
		int result[] = new int[60];
		for(int i = 0, k = 0; k < 50;) {
			result[49-k] += list[i][k];
			if(++i == 100) {
				i = 0;
				k++;
			}
		}
		//满十进一，将大于10的部分移到下一位
		for(int i = 0;;i++) {
			if(result[i] >= 10) {
				result[i + 1] += (result[i]/10);
				result[i] %= 10;
			}
			else
				break;
		}
		//反向打印输出
		for(int i = result.length - 1; i >= 0; i--)
			System.out.print(result[i]);
	}

}
