package problem1_15;
import java.io.*;
public class  {
	
	public static void main(String[] args) {
		//创建文件对象f
		File f = new File("C:/Users/77431/Desktop/workspace/Project Euler/bin/resource/E11.txt");
		//创建char数组，其长度为文件长度
		char input[] = new char[(int)f.length()];
		//创建基于对象的reader
		try(FileReader fr = new FileReader(f)){
			//以字符流的形式读取文件内容
			fr.read(input);
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		//将string类型数组input[]转换为2维int类型数组list[][]
		int list[][] = new int[20][20];
		for(int row = 0, col = 0, i = 0; row < 20;) {							//历边list[][]
			if(col == 20) {
				col = 0;
				row++;
			}
			if(row == 20)
				break;
			if(input[i] == ' ' || input[i] == '\n' || input[i] == '\r') {		//若是空格则跳过
				i++;
			}else {
				list[row][col] = 10 * (input[i]-48) + (input[i+1] - 48);		//若是数字则转换为int
				i+=2;
				col++;
			}
		}
		int max = 0;
		//通过枚举法找到最大乘积		4种路径：横--,竖|,正斜/,反斜\
		//横
		for(int i = 0, k = 0; i < 20; k++) {
			if(k == 17) {
				k = -1;
				i++;
				continue;
			}
			if(list[i][k] * list[i][k+1] * list[i][k+2] * list[i][k+3] > max)
				max = list[i][k] * list[i][k+1] * list[i][k+2] * list[i][k+3];
		}
		//竖
		for(int i = 0, k = 0; i < 17; k++) {
			if(k == 20) {
				k = -1;
				i++;
				continue;
			}
			if(list[i][k] * list[i+1][k] * list[i+2][k] * list[i+3][k] > max)
				max = list[i][k] * list[i+1][k] * list[i+2][k] * list[i+3][k];
		}
		//正斜/
		for(int i = 0, k = 3; i < 17; k++) {
			if(k == 20) {
				k = 2;
				i++;
				continue;
			}
			if(list[i][k] * list[i+1][k-1] * list[i+2][k-2] * list[i+3][k-3] > max)
				max = list[i][k] * list[i+1][k-1] * list[i+2][k-2] * list[i+3][k-3];
		}
		//反斜\
		for(int i = 0, k = 0; i < 17; k++) {
			if(k == 17) {
				k = -1;
				i++;
				continue;
			}
			if(list[i][k] * list[i+1][k+1] * list[i+2][k+2] * list[i+3][k+3] > max)
				max = list[i][k] * list[i+1][k+1] * list[i+2][k+2] * list[i+3][k+3];
		}
		
		System.out.println(max);
	}
	
}













