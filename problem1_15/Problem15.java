package problem1_15;

public class Problem15 {

	public static void main(String[] args) {
		long grid[][] = new long[21][21];
		
		for(int i = 0; i < 21; i++) {
			grid[0][i] = 1;
			grid[i][0] = 1;
		}
		for(int i = 0, k = 0; i < 21; k++) {
			if(k == 21) {
				k = -1;
				i++;
				continue;
			}
		}
		
		for(int i = 1, k = 1; i < 21; k++) {
			if(k == 21) {
				k = 0;
				i++;
				continue;
			}
			grid[i][k] = grid[i - 1][k] + grid[i][k - 1];
		}
		
		for(int i = 0, k = 0; i < 21; k++) {
			if(k == 21) {
				k = -1;
				i++;
				continue;
			}
		}
		
		System.out.println(grid[20][20]);
	}

}
