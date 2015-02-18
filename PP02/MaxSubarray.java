public class MaxSubarray {

	public static int[] bruteFindMaxSubarray (int[] myArray, int n) {
		int maxSum = -(2^31);
		int left = 0;
		int right = 0;
		for (int i=0; i<n; i++) {
			int currentSum = 0;
			for (int j=i; j<n; j++) {
				currentSum += myArray[j];
				if (currentSum>maxSum) {
					maxSum = currentSum;
					left = i;
					right = j;
				}
			}
		}
		int[] answer = new int[3];
		answer[0] = left;
		answer[1] = right;
		answer[2] = maxSum;
		return answer;
	}

	public static int[] findMaxCrossingSubarray (int[] myArray, int low, int mid, int high) {
		int leftSum = -(2^31);
		int maxLeft = 0;
		int rightSum = -(2^31);
		int maxRight = 0;
		int sum = 0;
		for (int i=mid; i>=low; i--) {
			sum += myArray[i];
			if (sum>leftSum) {
				leftSum = sum;
				maxLeft = i;
			}
		}
		sum = 0;
		for (int j=mid+1; j<high; j++) {
			sum += myArray[j];
			if (sum>rightSum) {
				rightSum = sum;
				maxRight = j;
			}
		}
		int[] answer = new int[3];
		answer[0] = maxLeft;
		answer[1] = maxRight;
		answer[2] = leftSum+rightSum;
		return answer;
	}

	public static int[] recursiveFindMaxSubarray (int[] myArray, int low, int high) {
		int[] answer = new int[3];
		int[] lefts = new int[3];
		int[] rights = new int[3];
		int[] crosses = new int[3];
		if (high==low) {
			System.out.println("base case, low is "+low);
			answer[0] = low;
			answer[1] = high;
			answer[2] = myArray[low];
			return answer;
		} else {
			int mid = (int)Math.floor((low+high)/2);
			System.out.println("mid is "+mid);
			lefts = recursiveFindMaxSubarray(myArray, low, mid);
			System.out.println("finding left...");
			rights = recursiveFindMaxSubarray(myArray, (mid+1), high);
			System.out.println("finding right...");
			crosses = findMaxCrossingSubarray(myArray, low, mid, high);
			System.out.println("finding cross...");
			if (lefts[2]>=rights[2] && lefts[2]>=crosses[2]) {
				System.out.println("left wins");
				answer[0] = lefts[0];
				answer[1] = lefts[1];
				answer[2] = lefts[2];
				return answer;
			}
			else if (rights[2]>=lefts[2] && rights[2]>=crosses[2]) {
				System.out.println("right wins");
				answer[0] = rights[0];
				answer[1] = rights[1];
				answer[2] = rights[2];
				return answer;
			}
			else {
				System.out.println("cross wins");
				answer[0] = crosses[0];
				answer[1] = crosses[1];
				answer[2] = crosses[2];
				return answer;
			}
		}
	}
	
	public static void main(String[] args) {
		int[] testArray = {-5,3,-1,2,-7,8};
		
		System.out.println("This is the brute force method of the maximum subarray problem.");
		long startBTime = System.currentTimeMillis();
		int[] testBAnswer = bruteFindMaxSubarray(testArray, testArray.length);
		long endBTime = System.currentTimeMillis();
		long totalBTime = endBTime-startBTime;
		System.out.println("N: "+testArray.length+" Total time: "+totalBTime);
		System.out.println("Left: "+testBAnswer[0]+" Right: "+testBAnswer[1]+" Sum: "+testBAnswer[2]);

		System.out.println("This is the recursive method of the maximum subarray problem.");
		long startRTime = System.currentTimeMillis();
		int[] testRAnswer = recursiveFindMaxSubarray(testArray, 0,testArray.length);
		long endRTime = System.currentTimeMillis();
		long totalRTime = endRTime-startRTime;
		System.out.println("N: "+testArray.length+" Total time: "+totalRTime);
		System.out.println("Left: "+testRAnswer[0]+" Right: "+testRAnswer[1]+" Sum: "+testRAnswer[2]);
	}
}