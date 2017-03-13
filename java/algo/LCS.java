public class LCS {

	public static int find(char[] A, char[] B) {
		int[][] LCS = new int[A.length + 1][B.length + 1];
		String[][] solution = new String[A.length + 1][B.length + 1];
		// if A is null then LCS of A, B =0
		for (int i = 0; i <= B.length; i++) {
			LCS[0][i] = 0;
			solution[0][i] = "0";
		}

		// if B is null then LCS of A, B =0
		for (int i = 0; i <= A.length; i++) {
			LCS[i][0] = 0;
			solution[i][0] = "0";
		}

		for (int i = 1; i <= A.length; i++) {
			for (int j = 1; j <= B.length; j++) {
				if (A[i - 1] == B[j - 1]) {
					LCS[i][j] = LCS[i - 1][j - 1] + 1;
					solution[i][j] = "diagonal";
				} else {
					LCS[i][j] = Math.max(LCS[i - 1][j], LCS[i][j - 1]);
					if (LCS[i][j] == LCS[i - 1][j]) {
						solution[i][j] = "top";
					} else {
						solution[i][j] = "left";
					}
				}
			}
		}
		// below code is to just print the result
		String x = solution[A.length][B.length];
		String answer = "";
		int a = A.length;
		int b = B.length;
		while (x != "0") {
			if (solution[a][b] == "diagonal") {
				answer = A[a - 1] + answer;
				a--;
				b--;
			} else if (solution[a][b] == "left") {
				b--;
			} else if (solution[a][b] == "top") {
				a--;
			}
			x = solution[a][b];
		}
		System.out.println("ANSWER="+answer);

		for (int i = 0; i <= A.length; i++) {
			for (int j = 0; j <= B.length; j++) {
				System.out.print(" " + LCS[i][j]);
			}
			System.out.println();
		}
		return LCS[A.length][B.length];
	}

	public static void main(String[] args) {
		String A = "ACBDEA";
		String B = "ABCDA";
        System.out.println("Input: " + A + " and " + B);
		System.out.println("Answer: LCS :" + find(A.toCharArray(), B.toCharArray()));
	}
}