// HSCTF 8
// misc: seeded-randomizer
// woanmeo11

import java.util.Random;

public class SeededRandomizer {
	public static void display(char[] arr) {
		for (char x: arr)
			System.out.print(x);
		System.out.println();
	}
	public static void main(String[] args) {
		// Instantiate another seeded randomizer below (seed is integer between 0 and 1000, exclusive):
		char[] flag = new char[33];
		int[] c = {13, 35, 15, -18, 88, 68, -72, -51, 73, -10, 63, 
				1, 35, -47, 6, -18, 10, 20, -31, 100, -48, 33, -12, 
				13, -24, 11, 20, -16, -10, -76, -63, -18, 118};
		for (int k = 0; k <= 1000; ++k) {
			Random rand = new Random(k);
			for (int i = 0; i < flag.length; i++) {
				int n = rand.nextInt(128) + c[i];
				flag[i] = (char)n;
			}
			if (new String(flag).indexOf("flag") != -1)
				display(flag);
		}
	}
}
