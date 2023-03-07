// Write your code here
   public PerformOperation isOdd() {
    return a -> a % 2 != 0;
}

public PerformOperation isPrime() {
    return a -> (a == 1 || a == 2) || (a % 2 != 0 && a % 3 != 0);

    }

public PerformOperation isPalindrome() {
    return a -> isPalindromeChecker(String.valueOf(a));
}

private boolean isPalindromeChecker(String s) {
    int start = 0;
    int end = s.length() - 1;

    while (start < end) {
        if (s.charAt(start) != s.charAt(end)) {
            return false;
        }
        start++;
        end--;
    }

    return true;
}
}

