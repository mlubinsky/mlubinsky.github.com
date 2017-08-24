public class Board {
  // find # of pathes on board from top left to bootom right
  // solution #1
  public int count(int [][] arrA, int row, int col){ // recursive solution
     //base case
     //check if last row OR column is reached since after that only one path
     //is possible to reach to the bottom right corner.
     if(row==arrA.length-1 || col==arrA.length-1){
               return 1;
     }
     return count(arrA, row+1, col) + count(arrA, row, col+1);
  }
  // solution #2
  public int countDP(int [][] arrA){ // DP solution, no recursion
      int result [][] = new int[arrA.length][arrA.length];

      //base case: if we have one cell then there is only one way
      result[0][0] = 1;

      //no of paths to reach in any cell in first row = 1
      for (int i = 0; i <result.length ; i++) {
            result[0][i] = 1;
      }

			//no of paths to reach in any cell in first col = 1
			for (int i = 0; i <result.length ; i++) {
         result[i][0] = 1;
      }

      for (int i = 1; i <result.length ; i++) {
        for (int j = 1; j <result.length ; j++) {
                 result[i][j] = result[i-1][j] + result[i][j-1];
        }
      }

      return result[arrA.length-1][arrA.length-1];
  }


//  Given a 2-d grid map of '1's (land) and '0's (water), count the number of islands.
//  An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
//  You may assume all four edges of the grid are all surrounded by water.
  public int numIslands(char[][] grid) {
    if(grid==null || grid.length==0||grid[0].length==0)
        return 0;

    int m = grid.length;
    int n = grid[0].length;

    int count=0;
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            if(grid[i][j]=='1'){
                count++;
                merge(grid, i, j);
            }
        }
    }

    return count;
}

public void merge(char[][] grid, int i, int j){
    int m=grid.length;
    int n=grid[0].length;

    if(i<0||i>=m||j<0||j>=n||grid[i][j]!='1')
        return;

    grid[i][j]='X';

    merge(grid, i-1, j);
    merge(grid, i+1, j);
    merge(grid, i, j-1);
    merge(grid, i, j+1);
}

// Minimum path sum using Dynamic programming
public int minPathSum(int[][] grid) {
    if(grid == null || grid.length==0)
        return 0;

    int m = grid.length;
    int n = grid[0].length;

    int[][] dp = new int[m][n];
    dp[0][0] = grid[0][0];

    // initialize top row
    for(int i=1; i<n; i++){
        dp[0][i] = dp[0][i-1] + grid[0][i];
    }

    // initialize left column
    for(int j=1; j<m; j++){
        dp[j][0] = dp[j-1][0] + grid[j][0];
    }

    // fill up the dp table
    for(int i=1; i<m; i++){
        for(int j=1; j<n; j++){
            if(dp[i-1][j] > dp[i][j-1]){
                dp[i][j] = dp[i][j-1] + grid[i][j];
            }else{
                dp[i][j] = dp[i-1][j] + grid[i][j];
            }
        }
    }

    return dp[m-1][n-1];
}

  public static void main(String[] args) {
			int arrA [][] = {{1,1,1},{1,1,1},{1,1,1}};
			Board noOfPaths = new Board();
			System.out.println("No Of Path (Recursion):- " +noOfPaths.count(arrA,0,0));
			System.out.println("No Of Path (DP):- " +noOfPaths.countDP(arrA));
	 }
}

